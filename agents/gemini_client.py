"""Async Gemini client with retry logic and rate limiting."""

import asyncio
import time
import logging
from typing import Optional
from google import genai
from google.genai import types

from agents.config import (
    GEMINI_API_KEY,
    MODEL_REASONING,
    MODEL_BULK,
    MAX_CONCURRENT_REQUESTS,
    RETRY_MAX_ATTEMPTS,
    RETRY_BASE_DELAY,
    RETRY_MAX_DELAY,
)

logger = logging.getLogger(__name__)


class TokenBucket:
    """Simple token bucket rate limiter."""

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


class GeminiClient:
    """Async wrapper around the Gemini API with retry and rate limiting."""

    def __init__(self, requests_per_minute: int = 300):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
        self.rate_limiter = TokenBucket(
            rate=requests_per_minute / 60.0,
            capacity=min(requests_per_minute / 6, 30),  # Allow small bursts
        )
        self.total_requests = 0
        self.total_tokens_used = 0
        self._lock = asyncio.Lock()

    async def _update_stats(self, tokens: int = 0):
        async with self._lock:
            self.total_requests += 1
            self.total_tokens_used += tokens

    async def query(
        self,
        prompt: str,
        model: Optional[str] = None,
        system_instruction: Optional[str] = None,
        temperature: float = 0.7,
        max_output_tokens: int = 8192,
    ) -> str:
        """Send a query to Gemini with retry and rate limiting.

        Args:
            prompt: The user prompt to send.
            model: Model name. Defaults to MODEL_BULK.
            system_instruction: Optional system instruction.
            temperature: Sampling temperature.
            max_output_tokens: Max response length.

        Returns:
            The text response from Gemini.
        """
        model = model or MODEL_BULK

        async with self.semaphore:
            await self.rate_limiter.acquire()
            return await self._query_with_retry(
                prompt, model, system_instruction, temperature, max_output_tokens
            )

    async def _query_with_retry(
        self,
        prompt: str,
        model: str,
        system_instruction: Optional[str],
        temperature: float,
        max_output_tokens: int,
    ) -> str:
        last_error = None

        for attempt in range(RETRY_MAX_ATTEMPTS):
            try:
                config = types.GenerateContentConfig(
                    temperature=temperature,
                    max_output_tokens=max_output_tokens,
                )
                if system_instruction:
                    config.system_instruction = system_instruction

                response = await asyncio.to_thread(
                    self.client.models.generate_content,
                    model=model,
                    contents=prompt,
                    config=config,
                )

                if response.text:
                    tokens = 0
                    if response.usage_metadata:
                        tokens = response.usage_metadata.total_token_count or 0
                    await self._update_stats(tokens)
                    logger.debug(
                        f"Query succeeded (attempt {attempt + 1}, tokens: {tokens})"
                    )
                    return response.text

                raise ValueError("Empty response from Gemini")

            except Exception as e:
                last_error = e
                delay = min(
                    RETRY_BASE_DELAY * (2 ** attempt),
                    RETRY_MAX_DELAY,
                )
                logger.warning(
                    f"Attempt {attempt + 1}/{RETRY_MAX_ATTEMPTS} failed: {e}. "
                    f"Retrying in {delay:.1f}s..."
                )
                await asyncio.sleep(delay)

        raise RuntimeError(
            f"All {RETRY_MAX_ATTEMPTS} attempts failed. Last error: {last_error}"
        )

    async def query_reasoning(
        self,
        prompt: str,
        system_instruction: Optional[str] = None,
        temperature: float = 0.7,
        max_output_tokens: int = 16384,
    ) -> str:
        """Use the reasoning-heavy model for deep analysis."""
        return await self.query(
            prompt=prompt,
            model=MODEL_REASONING,
            system_instruction=system_instruction,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        )

    async def query_bulk(
        self,
        prompt: str,
        system_instruction: Optional[str] = None,
        temperature: float = 0.5,
        max_output_tokens: int = 8192,
    ) -> str:
        """Use the fast model for bulk research."""
        return await self.query(
            prompt=prompt,
            model=MODEL_BULK,
            system_instruction=system_instruction,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        )

    async def batch_query(
        self,
        prompts: list[dict],
        model: Optional[str] = None,
    ) -> list[str]:
        """Run multiple queries in parallel with rate limiting.

        Args:
            prompts: List of dicts with 'prompt' and optional 'system_instruction'.
            model: Model to use for all queries.

        Returns:
            List of response texts in same order as prompts.
        """
        tasks = [
            self.query(
                prompt=p["prompt"],
                model=model,
                system_instruction=p.get("system_instruction"),
            )
            for p in prompts
        ]
        return await asyncio.gather(*tasks, return_exceptions=True)

    def get_stats(self) -> dict:
        """Return usage statistics."""
        return {
            "total_requests": self.total_requests,
            "total_tokens_used": self.total_tokens_used,
        }
