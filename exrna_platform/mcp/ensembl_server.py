"""MCP tool server for the Ensembl Plants REST API."""

import logging
from typing import Any, Optional

from exrna_platform.mcp.base import MCPToolServer

logger = logging.getLogger(__name__)

_ENSEMBL_BASE_URL = "https://rest.ensembl.org/"

# Ensembl REST API allows up to 15 requests per second.
_DEFAULT_RATE = 15.0


class EnsemblServer(MCPToolServer):
    """Rate-limited client for the Ensembl REST API.

    Primarily targets **Ensembl Plants** endpoints but works with any
    Ensembl species.  Documentation: https://rest.ensembl.org/

    Parameters
    ----------
    requests_per_second:
        Maximum request rate (default 15, the documented Ensembl limit).
    """

    def __init__(self, requests_per_second: float = _DEFAULT_RATE):
        super().__init__(
            name="ensembl",
            base_url=_ENSEMBL_BASE_URL,
            requests_per_second=requests_per_second,
        )

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _parse_xref_results(data: list | dict) -> list[dict]:
        """Normalise the xrefs/symbol response into a list of dicts."""
        if isinstance(data, dict):
            # Single-hit responses are sometimes returned as a bare dict.
            data = [data]

        results: list[dict] = []
        for entry in data:
            results.append({
                "id": entry.get("id", ""),
                "type": entry.get("type", ""),
                "description": entry.get("description", ""),
                "species": entry.get("species", ""),
                "display_name": entry.get("display_name", ""),
            })
        return results

    @staticmethod
    def _parse_lookup(data: dict) -> dict:
        """Normalise a lookup/id response."""
        return {
            "id": data.get("id", ""),
            "display_name": data.get("display_name", ""),
            "species": data.get("species", ""),
            "biotype": data.get("biotype", ""),
            "object_type": data.get("object_type", ""),
            "description": data.get("description", ""),
            "source": data.get("source", ""),
            "logic_name": data.get("logic_name", ""),
            "seq_region_name": data.get("seq_region_name", ""),
            "start": data.get("start"),
            "end": data.get("end"),
            "strand": data.get("strand"),
            "assembly_name": data.get("assembly_name", ""),
        }

    @staticmethod
    def _parse_homology(data: dict) -> list[dict]:
        """Extract ortholog entries from a homology/id response."""
        homologies: list[dict] = []
        for entry in data.get("data", []):
            for hom in entry.get("homologies", []):
                target = hom.get("target", {})
                homologies.append({
                    "type": hom.get("type", ""),
                    "taxonomy_level": hom.get("taxonomy_level", ""),
                    "target_id": target.get("id", ""),
                    "target_species": target.get("species", ""),
                    "target_protein_id": target.get("protein_id", ""),
                    "target_description": target.get("description", ""),
                    "target_perc_id": target.get("perc_id"),
                    "source_perc_id": hom.get("source", {}).get("perc_id"),
                })
        return homologies

    # ------------------------------------------------------------------
    # Ensembl-specific headers
    # ------------------------------------------------------------------

    @staticmethod
    def _json_headers() -> dict[str, str]:
        """Ensembl REST requires an explicit Content-Type for JSON."""
        return {"Content-Type": "application/json"}

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    async def search(
        self,
        query: str,
        *,
        species: str = "spinacia_oleracea",
        **kwargs,
    ) -> list[dict]:
        """Look up a gene symbol via xrefs/symbol.

        Parameters
        ----------
        query:
            Gene symbol (e.g. ``"ABI3"``).
        species:
            Ensembl species string (default ``"spinacia_oleracea"``).

        Returns
        -------
        list[dict]
            Matching cross-reference entries with ``id``, ``type``,
            ``description``, ``species``, and ``display_name``.
        """
        url = f"xrefs/symbol/{species}/{query}"

        logger.info("[ensembl] search symbol=%r species=%s", query, species)
        try:
            data = await self._get(url, headers=self._json_headers())
        except Exception as exc:
            # Ensembl returns 400 for unknown symbols; treat as empty.
            logger.warning("[ensembl] search failed for %s/%s: %s", species, query, exc)
            return []

        results = self._parse_xref_results(data)
        logger.info("[ensembl] search returned %d hits", len(results))
        return results

    async def fetch(
        self,
        gene_id: str,
        *,
        species: str = "spinacia_oleracea",
        **kwargs,
    ) -> dict:
        """Fetch gene information by stable Ensembl ID.

        Parameters
        ----------
        gene_id:
            Ensembl stable ID (e.g. ``"ENSRNA049442065"``).
        species:
            Optional species hint (not used in the URL but logged).

        Returns
        -------
        dict
            Gene metadata including coordinates, biotype, and description.
        """
        url = f"lookup/id/{gene_id}"
        params: dict[str, str] = {"expand": "1"}

        logger.info("[ensembl] fetch gene_id=%s", gene_id)
        data = await self._get(url, params=params, headers=self._json_headers())
        return self._parse_lookup(data)

    async def get_orthologs(
        self,
        gene_id: str,
        *,
        ortholog_type: str = "orthologues",
        **kwargs,
    ) -> list[dict]:
        """Retrieve orthologs for a gene via the homology endpoint.

        Parameters
        ----------
        gene_id:
            Ensembl stable gene ID.
        ortholog_type:
            Homology type filter.  ``"orthologues"`` (default),
            ``"paralogues"``, or ``"all"``.

        Returns
        -------
        list[dict]
            Each dict has ``type``, ``taxonomy_level``, ``target_id``,
            ``target_species``, ``target_protein_id``,
            ``target_description``, ``target_perc_id``, and
            ``source_perc_id``.
        """
        url = f"homology/id/{gene_id}"
        params: dict[str, str] = {"type": ortholog_type}

        logger.info(
            "[ensembl] get_orthologs gene_id=%s type=%s", gene_id, ortholog_type
        )
        try:
            data = await self._get(url, params=params, headers=self._json_headers())
        except Exception as exc:
            logger.warning("[ensembl] get_orthologs failed for %s: %s", gene_id, exc)
            return []

        results = self._parse_homology(data)
        logger.info("[ensembl] get_orthologs found %d homologs", len(results))
        return results
