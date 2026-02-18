"""Abstract base class for MCP tool servers with rate-limited aiohttp clients."""

import asyncio
import time
import logging
from abc import ABC, abstractmethod
from typing import Any, Optional

import aiohttp

logger = logging.getLogger(__name__)


class TokenBucket:
    """Simple token bucket rate limiter.

    Copied from agents/gemini_client.py for consistency across the codebase.
    """

    def __init__(self, rate: float, capacity: float):
        self.rate = rate          # tokens per second
        self.capacity = capacity  # max burst
        self.tokens = capacity
        self.last_refill = time.monotonic()
        self._lock = asyncio.Lock()

    async def acquire(self):
        async with self._lock:
            now = time.monotonic()
            elapsed = now - self.last_refill
            self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)
            self.last_refill = now

            if self.tokens < 1:
                wait_time = (1 - self.tokens) / self.rate
                await asyncio.sleep(wait_time)
                self.tokens = 0
            else:
                self.tokens -= 1


class MCPToolServer(ABC):
    """Abstract base class for biology API tool servers.

    Provides a rate-limited aiohttp client session with lazy initialization,
    JSON response parsing, and context manager support.

    Subclasses must implement ``search`` and ``fetch``.
    """

    def __init__(
        self,
        name: str,
        base_url: str,
        requests_per_second: float = 3.0,
    ):
        self.name = name
        self.base_url = base_url.rstrip("/")
        self.requests_per_second = requests_per_second
        self._session: Optional[aiohttp.ClientSession] = None
        self._rate_limiter = TokenBucket(
            rate=requests_per_second,
            capacity=max(requests_per_second, 1.0),
        )
        self._total_requests = 0
        self._total_errors = 0
        logger.info(
            "MCPToolServer '%s' initialised (base_url=%s, rate=%.1f req/s)",
            self.name,
            self.base_url,
            self.requests_per_second,
        )

    # ------------------------------------------------------------------
    # Session management
    # ------------------------------------------------------------------

    def _get_session(self) -> aiohttp.ClientSession:
        """Return the shared session, creating it lazily."""
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(
                headers={"Accept": "application/json"},
                timeout=aiohttp.ClientTimeout(total=30),
            )
        return self._session

    async def close(self) -> None:
        """Close the underlying HTTP session."""
        if self._session and not self._session.closed:
            await self._session.close()
            self._session = None
            logger.info("MCPToolServer '%s' session closed.", self.name)

    # ------------------------------------------------------------------
    # Context manager
    # ------------------------------------------------------------------

    async def __aenter__(self) -> "MCPToolServer":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()

    # ------------------------------------------------------------------
    # HTTP helper
    # ------------------------------------------------------------------

    async def _get(
        self,
        url: str,
        params: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> dict:
        """Perform a rate-limited GET request and return parsed JSON.

        Parameters
        ----------
        url:
            Full URL or path relative to ``self.base_url``.
        params:
            Optional query parameters.
        headers:
            Optional extra headers (merged with session defaults).

        Returns
        -------
        dict
            Parsed JSON response.

        Raises
        ------
        aiohttp.ClientResponseError
            On non-2xx status codes.
        """
        if not url.startswith("http"):
            url = f"{self.base_url}/{url.lstrip('/')}"

        await self._rate_limiter.acquire()
        session = self._get_session()

        logger.debug("[%s] GET %s params=%s", self.name, url, params)
        self._total_requests += 1

        try:
            async with session.get(url, params=params, headers=headers) as resp:
                resp.raise_for_status()
                return await resp.json(content_type=None)
        except aiohttp.ClientResponseError as exc:
            self._total_errors += 1
            logger.error(
                "[%s] HTTP %s for %s: %s",
                self.name,
                exc.status,
                url,
                exc.message,
            )
            raise
        except Exception as exc:
            self._total_errors += 1
            logger.error("[%s] Request failed for %s: %s", self.name, url, exc)
            raise

    async def _get_text(
        self,
        url: str,
        params: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> str:
        """Perform a rate-limited GET request and return raw text.

        Same contract as ``_get`` but returns text instead of JSON.  Useful
        for APIs that return XML or plain-text (e.g. PubMed efetch).
        """
        if not url.startswith("http"):
            url = f"{self.base_url}/{url.lstrip('/')}"

        await self._rate_limiter.acquire()
        session = self._get_session()

        logger.debug("[%s] GET (text) %s params=%s", self.name, url, params)
        self._total_requests += 1

        try:
            async with session.get(url, params=params, headers=headers) as resp:
                resp.raise_for_status()
                return await resp.text()
        except aiohttp.ClientResponseError as exc:
            self._total_errors += 1
            logger.error(
                "[%s] HTTP %s for %s: %s",
                self.name,
                exc.status,
                url,
                exc.message,
            )
            raise
        except Exception as exc:
            self._total_errors += 1
            logger.error("[%s] Request failed for %s: %s", self.name, url, exc)
            raise

    # ------------------------------------------------------------------
    # Abstract interface
    # ------------------------------------------------------------------

    @abstractmethod
    async def search(self, query: str, **kwargs) -> list[dict]:
        """Search the API for entries matching *query*."""
        ...

    @abstractmethod
    async def fetch(self, identifier: str) -> dict:
        """Fetch a single record by its identifier."""
        ...

    # ------------------------------------------------------------------
    # Stats
    # ------------------------------------------------------------------

    def get_stats(self) -> dict:
        """Return basic usage statistics."""
        return {
            "name": self.name,
            "total_requests": self._total_requests,
            "total_errors": self._total_errors,
        }

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__} name={self.name!r} "
            f"base_url={self.base_url!r} rate={self.requests_per_second} req/s>"
        )
