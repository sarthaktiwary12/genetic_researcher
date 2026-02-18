"""Migrate markdown knowledge base into ChromaDB vector collections.

Reads all markdown files from the knowledge base, chunks them by
``## `` section headers, and embeds each chunk into the appropriate
ChromaDB collection with rich metadata for filtered retrieval.

Collections used:
    gene_narratives    — Per-target gene analysis chunks
    research_findings  — Pathway, theme, and synthesis document chunks

Usage:
    python -m platform.migration.markdown_to_vectors
"""

import asyncio
import logging
import re
import sys
from pathlib import Path

# Ensure project root is on path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from agents.config import (
    CHROMA_PERSIST_DIR,
    KB_PATHWAYS,
    KB_SYNTHESIS,
    KB_TARGETS,
    KB_TARGETS_HIGH,
    KB_TARGETS_LOW,
    KB_TARGETS_MEDIUM,
    KB_THEMES,
    KNOWLEDGE_BASE,
    PROJECT_ROOT,
)
from exrna_platform.db.chroma_client import ChromaClient

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Markdown parsing helpers
# ---------------------------------------------------------------------------

_PRIORITY_RE = re.compile(r"^>\s*Priority:\s*(\w+)", re.MULTILINE)
_PATHWAY_RE = re.compile(r"^>\s*Pathway:\s*(\S+)", re.MULTILINE)
_GENE_TITLE_RE = re.compile(r"^#\s+(SOV\S+)\s*-\s*(.+)", re.MULTILINE)

# Section splitter: splits on lines starting with "## "
_SECTION_SPLIT_RE = re.compile(r"(?=^## )", re.MULTILINE)


def _read_text(path: Path) -> str:
    """Read file text, returning empty string on failure."""
    try:
        return path.read_text(encoding="utf-8")
    except Exception as exc:
        logger.warning("Could not read %s: %s", path, exc)
        return ""


def _extract_section_heading(section_text: str) -> str:
    """Extract the heading text from a section chunk.

    Given text starting with ``## Some Heading\\n...``, returns
    ``Some Heading``.
    """
    first_line = section_text.split("\n", 1)[0]
    heading = re.sub(r"^#+\s*", "", first_line).strip()
    return heading or "preamble"


def _make_doc_id(relative_path: str, section: str) -> str:
    """Create a deterministic doc_id from file path and section heading.

    Example: ``targets/high_priority/SOV3g035520_1_lox.md::Analysis``
    """
    # Sanitize section heading for use as ID component
    safe_section = re.sub(r"[^a-zA-Z0-9_\-]", "_", section)[:80]
    return f"{relative_path}::{safe_section}"


def chunk_markdown(text: str) -> list[dict]:
    """Split markdown text into chunks by ``## `` section headers.

    Returns list of dicts with keys: section, text.
    The preamble (content before the first ``## ``) is returned as
    a chunk with section="preamble".
    """
    if not text.strip():
        return []

    # Split on ## headers
    parts = _SECTION_SPLIT_RE.split(text)
    chunks: list[dict] = []

    for part in parts:
        part = part.strip()
        if not part:
            continue

        if part.startswith("## "):
            section = _extract_section_heading(part)
        else:
            section = "preamble"

        # Skip very short chunks (headers only, no content)
        if len(part) < 30:
            continue

        chunks.append({
            "section": section,
            "text": part,
        })

    return chunks


def _extract_gene_meta(text: str) -> dict:
    """Extract gene-specific metadata from target file text."""
    meta: dict = {}
    m = _GENE_TITLE_RE.search(text)
    if m:
        meta["gene_id"] = m.group(1).strip()
        meta["annotation"] = m.group(2).strip()
    m = _PRIORITY_RE.search(text)
    if m:
        meta["priority"] = m.group(1).strip().lower()
    m = _PATHWAY_RE.search(text)
    if m:
        meta["pathway"] = m.group(1).strip()
    return meta


# ---------------------------------------------------------------------------
# Ingestion functions
# ---------------------------------------------------------------------------

# ChromaDB maximum batch size to avoid memory issues
_BATCH_SIZE = 50


def _flush_batch(
    chroma: ChromaClient,
    collection_name: str,
    batch_ids: list[str],
    batch_texts: list[str],
    batch_metas: list[dict],
) -> int:
    """Upsert a batch of documents into ChromaDB and return count."""
    if not batch_ids:
        return 0
    chroma.add_documents_batch(
        collection_name=collection_name,
        doc_ids=batch_ids,
        texts=batch_texts,
        metadatas=batch_metas,
    )
    return len(batch_ids)


