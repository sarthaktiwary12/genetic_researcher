"""Writes analysis results to Neo4j knowledge graph.

Companion writer: every target/pathway/theme analysis also writes to Neo4j,
mirroring the existing markdown writer interfaces.
"""

import logging
from typing import Optional

from exrna_platform.db.neo4j_client import Neo4jClient

logger = logging.getLogger(__name__)


class GraphWriter:
    """Writes research outputs to Neo4j graph database."""

    def __init__(self, client: Neo4jClient):
        self.client = client

    async def write_target(
        self,
        gene_id: str,
        annotation: str,
        pathway: str,
        priority: str,
        organism: str = "Spinacia oleracea",
        chromosome: Optional[str] = None,
        tldr: str = "",
        analysis_summary: str = "",
    ) -> dict:
        """Write a gene target node and its pathway/crop relationships.

        Args:
            gene_id: Gene identifier (e.g., SOV3g040200.1).
            annotation: Gene annotation/description.
            pathway: Pathway classification key.
            priority: Priority level (high/medium/low).
            organism: Species name.
            chromosome: Chromosome location.
            tldr: Short summary.
            analysis_summary: Truncated analysis for graph storage.

        Returns:
            Write summary counters.
        """
        # Create/merge Gene node
        gene_props = {
            "annotation": annotation,
            "pathway": pathway,
            "priority": priority,
            "organism": organism,
            "tldr": tldr[:500],
        }
        if chromosome:
            gene_props["chromosome"] = chromosome
        if analysis_summary:
            gene_props["analysis_summary"] = analysis_summary[:1000]

        result = await self.client.merge_node("Gene", "gene_id", gene_id, gene_props)

        # Create/merge Pathway node and relationship
        await self.client.merge_node("Pathway", "pathway_id", pathway, {
            "name": pathway.replace("_", " ").title(),
        })
        await self.client.merge_relationship(
            "Gene", "gene_id", gene_id,
            "BELONGS_TO_PATHWAY",
            "Pathway", "pathway_id", pathway,
        )

        # Create/merge Crop node and relationship
        crop_key = organism.lower().replace(" ", "_")
        await self.client.merge_node("Crop", "species", crop_key, {
            "scientific_name": organism,
            "common_name": _common_name(organism),
        })
        await self.client.merge_relationship(
            "Gene", "gene_id", gene_id,
            "STUDIED_IN_CROP",
            "Crop", "species", crop_key,
        )

        logger.info(f"Graph: wrote target {gene_id} → {pathway} ({organism})")
        return result

    async def write_pathway(
        self,
        pathway_key: str,
        pathway_name: str,
        gene_ids: list[str],
        tldr: str = "",
    ) -> dict:
        """Write a pathway node and link its genes.

        Args:
            pathway_key: Pathway identifier.
            pathway_name: Human-readable name.
            gene_ids: List of gene IDs belonging to this pathway.
            tldr: Pathway summary.

        Returns:
            Write summary.
        """
        await self.client.merge_node("Pathway", "pathway_id", pathway_key, {
            "name": pathway_name,
            "gene_count": len(gene_ids),
            "tldr": tldr[:500],
        })

        for gid in gene_ids:
            await self.client.merge_relationship(
                "Gene", "gene_id", gid,
                "BELONGS_TO_PATHWAY",
                "Pathway", "pathway_id", pathway_key,
            )

        logger.info(f"Graph: wrote pathway {pathway_key} with {len(gene_ids)} genes")
        return {"pathway": pathway_key, "genes_linked": len(gene_ids)}

    async def write_theme(
        self,
        theme_id: str,
        theme_name: str,
        gene_ids: list[str],
        description: str = "",
    ) -> dict:
        """Write a theme node and link genes.

        Args:
            theme_id: Theme identifier.
            theme_name: Human-readable theme name.
            gene_ids: Genes associated with this theme.
            description: Theme description.

        Returns:
            Write summary.
        """
        await self.client.merge_node("Theme", "theme_id", theme_id, {
            "name": theme_name,
            "description": description[:500],
            "gene_count": len(gene_ids),
        })

        for gid in gene_ids:
            await self.client.merge_relationship(
                "Gene", "gene_id", gid,
                "HAS_THEME",
                "Theme", "theme_id", theme_id,
            )

        logger.info(f"Graph: wrote theme {theme_id} with {len(gene_ids)} genes")
        return {"theme": theme_id, "genes_linked": len(gene_ids)}

    async def write_claim(
        self,
        claim_id: str,
        text: str,
        evidence_level: str = "inferred",
        source: str = "",
        gene_ids: Optional[list[str]] = None,
    ) -> dict:
        """Write a claim node and link to supporting genes.

        Args:
            claim_id: Unique claim identifier.
            text: Claim text.
            evidence_level: known/inferred/speculative.
            source: Source document or analysis.
            gene_ids: Related gene IDs.

        Returns:
            Write summary.
        """
        await self.client.merge_node("Claim", "claim_id", claim_id, {
            "text": text[:1000],
            "evidence_level": evidence_level,
            "source": source,
        })

        for gid in (gene_ids or []):
            await self.client.merge_relationship(
                "Claim", "claim_id", claim_id,
                "SUPPORTED_BY_CLAIM",
                "Gene", "gene_id", gid,
            )

        logger.info(f"Graph: wrote claim {claim_id} ({evidence_level})")
        return {"claim": claim_id, "genes_linked": len(gene_ids or [])}

    async def write_paper(
        self,
        doi: str,
        title: str,
        authors: str = "",
        year: Optional[int] = None,
        gene_ids: Optional[list[str]] = None,
    ) -> dict:
        """Write a paper node and link cited genes."""
        props = {"title": title}
        if authors:
            props["authors"] = authors[:500]
        if year:
            props["year"] = year

        await self.client.merge_node("Paper", "doi", doi, props)

        for gid in (gene_ids or []):
            await self.client.merge_relationship(
                "Gene", "gene_id", gid,
                "CITED_IN_PAPER",
                "Paper", "doi", doi,
            )

        return {"paper": doi, "genes_linked": len(gene_ids or [])}


def _common_name(organism: str) -> str:
    """Map scientific name to common name."""
    mapping = {
        "Spinacia oleracea": "spinach",
        "Brassica oleracea": "broccoli",
        "Zea mays": "maize",
        "Triticum aestivum": "wheat",
        "Chenopodium quinoa": "quinoa",
        "Glycine max": "soybean",
        "Oryza sativa": "rice",
    }
    return mapping.get(organism, organism.split()[0].lower())
