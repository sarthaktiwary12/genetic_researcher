"""MCP tool server for the UniProt REST API."""

import logging
from typing import Optional

from exrna_platform.mcp.base import MCPToolServer

logger = logging.getLogger(__name__)

_UNIPROT_BASE_URL = "https://rest.uniprot.org/"


class UniProtServer(MCPToolServer):
    """Rate-limited client for the UniProt REST API.

    Documentation: https://www.uniprot.org/help/api
    """

    def __init__(self, requests_per_second: float = 3.0):
        super().__init__(
            name="uniprot",
            base_url=_UNIPROT_BASE_URL,
            requests_per_second=requests_per_second,
        )

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _build_query(query: str, organism: Optional[str] = None) -> str:
        """Build a UniProt query string, optionally scoped to an organism.

        Parameters
        ----------
        query:
            Free-text or field-based search term.
        organism:
            Organism name or NCBI taxonomy ID.  When provided the query is
            wrapped with an ``AND organism_name:...`` clause.
        """
        if organism:
            return f"({query}) AND (organism_name:{organism})"
        return query

    @staticmethod
    def _parse_search_results(data: dict) -> list[dict]:
        """Normalise the UniProt search response into a list of dicts."""
        results: list[dict] = []
        for entry in data.get("results", []):
            accession = entry.get("primaryAccession", "")
            protein_name = ""
            if entry.get("proteinDescription", {}).get("recommendedName"):
                protein_name = (
                    entry["proteinDescription"]["recommendedName"]
                    .get("fullName", {})
                    .get("value", "")
                )
            elif entry.get("proteinDescription", {}).get("submissionNames"):
                names = entry["proteinDescription"]["submissionNames"]
                if names:
                    protein_name = names[0].get("fullName", {}).get("value", "")

            gene_names: list[str] = []
            for gene in entry.get("genes", []):
                if gene.get("geneName"):
                    gene_names.append(gene["geneName"].get("value", ""))

            organism_info = entry.get("organism", {})
            organism_name = organism_info.get("scientificName", "")
            taxon_id = organism_info.get("taxonId", "")

            results.append({
                "accession": accession,
                "protein_name": protein_name,
                "gene_names": gene_names,
                "organism": organism_name,
                "taxon_id": taxon_id,
            })
        return results

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    async def search(
        self,
        query: str,
        *,
        organism: Optional[str] = None,
        limit: int = 10,
        **kwargs,
    ) -> list[dict]:
        """Search UniProtKB.

        Parameters
        ----------
        query:
            Search term (gene name, protein name, keyword, etc.).
        organism:
            Optional organism filter (name or NCBI taxonomy ID).
        limit:
            Maximum number of results (default 10).

        Returns
        -------
        list[dict]
            Each entry has ``accession``, ``protein_name``, ``gene_names``,
            ``organism``, and ``taxon_id``.
        """
        full_query = self._build_query(query, organism)
        params = {
            "query": full_query,
            "format": "json",
            "size": str(limit),
        }

        logger.info("[uniprot] search query=%r organism=%s limit=%d", query, organism, limit)
        data = await self._get("uniprotkb/search", params=params)
        results = self._parse_search_results(data)
        logger.info("[uniprot] search returned %d results", len(results))
        return results

    async def fetch(self, accession: str, **kwargs) -> dict:
        """Fetch a single UniProtKB entry by accession.

        Parameters
        ----------
        accession:
            UniProt accession (e.g. ``"P12345"``).

        Returns
        -------
        dict
            Full UniProt JSON entry.
        """
        logger.info("[uniprot] fetch accession=%s", accession)
        data = await self._get(f"uniprotkb/{accession}", params={"format": "json"})
        return data

    async def get_orthologs(self, accession: str) -> list[dict]:
        """Retrieve ortholog information for a UniProt entry.

        Uses a search for entries in the same gene family across organisms,
        requesting organism and gene name fields.

        Parameters
        ----------
        accession:
            UniProt accession to find orthologs for.

        Returns
        -------
        list[dict]
            Each dict contains ``accession``, ``organism``, and ``gene_names``.
        """
        logger.info("[uniprot] get_orthologs accession=%s", accession)

        # First, fetch the source entry to learn the gene name.
        source = await self.fetch(accession)
        gene_names = []
        for gene in source.get("genes", []):
            if gene.get("geneName"):
                gene_names.append(gene["geneName"].get("value", ""))

        if not gene_names:
            logger.warning(
                "[uniprot] No gene name found for %s; cannot search orthologs.",
                accession,
            )
            return []

        gene_name = gene_names[0]
        params = {
            "query": f"(gene:{gene_name})",
            "fields": "accession,organism_name,gene_names",
            "format": "json",
            "size": "25",
        }

        data = await self._get("uniprotkb/search", params=params)
        results: list[dict] = []
        for entry in data.get("results", []):
            entry_accession = entry.get("primaryAccession", "")
            if entry_accession == accession:
                continue  # skip the query entry itself
            organism_name = entry.get("organism", {}).get("scientificName", "")
            entry_gene_names: list[str] = []
            for gene in entry.get("genes", []):
                if gene.get("geneName"):
                    entry_gene_names.append(gene["geneName"].get("value", ""))
            results.append({
                "accession": entry_accession,
                "organism": organism_name,
                "gene_names": entry_gene_names,
            })

        logger.info("[uniprot] get_orthologs found %d entries for gene=%s", len(results), gene_name)
        return results