def ingest_targets(chroma: ChromaClient) -> int:
    """Ingest all target markdown files into the gene_narratives collection.

    Each ``## `` section becomes a separate document with metadata
    including gene_id, priority, pathway, and source_file.
    """
    collection_name = "gene_narratives"
    target_dirs = [KB_TARGETS_HIGH, KB_TARGETS_MEDIUM, KB_TARGETS_LOW]
    total = 0

    batch_ids: list[str] = []
    batch_texts: list[str] = []
    batch_metas: list[dict] = []

    for tdir in target_dirs:
        if not tdir.exists():
            logger.warning("Target directory not found: %s", tdir)
            continue

        for md_file in sorted(tdir.glob("*.md")):
            if md_file.name == "INDEX.md":
                continue

            text = _read_text(md_file)
            if not text:
                continue

            relative_path = str(md_file.relative_to(PROJECT_ROOT))
            gene_meta = _extract_gene_meta(text)
            chunks = chunk_markdown(text)

            for chunk in chunks:
                doc_id = _make_doc_id(relative_path, chunk["section"])
                metadata = {
                    "source_file": relative_path,
                    "section": chunk["section"],
                    "category": "target",
                    "gene_id": gene_meta.get("gene_id", ""),
                    "annotation": gene_meta.get("annotation", ""),
                    "priority": gene_meta.get("priority", ""),
                    "pathway": gene_meta.get("pathway", ""),
                }

                batch_ids.append(doc_id)
                batch_texts.append(chunk["text"])
                batch_metas.append(metadata)

                if len(batch_ids) >= _BATCH_SIZE:
                    total += _flush_batch(
                        chroma, collection_name,
                        batch_ids, batch_texts, batch_metas,
                    )
                    batch_ids, batch_texts, batch_metas = [], [], []

    # Flush remaining
    total += _flush_batch(chroma, collection_name, batch_ids, batch_texts, batch_metas)
    logger.info("Ingested %d chunks into %s", total, collection_name)
    return total


def ingest_research_findings(chroma: ChromaClient) -> int:
    """Ingest pathway, theme, and synthesis files into research_findings.

    Each ``## `` section becomes a separate document with metadata
    including source category, pathway/theme ID, and source file.
    """
    collection_name = "research_findings"
    total = 0

    batch_ids: list[str] = []
    batch_texts: list[str] = []
    batch_metas: list[dict] = []

    # Define source directories and their categories
    sources: list[tuple[Path, str]] = [
        (KB_PATHWAYS, "pathway"),
        (KB_THEMES, "theme"),
        (KB_SYNTHESIS, "synthesis"),
    ]

    for source_dir, category in sources:
        if not source_dir.exists():
            logger.warning("Directory not found: %s", source_dir)
            continue

        for md_file in sorted(source_dir.glob("*.md")):
            if md_file.name == "INDEX.md":
                continue

            text = _read_text(md_file)
            if not text:
                continue

            relative_path = str(md_file.relative_to(PROJECT_ROOT))
            chunks = chunk_markdown(text)

            for chunk in chunks:
                doc_id = _make_doc_id(relative_path, chunk["section"])

                # Build metadata specific to the source category
                metadata: dict = {
                    "source_file": relative_path,
                    "section": chunk["section"],
                    "category": category,
                }

                if category == "pathway":
                    metadata["pathway"] = md_file.stem
                elif category == "theme":
                    metadata["theme"] = md_file.stem

                # Extract any gene_id references within the chunk
                gene_refs = re.findall(r"SOV\w+\.\d+", chunk["text"])
                if gene_refs:
                    metadata["gene_ids_referenced"] = ",".join(
                        sorted(set(gene_refs))[:10]
                    )

                batch_ids.append(doc_id)
                batch_texts.append(chunk["text"])
                batch_metas.append(metadata)

                if len(batch_ids) >= _BATCH_SIZE:
                    total += _flush_batch(
                        chroma, collection_name,
                        batch_ids, batch_texts, batch_metas,
                    )
                    batch_ids, batch_texts, batch_metas = [], [], []

    # Flush remaining
    total += _flush_batch(chroma, collection_name, batch_ids, batch_texts, batch_metas)
    logger.info("Ingested %d chunks into %s", total, collection_name)
    return total


# ---------------------------------------------------------------------------
# Main migration orchestrator
# ---------------------------------------------------------------------------


async def main():
    """Run the full markdown-to-vectors migration.

    Although ChromaDB operations are synchronous, the function is async
    to match the project's async patterns and allow future migration to
    async embedding pipelines.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    logger.info("Starting markdown-to-vectors migration")
    logger.info("Knowledge base: %s", KNOWLEDGE_BASE)
    logger.info("ChromaDB persist dir: %s", CHROMA_PERSIST_DIR)

    chroma = ChromaClient(persist_dir=str(CHROMA_PERSIST_DIR))

    # Log pre-migration collection stats
    pre_stats = chroma.get_collection_stats()
    logger.info("Pre-migration collection counts: %s", pre_stats)

    # Ingest targets into gene_narratives
    target_count = ingest_targets(chroma)

    # Ingest pathways, themes, and synthesis into research_findings
    findings_count = ingest_research_findings(chroma)

    # Log post-migration collection stats
    post_stats = chroma.get_collection_stats()
    logger.info("Post-migration collection counts: %s", post_stats)

    summary = {
        "gene_narrative_chunks": target_count,
        "research_finding_chunks": findings_count,
        "collections": post_stats,
    }
    logger.info("Migration complete: %s", summary)
    return summary


if __name__ == "__main__":
    asyncio.run(main())
