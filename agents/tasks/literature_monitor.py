"""Daily PubMed literature monitor.

Scans PubMed for new papers matching configurable keywords,
scores relevance via Gemini Flash, extracts claims via Claude Sonnet,
and stores results in the literature_alerts table.
"""

import asyncio
import logging
import time
from datetime import datetime, timedelta
from typing import Optional

from agents.config import KB_RESEARCH_LIT

logger = logging.getLogger(__name__)

# Default search keywords for exRNA germination research
DEFAULT_KEYWORDS = [
    "extracellular RNA seed germination",
    "bacterial small RNA plant",
    "cross-kingdom RNA interference",
    "EPS seed priming",
    "exRNA plant-microbe",
    "tRF plant defense",
    "antisense RNA germination vigor",
    "Spinacia oleracea germination",
    "seed priming bacterial",
]


class LiteratureMonitor:
    """Monitors PubMed for relevant new publications.

    Workflow:
    1. Search PubMed with configured keywords
    2. Fetch abstracts for new results
    3. Score relevance using Gemini Flash (cheap, fast)
    4. Extract claims from high-relevance papers using Claude Sonnet
    5. Store alerts in database
    """

    def __init__(
        self,
        pubmed_server,
        gemini_client=None,
        claude_client=None,
        db_session=None,
        keywords: Optional[list[str]] = None,
        relevance_threshold: float = 0.6,
    ):
        self.pubmed = pubmed_server
        self.gemini = gemini_client
        self.claude = claude_client
        self.db_session = db_session
        self.keywords = keywords or DEFAULT_KEYWORDS
        self.relevance_threshold = relevance_threshold

    async def scan(
        self,
        days_back: int = 1,
        max_results_per_keyword: int = 10,
    ) -> dict:
        """Run a full scan cycle.

        Args:
            days_back: How many days back to search.
            max_results_per_keyword: Max PubMed results per keyword search.

        Returns:
            Summary dict with counts and alert details.
        """
        start = time.time()
        min_date = (datetime.now() - timedelta(days=days_back)).strftime("%Y/%m/%d")
        max_date = datetime.now().strftime("%Y/%m/%d")

        logger.info(
            f"Literature scan: {len(self.keywords)} keywords, "
            f"date range {min_date} to {max_date}"
        )

        # Phase 1: Search PubMed
        all_pmids = set()
        for keyword in self.keywords:
            try:
                results = await self.pubmed.search(
                    query=keyword,
                    retmax=max_results_per_keyword,
                    mindate=min_date,
                    maxdate=max_date,
                )
                pmids = [r.get("id", r.get("uid", "")) for r in results if r]
                all_pmids.update(p for p in pmids if p)
                logger.debug(f"Keyword '{keyword}': {len(pmids)} results")
            except Exception as e:
                logger.warning(f"Search failed for '{keyword}': {e}")

        if not all_pmids:
            logger.info("No new papers found")
            return {"papers_found": 0, "alerts_created": 0, "duration_seconds": 0}

        logger.info(f"Found {len(all_pmids)} unique papers")

        # Phase 2: Fetch abstracts
        abstracts = {}
        pmid_list = list(all_pmids)
        try:
            results = await self.pubmed.fetch_abstracts(pmid_list)
            for item in results:
                pmid = item.get("pmid", "")
                if pmid:
                    abstracts[pmid] = item
        except Exception as e:
            logger.warning(f"Batch abstract fetch failed: {e}")
            # Fall back to individual fetches
            for pmid in pmid_list[:20]:  # Limit fallback
                try:
                    result = await self.pubmed.fetch(pmid)
                    if result:
                        abstracts[pmid] = result
                except Exception:
                    pass

        # Phase 3: Score relevance
        alerts = []
        for pmid, paper in abstracts.items():
            title = paper.get("title", "")
            abstract = paper.get("abstract", "")
            if not abstract:
                continue

            score, reason = await self._score_relevance(title, abstract)

            if score >= self.relevance_threshold:
                alert = {
                    "pmid": pmid,
                    "title": title,
                    "authors": paper.get("authors", ""),
                    "journal": paper.get("journal", ""),
                    "pub_date": paper.get("pub_date"),
                    "abstract": abstract,
                    "relevance_score": score,
                    "relevance_reason": reason,
                    "matched_keywords": _match_keywords(
                        f"{title} {abstract}", self.keywords
                    ),
                }

                # Phase 4: Extract claims from high-relevance papers
                if score >= 0.8 and self.claude:
                    claims = await self._extract_claims(title, abstract)
                    alert["claims_extracted"] = claims

                alerts.append(alert)

        # Phase 5: Store alerts
        stored_count = 0
        if self.db_session and alerts:
            stored_count = await self._store_alerts(alerts)

        # Also write to markdown for knowledge base
        if alerts:
            self._write_scan_summary(alerts)

        duration = time.time() - start
        result = {
            "papers_found": len(all_pmids),
            "abstracts_fetched": len(abstracts),
            "alerts_created": len(alerts),
            "alerts_stored": stored_count,
            "duration_seconds": round(duration, 1),
        }
        logger.info(f"Literature scan complete: {result}")
        return result

    async def _score_relevance(self, title: str, abstract: str) -> tuple[float, str]:
        """Score paper relevance using Gemini Flash."""
        if not self.gemini:
            # Fallback: keyword-based scoring
            text = f"{title} {abstract}".lower()
            score = sum(1 for kw in self.keywords if kw.lower() in text)
            normalized = min(score / 3.0, 1.0)
            return normalized, f"Keyword match: {score} keywords"

        prompt = f"""Rate the relevance of this paper to research on bacterial extracellular
small RNAs (exRNA) improving seed germination in crops. Score 0.0 to 1.0.

Title: {title}
Abstract: {abstract[:1500]}

Respond with ONLY a JSON object:
{{"score": 0.X, "reason": "brief explanation"}}"""

        try:
            response = await self.gemini.query_bulk(
                prompt=prompt,
                max_output_tokens=256,
                temperature=0.1,
            )
            import json
            # Extract JSON from response
            text = response.strip()
            if text.startswith("```"):
                text = text.split("```")[1].strip()
                if text.startswith("json"):
                    text = text[4:].strip()
            data = json.loads(text)
            return float(data.get("score", 0.5)), data.get("reason", "")
        except Exception as e:
            logger.warning(f"Relevance scoring failed: {e}")
            return 0.5, "scoring_error"

    async def _extract_claims(self, title: str, abstract: str) -> list[dict]:
        """Extract scientific claims from a paper using Claude Sonnet."""
        prompt = f"""Extract key scientific claims from this paper that are relevant to
exRNA, seed germination, or plant-microbe RNA transfer.

Title: {title}
Abstract: {abstract[:2000]}

For each claim, provide:
1. The claim text (one sentence)
2. Evidence level: DIRECT (stated in paper), INFERRED (reasonable inference), TANGENTIAL (related but indirect)
3. Relevant genes or pathways mentioned

Respond with a JSON array:
[{{"claim": "...", "evidence": "DIRECT|INFERRED|TANGENTIAL", "genes": ["..."], "pathways": ["..."]}}]"""

        try:
            response = await self.claude.query_synthesis(
                prompt=prompt,
                max_output_tokens=2048,
                temperature=0.3,
            )
            import json
            text = response.strip()
            if text.startswith("```"):
                text = text.split("```")[1].strip()
                if text.startswith("json"):
                    text = text[4:].strip()
            return json.loads(text)
        except Exception as e:
            logger.warning(f"Claim extraction failed: {e}")
            return []

    async def _store_alerts(self, alerts: list[dict]) -> int:
        """Store alerts in the literature_alerts database table."""
        from platform.db.postgres import LiteratureAlert
        from sqlalchemy import select

        stored = 0
        for alert in alerts:
            try:
                # Check if PMID already exists
                existing = await self.db_session.execute(
                    select(LiteratureAlert).where(LiteratureAlert.pmid == alert["pmid"])
                )
                if existing.scalar_one_or_none():
                    continue

                db_alert = LiteratureAlert(
                    pmid=alert["pmid"],
                    title=alert["title"],
                    authors=alert.get("authors", ""),
                    journal=alert.get("journal", ""),
                    abstract=alert.get("abstract", ""),
                    relevance_score=alert["relevance_score"],
                    relevance_reason=alert.get("relevance_reason", ""),
                    matched_keywords=alert.get("matched_keywords", []),
                    claims_extracted=alert.get("claims_extracted", []),
                )
                self.db_session.add(db_alert)
                stored += 1
            except Exception as e:
                logger.warning(f"Failed to store alert PMID:{alert['pmid']}: {e}")

        if stored:
            await self.db_session.commit()

        return stored

    def _write_scan_summary(self, alerts: list[dict]):
        """Write scan results to markdown for the knowledge base."""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
        output_path = KB_RESEARCH_LIT / f"pubmed_scan_{timestamp}.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)

        lines = [
            f"# PubMed Literature Scan — {timestamp}",
            f"> Found {len(alerts)} relevant papers\n",
        ]

        for alert in sorted(alerts, key=lambda x: -x["relevance_score"]):
            lines.append(f"## [{alert['title']}]")
            lines.append(f"- **PMID**: {alert['pmid']}")
            lines.append(f"- **Relevance**: {alert['relevance_score']:.2f}")
            lines.append(f"- **Reason**: {alert.get('relevance_reason', 'N/A')}")
            if alert.get("claims_extracted"):
                lines.append("- **Claims**:")
                for claim in alert["claims_extracted"]:
                    lines.append(f"  - [{claim.get('evidence', '?')}] {claim.get('claim', '')}")
            lines.append("")

        output_path.write_text("\n".join(lines))
        logger.info(f"Wrote scan summary: {output_path}")


def _match_keywords(text: str, keywords: list[str]) -> list[str]:
    """Return which keywords appear in the text."""
    text_lower = text.lower()
    return [kw for kw in keywords if kw.lower() in text_lower]


async def run(
    pubmed_server,
    gemini_client=None,
    claude_client=None,
    db_session=None,
    days_back: int = 1,
) -> dict:
    """Convenience function to run a single scan cycle."""
    monitor = LiteratureMonitor(
        pubmed_server=pubmed_server,
        gemini_client=gemini_client,
        claude_client=claude_client,
        db_session=db_session,
    )
    return await monitor.scan(days_back=days_back)
