"""Async Anthropic client with retry logic and rate limiting.

Mirrors the GeminiClient pattern: TokenBucket rate limiter, semaphore
concurrency control, and exponential backoff retry.
"""

import asyncio
import time
import logging
from typing import Optional

import anthropic

from agents.config import (
    MAX_CONCURRENT_REQUESTS,
    RETRY_MAX_ATTEMPTS,
    RETRY_BASE_DELAY,
    RETRY_MAX_DELAY,
)

logger = logging.getLogger(__name__)

# Claude-specific defaults
CLAUDE_MODEL_OPUS = "claude-opus-4-6"
CLAUDE_MODEL_SONNET = "claude-sonnet-4-6"
CLAUDE_MODEL_HAIKU = "claude-haiku-4-5-20251001"
CLAUDE_REQUESTS_PER_MINUTE = 60


class TokenBucket:
    """Simple token bucket rate limiter."""

    def __init__(self, rate: float, capacity: float):
        self.rate = rate
        self.capacity = capacity
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


class ClaudeClient:
    """Async wrapper around the Anthropic API with retry and rate limiting."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        requests_per_minute: int = CLAUDE_REQUESTS_PER_MINUTE,
        max_concurrent: int = MAX_CONCURRENT_REQUESTS,
    ):
        self.client = anthropic.AsyncAnthropic(api_key=api_key)
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.rate_limiter = TokenBucket(
            rate=requests_per_minute / 60.0,
            capacity=min(requests_per_minute / 6, 10),
        )
        self.total_requests = 0
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_cost_usd = 0.0
        self._lock = asyncio.Lock()

    # Cost per million tokens (approximate)
    _COST_TABLE = {
        CLAUDE_MODEL_OPUS: {"input": 15.0, "output": 75.0},
        CLAUDE_MODEL_SONNET: {"input": 3.0, "output": 15.0},
        CLAUDE_MODEL_HAIKU: {"input": 0.80, "output": 4.0},
    }

    async def _update_stats(self, model: str, input_tokens: int, output_tokens: int):
        async with self._lock:
            self.total_requests += 1
            self.total_input_tokens += input_tokens
            self.total_output_tokens += output_tokens

            costs = self._COST_TABLE.get(model, {"input": 3.0, "output": 15.0})
            cost = (input_tokens * costs["input"] + output_tokens * costs["output"]) / 1_000_000
            self.total_cost_usd += cost

    async def query(
        self,
        prompt: str,
        model: Optional[str] = None,
        system_instruction: Optional[str] = None,
        temperature: float = 0.7,
        max_output_tokens: int = 8192,
    ) -> str:
        """Send a query to Claude with retry and rate limiting.

        Args:
            prompt: The user prompt to send.
            model: Model name. Defaults to CLAUDE_MODEL_SONNET.
            system_instruction: Optional system instruction.
            temperature: Sampling temperature.
            max_output_tokens: Max response length.

        Returns:
            The text response from Claude.
        """
        model = model or CLAUDE_MODEL_SONNET

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
                kwargs = {
                    "model": model,
                    "max_tokens": max_output_tokens,
                    "temperature": temperature,
                    "messages": [{"role": "user", "content": prompt}],
                }
                if system_instruction:
                    kwargs["system"] = system_instruction

                response = await self.client.messages.create(**kwargs)

                if response.content and response.content[0].text:
                    input_tokens = response.usage.input_tokens
                    output_tokens = response.usage.output_tokens
                    await self._update_stats(model, input_tokens, output_tokens)
                    logger.debug(
                        f"Query succeeded (attempt {attempt + 1}, "
                        f"tokens: {input_tokens}+{output_tokens})"
                    )
                    return response.content[0].text

                raise ValueError("Empty response from Claude")

            except anthropic.RateLimitError as e:
                last_error = e
                delay = min(RETRY_BASE_DELAY * (2 ** (attempt + 1)), RETRY_MAX_DELAY)
                logger.warning(
                    f"Rate limited (attempt {attempt + 1}/{RETRY_MAX_ATTEMPTS}). "
                    f"Retrying in {delay:.1f}s..."
                )
                await asyncio.sleep(delay)

            except anthropic.APIStatusError as e:
                last_error = e
                if e.status_code >= 500:
                    delay = min(RETRY_BASE_DELAY * (2 ** attempt), RETRY_MAX_DELAY)
                    logger.warning(
                        f"Server error {e.status_code} (attempt {attempt + 1}). "
                        f"Retrying in {delay:.1f}s..."
                    )
                    await asyncio.sleep(delay)
                else:
                    raise

            except Exception as e:
                last_error = e
                delay = min(RETRY_BASE_DELAY * (2 ** attempt), RETRY_MAX_DELAY)
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
        """Use Opus for deep analysis and critical review."""
        return await self.query(
            prompt=prompt,
            model=CLAUDE_MODEL_OPUS,
            system_instruction=system_instruction,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        )

    async def query_synthesis(
        self,
        prompt: str,
        system_instruction: Optional[str] = None,
        temperature: float = 0.5,
        max_output_tokens: int = 16384,
    ) -> str:
        """Use Sonnet for synthesis and claim extraction."""
        return await self.query(
            prompt=prompt,
            model=CLAUDE_MODEL_SONNET,
            system_instruction=system_instruction,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        )

    async def query_fast(
        self,
        prompt: str,
        system_instruction: Optional[str] = None,
        temperature: float = 0.3,
        max_output_tokens: int = 4096,
    ) -> str:
        """Use Haiku for fast, cheap classification and scoring."""
        return await self.query(
            prompt=prompt,
            model=CLAUDE_MODEL_HAIKU,
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
            "total_input_tokens": self.total_input_tokens,
            "total_output_tokens": self.total_output_tokens,
            "total_cost_usd": round(self.total_cost_usd, 4),
        }
