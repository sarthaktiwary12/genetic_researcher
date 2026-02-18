"""MCP tool server for the NCBI Entrez E-utilities API."""

import logging
import xml.etree.ElementTree as ET
from typing import Any, Optional

from exrna_platform.mcp.base import MCPToolServer

logger = logging.getLogger(__name__)

_NCBI_BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

# NCBI allows 10 req/s with an API key, 3 req/s without.
_RATE_WITH_KEY = 10.0
_RATE_WITHOUT_KEY = 3.0


class NCBIServer(MCPToolServer):
    """Rate-limited client for the NCBI Entrez E-utilities.

    Parameters
    ----------
    ncbi_api_key:
        Optional NCBI API key.  When provided the rate limit is raised
        from 3 to 10 requests per second.
    """

    def __init__(self, ncbi_api_key: Optional[str] = None):
        rate = _RATE_WITH_KEY if ncbi_api_key else _RATE_WITHOUT_KEY
        super().__init__(name="ncbi", base_url=_NCBI_BASE_URL, requests_per_second=rate)
        self._api_key = ncbi_api_key

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _base_params(self) -> dict[str, str]:
        """Return query params that should be included in every call."""
        params: dict[str, str] = {"retmode": "json"}
        if self._api_key:
            params["api_key"] = self._api_key
        return params

    def _base_params_xml(self) -> dict[str, str]:
        """Return base params for XML endpoints."""
        params: dict[str, str] = {"retmode": "xml"}
        if self._api_key:
            params["api_key"] = self._api_key
        return params

    @staticmethod
    def _parse_esearch_json(data: dict) -> list[dict]:
        """Extract id list and metadata from an esearch JSON response."""
        result = data.get("esearchresult", {})
        id_list = result.get("idlist", [])
        return [
            {
                "uid": uid,
                "count": result.get("count", "0"),
                "query_translation": result.get("querytranslation", ""),
            }
            for uid in id_list
        ]

    @staticmethod
    def _parse_efetch_xml(xml_text: str) -> dict:
        """Best-effort parse of efetch XML into a dict."""
        try:
            root = ET.fromstring(xml_text)
        except ET.ParseError:
            return {"raw": xml_text}

        result: dict[str, Any] = {}

        # Try to grab gene-level info (Entrezgene_gene / Gene-ref_locus etc.)
        for tag in root.iter():
            if tag.text and tag.text.strip():
                key = tag.tag.replace("-", "_")
                result.setdefault(key, tag.text.strip())

        return result

    @staticmethod
    def _parse_pubmed_abstract_xml(xml_text: str) -> dict:
        """Parse a PubMed efetch XML response into a structured dict."""
        try:
            root = ET.fromstring(xml_text)
        except ET.ParseError:
            return {"raw": xml_text}

        article = root.find(".//PubmedArticle")
        if article is None:
            return {"raw": xml_text}

        title_el = article.find(".//ArticleTitle")
        abstract_el = article.find(".//AbstractText")
        pmid_el = article.find(".//PMID")
        journal_el = article.find(".//Journal/Title")

        return {
            "pmid": pmid_el.text if pmid_el is not None else None,
            "title": title_el.text if title_el is not None else None,
            "abstract": abstract_el.text if abstract_el is not None else None,
            "journal": journal_el.text if journal_el is not None else None,
        }

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    async def search(
        self,
        query: str,
        *,
        db: str = "gene",
        retmax: int = 10,
        **kwargs,
    ) -> list[dict]:
        """Run an ESearch query against *db*.

        Parameters
        ----------
        query:
            Entrez search term (e.g. ``"ABI3[Gene] AND spinacia oleracea[Orgn]"``).
        db:
            NCBI database name (``gene``, ``pubmed``, ``nucleotide``, ...).
        retmax:
            Maximum number of UIDs to return.

        Returns
        -------
        list[dict]
            Each dict contains at least ``uid``, ``count``, and ``query_translation``.
        """
        params = self._base_params()
        params.update({"db": db, "term": query, "retmax": str(retmax)})

        logger.info("[ncbi] esearch db=%s query=%r retmax=%d", db, query, retmax)
        data = await self._get("esearch.fcgi", params=params)
        results = self._parse_esearch_json(data)
        logger.info("[ncbi] esearch returned %d UIDs", len(results))
        return results

    async def fetch(
        self,
        uid: str,
        *,
        db: str = "gene",
        **kwargs,
    ) -> dict:
        """Fetch a full record via EFetch.

        Parameters
        ----------
        uid:
            NCBI UID (e.g. gene ID or nucleotide GI).
        db:
            Database to fetch from.

        Returns
        -------
        dict
            Parsed record fields.
        """
        params = self._base_params_xml()
        params.update({"db": db, "id": uid})

        logger.info("[ncbi] efetch db=%s uid=%s", db, uid)
        xml_text = await self._get_text("efetch.fcgi", params=params)
        return self._parse_efetch_xml(xml_text)

    async def fetch_abstract(self, pmid: str) -> dict:
        """Fetch a PubMed abstract by PMID.

        Parameters
        ----------
        pmid:
            PubMed identifier (e.g. ``"12345678"``).

        Returns
        -------
        dict
            Keys: ``pmid``, ``title``, ``abstract``, ``journal``.
        """
        params = self._base_params_xml()
        params.update({
            "db": "pubmed",
            "id": pmid,
            "rettype": "abstract",
        })

        logger.info("[ncbi] fetch_abstract pmid=%s", pmid)
        xml_text = await self._get_text("efetch.fcgi", params=params)
        return self._parse_pubmed_abstract_xml(xml_text)
