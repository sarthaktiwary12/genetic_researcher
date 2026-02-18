"""Writes analysis results to ChromaDB vector store.

Companion writer: every analysis also embeds into ChromaDB alongside
the markdown writer output. Uses chunking by section for long documents.
"""

import logging
import re
from typing import Optional

from exrna_platform.db.chroma_client import ChromaClient

logger = logging.getLogger(__name__)

MAX_CHUNK_LENGTH = 8000  # Characters per chunk


class VectorWriter:
    """Writes research outputs to ChromaDB vector collections."""

    def __init__(self, client: ChromaClient):
        self.client = client

    def write_target(
        self,
        gene_id: str,
        annotation: str,
        pathway: str,
        priority: str,
        analysis: str,
        organism: str = "Spinacia oleracea",
        tldr: str = "",
    ):
        """Embed a gene target analysis into gene_narratives collection.

        Args:
            gene_id: Gene identifier.
            annotation: Gene annotation.
            pathway: Pathway classification.
            priority: Priority level.
            analysis: Full analysis text.
            organism: Species name.
            tldr: Short summary.
        """
        doc_id = f"target_{gene_id}"
        metadata = {
            "gene_id": gene_id,
            "annotation": annotation[:200],
            "pathway": pathway,
            "priority": priority,
            "organism": organism,
            "doc_type": "target_analysis",
        }

        # Use TL;DR + analysis as the embedded text
        text = f"{gene_id} - {annotation}\n{tldr}\n\n{analysis}"

        # Chunk if too long
        chunks = _chunk_by_sections(text, MAX_CHUNK_LENGTH)
        if len(chunks) == 1:
            self.client.add_document("gene_narratives", doc_id, chunks[0], metadata)
        else:
            ids = [f"{doc_id}_chunk{i}" for i in range(len(chunks))]
            metas = [{**metadata, "chunk": i} for i in range(len(chunks))]
            self.client.add_documents_batch("gene_narratives", ids, chunks, metas)

        logger.debug(f"Vector: wrote target {gene_id} ({len(chunks)} chunks)")

    def write_pathway(
        self,
        pathway_key: str,
        pathway_name: str,
        analysis: str,
        gene_ids: Optional[list[str]] = None,
        tldr: str = "",
    ):
        """Embed a pathway analysis into research_findings collection."""
        doc_id = f"pathway_{pathway_key}"
        metadata = {
            "pathway_id": pathway_key,
            "pathway_name": pathway_name,
            "doc_type": "pathway_analysis",
            "gene_count": len(gene_ids or []),
        }

        text = f"Pathway: {pathway_name}\n{tldr}\n\n{analysis}"
        chunks = _chunk_by_sections(text, MAX_CHUNK_LENGTH)

        if len(chunks) == 1:
            self.client.add_document("research_findings", doc_id, chunks[0], metadata)
        else:
            ids = [f"{doc_id}_chunk{i}" for i in range(len(chunks))]
            metas = [{**metadata, "chunk": i} for i in range(len(chunks))]
            self.client.add_documents_batch("research_findings", ids, chunks, metas)

        logger.debug(f"Vector: wrote pathway {pathway_key}")

    def write_theme(
        self,
        theme_id: str,
        theme_name: str,
        analysis: str,
        tldr: str = "",
    ):
        """Embed a theme analysis into research_findings collection."""
        doc_id = f"theme_{theme_id}"
        metadata = {
            "theme_id": theme_id,
            "theme_name": theme_name,
            "doc_type": "theme_analysis",
        }

        text = f"Theme: {theme_name}\n{tldr}\n\n{analysis}"
        self.client.add_document("research_findings", doc_id, text[:MAX_CHUNK_LENGTH], metadata)
        logger.debug(f"Vector: wrote theme {theme_id}")

    def write_synthesis(
        self,
        doc_name: str,
        content: str,
        doc_type: str = "synthesis",
    ):
        """Embed a synthesis document into research_findings."""
        doc_id = f"synthesis_{doc_name}"
        metadata = {"doc_type": doc_type, "source": doc_name}

        chunks = _chunk_by_sections(content, MAX_CHUNK_LENGTH)
        if len(chunks) == 1:
            self.client.add_document("research_findings", doc_id, chunks[0], metadata)
        else:
            ids = [f"{doc_id}_chunk{i}" for i in range(len(chunks))]
            metas = [{**metadata, "chunk": i} for i in range(len(chunks))]
            self.client.add_documents_batch("research_findings", ids, chunks, metas)

        logger.debug(f"Vector: wrote synthesis {doc_name} ({len(chunks)} chunks)")

    def write_literature(
        self,
        pmid: str,
        title: str,
        abstract: str,
        metadata: Optional[dict] = None,
    ):
        """Embed a literature entry (PubMed abstract) into literature collection."""
        doc_id = f"pubmed_{pmid}"
        meta = {
            "pmid": pmid,
            "title": title[:200],
            "doc_type": "pubmed_abstract",
            **(metadata or {}),
        }

        text = f"{title}\n\n{abstract}"
        self.client.add_document("literature", doc_id, text[:MAX_CHUNK_LENGTH], meta)
        logger.debug(f"Vector: wrote literature PMID:{pmid}")


def _chunk_by_sections(text: str, max_length: int) -> list[str]:
    """Split text by ## section headers, keeping chunks under max_length.

    If no sections or all sections are small, returns a single chunk.
    """
    if len(text) <= max_length:
        return [text]

    sections = re.split(r'\n(?=## )', text)
    chunks = []
    current_chunk = ""

    for section in sections:
        if len(current_chunk) + len(section) + 1 > max_length:
            if current_chunk:
                chunks.append(current_chunk.strip())
            # If a single section is too long, truncate it
            if len(section) > max_length:
                current_chunk = section[:max_length]
            else:
                current_chunk = section
        else:
            current_chunk = current_chunk + "\n" + section if current_chunk else section

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks if chunks else [text[:max_length]]
