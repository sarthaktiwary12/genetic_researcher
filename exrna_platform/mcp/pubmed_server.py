"""MCP tool server for PubMed search and abstract retrieval.

Built on top of the NCBI Entrez E-utilities, but specialised for the
``pubmed`` database with convenience helpers for abstract batch-fetching.
"""

import logging
import xml.etree.ElementTree as ET
from typing import Any, Optional

from exrna_platform.mcp.base import MCPToolServer

logger = logging.getLogger(__name__)

_NCBI_BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

# Same rate rules as NCBIServer: 10 req/s with key, 3 req/s without.
_RATE_WITH_KEY = 10.0
_RATE_WITHOUT_KEY = 3.0


class PubMedServer(MCPToolServer):
    """Rate-limited client for PubMed via NCBI E-utilities.

    While :class:`NCBIServer` is a general-purpose Entrez client, this
    server provides a PubMed-focused interface with helpers for relevance-
    sorted search, date filtering, and batch abstract retrieval.

    Parameters
    ----------
    ncbi_api_key:
        Optional NCBI API key.  Raises the rate limit from 3 to 10 req/s.
    """

    def __init__(self, ncbi_api_key: Optional[str] = None):
        rate = _RATE_WITH_KEY if ncbi_api_key else _RATE_WITHOUT_KEY
        super().__init__(
            name="pubmed",
            base_url=_NCBI_BASE_URL,
            requests_per_second=rate,
        )
        self._api_key = ncbi_api_key

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _base_params(self) -> dict[str, str]:
        params: dict[str, str] = {"retmode": "json"}
        if self._api_key:
            params["api_key"] = self._api_key
        return params

    def _base_params_xml(self) -> dict[str, str]:
        params: dict[str, str] = {"retmode": "xml"}
        if self._api_key:
            params["api_key"] = self._api_key
        return params

    @staticmethod
    def _parse_esearch_json(data: dict) -> list[dict]:
        """Extract PMIDs and metadata from an esearch response."""
        result = data.get("esearchresult", {})
        id_list = result.get("idlist", [])
        return [
            {
                "pmid": pmid,
                "count": result.get("count", "0"),
                "query_translation": result.get("querytranslation", ""),
            }
            for pmid in id_list
        ]

    @staticmethod
    def _parse_pubmed_xml(xml_text: str) -> list[dict]:
        """Parse PubMed efetch XML into a list of article dicts."""
        try:
            root = ET.fromstring(xml_text)
        except ET.ParseError:
            return [{"raw": xml_text}]

        articles: list[dict] = []

        for article_el in root.findall(".//PubmedArticle"):
            pmid_el = article_el.find(".//PMID")
            title_el = article_el.find(".//ArticleTitle")
            journal_el = article_el.find(".//Journal/Title")

            # Abstract can span multiple AbstractText elements (labelled sections).
            abstract_parts: list[str] = []
            for abs_el in article_el.findall(".//AbstractText"):
                label = abs_el.get("Label", "")
                text = abs_el.text or ""
                if label:
                    abstract_parts.append(f"{label}: {text}")
                else:
                    abstract_parts.append(text)

            # Authors
            authors: list[str] = []
            for author_el in article_el.findall(".//Author"):
                last = author_el.findtext("LastName", "")
                initials = author_el.findtext("Initials", "")
                if last:
                    authors.append(f"{last} {initials}".strip())

            # Publication date
            pub_date_el = article_el.find(".//PubDate")
            year = pub_date_el.findtext("Year", "") if pub_date_el is not None else ""
            month = pub_date_el.findtext("Month", "") if pub_date_el is not None else ""
            pub_date = f"{year} {month}".strip()

            # DOI
            doi = ""
            for eid in article_el.findall(".//ArticleId"):
                if eid.get("IdType") == "doi":
                    doi = eid.text or ""

            articles.append({
                "pmid": pmid_el.text if pmid_el is not None else None,
                "title": title_el.text if title_el is not None else None,
                "abstract": "\n".join(abstract_parts) if abstract_parts else None,
                "authors": authors,
                "journal": journal_el.text if journal_el is not None else None,
                "pub_date": pub_date,
                "doi": doi,
            })

        return articles

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    async def search(
        self,
        query: str,
        *,
        retmax: int = 20,
        sort: str = "relevance",
        mindate: Optional[str] = None,
        maxdate: Optional[str] = None,
        **kwargs,
    ) -> list[dict]:
        """Search PubMed and return matching PMIDs.

        Parameters
        ----------
        query:
            PubMed search query (standard Entrez syntax).
        retmax:
            Maximum number of results (default 20).
        sort:
            Sort order.  ``"relevance"`` (default) or ``"pub_date"``.
        mindate:
            Minimum publication date in ``YYYY/MM/DD`` format.
        maxdate:
            Maximum publication date in ``YYYY/MM/DD`` format.

        Returns
        -------
        list[dict]
            Each dict has ``pmid``, ``count``, and ``query_translation``.
        """
        params = self._base_params()
        params.update({
            "db": "pubmed",
            "term": query,
            "retmax": str(retmax),
            "sort": sort,
        })
        if mindate:
            params["mindate"] = mindate
            params["datetype"] = "pdat"
        if maxdate:
            params["maxdate"] = maxdate
            params["datetype"] = "pdat"

        logger.info(
            "[pubmed] search query=%r retmax=%d sort=%s mindate=%s maxdate=%s",
            query,
            retmax,
            sort,
            mindate,
            maxdate,
        )
        data = await self._get("esearch.fcgi", params=params)
        results = self._parse_esearch_json(data)
        logger.info("[pubmed] search returned %d PMIDs", len(results))
        return results

    async def fetch(self, pmid: str, **kwargs) -> dict:
        """Fetch a single PubMed article by PMID (XML).

        Parameters
        ----------
        pmid:
            PubMed identifier.

        Returns
        -------
        dict
            Parsed article with ``pmid``, ``title``, ``abstract``,
            ``authors``, ``journal``, ``pub_date``, and ``doi``.
        """
        params = self._base_params_xml()
        params.update({
            "db": "pubmed",
            "id": pmid,
            "rettype": "xml",
        })

        logger.info("[pubmed] fetch pmid=%s", pmid)
        xml_text = await self._get_text("efetch.fcgi", params=params)
        articles = self._parse_pubmed_xml(xml_text)
        if articles:
            return articles[0]
        return {"pmid": pmid, "error": "no article found in response"}

    async def fetch_abstracts(self, pmids: list[str]) -> list[dict]:
        """Batch-fetch abstracts for a list of PMIDs.

        NCBI efetch supports comma-separated IDs in a single request
        (up to ~200 at a time).  This method chunks larger lists
        automatically.

        Parameters
        ----------
        pmids:
            List of PubMed identifiers.

        Returns
        -------
        list[dict]
            One dict per article (same schema as :meth:`fetch`).
        """
        if not pmids:
            return []

        chunk_size = 200
        all_articles: list[dict] = []

        for i in range(0, len(pmids), chunk_size):
            chunk = pmids[i : i + chunk_size]
            params = self._base_params_xml()
            params.update({
                "db": "pubmed",
                "id": ",".join(chunk),
                "rettype": "xml",
            })

            logger.info(
                "[pubmed] fetch_abstracts batch %d-%d of %d",
                i,
                i + len(chunk),
                len(pmids),
            )
            xml_text = await self._get_text("efetch.fcgi", params=params)
            articles = self._parse_pubmed_xml(xml_text)
            all_articles.extend(articles)

        logger.info("[pubmed] fetch_abstracts returned %d articles", len(all_articles))
        return all_articles
