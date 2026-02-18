"""Migrate markdown knowledge base into Neo4j graph database.

Reads existing markdown files from the knowledge base and creates
Neo4j nodes and relationships for: Gene, Pathway, Theme, Crop, and Claim.

Usage:
    python -m platform.migration.markdown_to_graph
"""

import asyncio
import json
import logging
import re
import sys
from pathlib import Path
from typing import Optional

# Ensure project root is on path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from agents.config import (
    KNOWLEDGE_BASE,
    KB_PATHWAYS,
    KB_SYNTHESIS,
    KB_TARGETS,
    KB_TARGETS_HIGH,
    KB_TARGETS_LOW,
    KB_TARGETS_MEDIUM,
    KB_THEMES,
    NEO4J_PASSWORD,
    NEO4J_URI,
    NEO4J_USER,
    ORGANISM,
    PROJECT_ROOT,
    TARGETS_CONFIG,
    TREATMENT,
)
from exrna_platform.db.neo4j_client import Neo4jClient

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Markdown parsing helpers
# ---------------------------------------------------------------------------

_HEADER_RE = re.compile(r"^#\s+(.+)", re.MULTILINE)
_TLDR_RE = re.compile(r"^>\s*TL;DR:\s*(.+)", re.MULTILINE)
_PRIORITY_RE = re.compile(r"^>\s*Priority:\s*(\w+)", re.MULTILINE)
_PATHWAY_RE = re.compile(r"^>\s*Pathway:\s*(\S+)", re.MULTILINE)
_UPDATED_RE = re.compile(r"^>\s*Last Updated:\s*(.+)", re.MULTILINE)
_GENE_COUNT_RE = re.compile(r"^>\s*Genes:\s*(\d+)", re.MULTILINE)

# Pattern to extract gene_id and annotation from a target file title
# e.g. "SOV3g035520.1 - Lipoxygenase (LOX)"
_GENE_TITLE_RE = re.compile(r"^#\s+(SOV\S+)\s*-\s*(.+)", re.MULTILINE)

# Pattern to extract Gene Information block fields
_FIELD_RE = re.compile(r"\*\*(\w[\w\s]*?)\*\*:\s*(.+)")

# Pattern for gene table rows in pathway files
# | SOV4g032870.1 | Histidine-containing ... | high |
_TABLE_ROW_RE = re.compile(
    r"\|\s*(SOV\S+)\s*\|\s*(.+?)\s*\|\s*(\w+)\s*\|"
)

# Pattern to find claim-like sentences in synthesis files
# Captures sentences starting with strong assertion phrases
_CLAIM_RE = re.compile(
    r"(?:^|\.\s+)"
    r"((?:The |This |Downregulat|Bacterial |Simultaneous |Coordinated )"
    r"[^.]{30,250}\.)",
    re.MULTILINE,
)

# Pattern to detect ortholog references like "Arabidopsis *met1*"
_ORTHOLOG_RE = re.compile(
    r"(?:Arabidopsis|rice|maize|wheat|soybean)\s+\*?(\w+)\*?\s+(?:mutant|homolog|ortholog)",
    re.IGNORECASE,
)


def _read_text(path: Path) -> str:
    """Read file text, returning empty string on failure."""
    try:
        return path.read_text(encoding="utf-8")
    except Exception as exc:
        logger.warning("Could not read %s: %s", path, exc)
        return ""


def _extract_meta(text: str) -> dict:
    """Extract metadata from the YAML-like blockquote header of a markdown file."""
    meta: dict = {}
    m = _TLDR_RE.search(text)
    if m:
        meta["tldr"] = m.group(1).strip()
    m = _PRIORITY_RE.search(text)
    if m:
        meta["priority"] = m.group(1).strip().lower()
    m = _PATHWAY_RE.search(text)
    if m:
        meta["pathway"] = m.group(1).strip()
    m = _UPDATED_RE.search(text)
    if m:
        meta["last_updated"] = m.group(1).strip()
    m = _GENE_COUNT_RE.search(text)
    if m:
        meta["gene_count"] = int(m.group(1))
    return meta


# ---------------------------------------------------------------------------
# Parsers for each knowledge-base section
# ---------------------------------------------------------------------------


def parse_target_file(path: Path) -> Optional[dict]:
    """Parse a target markdown file into a gene dict.

    Returns dict with keys: gene_id, annotation, pathway, priority,
    tldr, last_updated, analysis_text, source_file, orthologs.
    """
    text = _read_text(path)
    if not text:
        return None

    gene: dict = {"source_file": str(path.relative_to(PROJECT_ROOT))}

    # Title line
    m = _GENE_TITLE_RE.search(text)
    if m:
        gene["gene_id"] = m.group(1).strip()
        gene["annotation"] = m.group(2).strip()

    # Blockquote metadata
    meta = _extract_meta(text)
    gene.update(meta)

    # Gene Information fields
    for fm in _FIELD_RE.finditer(text):
        key = fm.group(1).strip().lower().replace(" ", "_")
        val = fm.group(2).strip()
        if key == "gene_id" and "gene_id" not in gene:
            gene["gene_id"] = val
        elif key == "annotation" and "annotation" not in gene:
            gene["annotation"] = val
        elif key == "pathway" and "pathway" not in gene:
            gene["pathway"] = val
        elif key == "priority" and "priority" not in gene:
            gene["priority"] = val.lower()

    if "gene_id" not in gene:
        logger.warning("No gene_id found in %s, skipping", path)
        return None

    # Extract analysis text (everything under ## Analysis)
    analysis_match = re.search(r"## Analysis\s*\n(.+)", text, re.DOTALL)
    if analysis_match:
        gene["analysis_text"] = analysis_match.group(1).strip()[:5000]

    # Extract ortholog references
    orthologs = []
    for om in _ORTHOLOG_RE.finditer(text):
        orthologs.append(om.group(1).strip())
    gene["orthologs"] = list(set(orthologs))

    return gene


def parse_pathway_file(path: Path) -> Optional[dict]:
    """Parse a pathway markdown file.

    Returns dict with keys: pathway_id, title, tldr, gene_count,
    last_updated, genes (list of gene_id), analysis_text, source_file.
    """
    text = _read_text(path)
    if not text:
        return None

    pathway: dict = {
        "pathway_id": path.stem,
        "source_file": str(path.relative_to(PROJECT_ROOT)),
    }

    m = _HEADER_RE.search(text)
    if m:
        pathway["title"] = m.group(1).strip()

    meta = _extract_meta(text)
    pathway.update(meta)

    # Extract gene rows from table
    genes = []
    for row in _TABLE_ROW_RE.finditer(text):
        genes.append(row.group(1).strip())
    pathway["genes"] = genes

    # Analysis text
    analysis_match = re.search(r"## Pathway Analysis\s*\n(.+)", text, re.DOTALL)
    if not analysis_match:
        analysis_match = re.search(r"## .*Analysis\s*\n(.+)", text, re.DOTALL)
    if analysis_match:
        pathway["analysis_text"] = analysis_match.group(1).strip()[:5000]

    return pathway


def parse_theme_file(path: Path) -> Optional[dict]:
    """Parse a theme markdown file.

    Returns dict with keys: theme_id, title, tldr, last_updated,
    analysis_text, source_file.
    """
    text = _read_text(path)
    if not text:
        return None

    theme: dict = {
        "theme_id": path.stem,
        "source_file": str(path.relative_to(PROJECT_ROOT)),
    }

    m = _HEADER_RE.search(text)
    if m:
        theme["title"] = m.group(1).strip()

    meta = _extract_meta(text)
    theme.update(meta)

    # Full text as analysis
    theme["analysis_text"] = text[:5000]

    return theme


def parse_synthesis_claims(path: Path) -> list[dict]:
    """Extract claim-like assertions from a synthesis markdown file.

    Returns list of dicts with keys: claim_id, text, source_file, evidence_level.
    """
    text = _read_text(path)
    if not text:
        return []

    source_file = str(path.relative_to(PROJECT_ROOT))
    claims: list[dict] = []

    for i, m in enumerate(_CLAIM_RE.finditer(text)):
        claim_text = m.group(1).strip()
        # Skip very short or table-like matches
        if len(claim_text) < 40:
            continue

        claim_id = f"{path.stem}::claim_{i:03d}"

        # Try to infer evidence level from surrounding context
        evidence_level = "inferred"
        lower = claim_text.lower()
        if any(w in lower for w in ["known", "established", "demonstrated", "shown"]):
            evidence_level = "established"
        elif any(w in lower for w in ["speculative", "hypothe", "may", "might", "could"]):
            evidence_level = "speculative"

        claims.append({
            "claim_id": claim_id,
            "text": claim_text,
            "source_file": source_file,
            "evidence_level": evidence_level,
        })

    return claims


# ---------------------------------------------------------------------------
# Graph population functions
# ---------------------------------------------------------------------------


async def create_crop_node(client: Neo4jClient, species: str, treatment: str) -> dict:
    """Create or merge the Crop node for the organism under study."""
    common_names = {
        "Spinacia oleracea": "spinach",
    }
    common = common_names.get(species, species.split()[-1].lower())
    props = {
        "common_name": common,
        "treatment": treatment,
    }
    result = await client.merge_node("Crop", "species", species, props)
    logger.info("Crop node merged: %s (%s)", species, common)
    return result


async def create_gene_nodes(
    client: Neo4jClient, genes: list[dict], species: str
) -> int:
    """Create Gene nodes from parsed target data."""
    count = 0
    for gene in genes:
        gene_id = gene.get("gene_id")
        if not gene_id:
            continue

        props = {
            "annotation": gene.get("annotation", ""),
            "pathway": gene.get("pathway", ""),
            "priority": gene.get("priority", ""),
            "organism": species,
            "crop": species,
            "tldr": gene.get("tldr", "")[:500],
            "source_file": gene.get("source_file", ""),
            "last_updated": gene.get("last_updated", ""),
        }
        await client.merge_node("Gene", "gene_id", gene_id, props)

        # Relationship: Gene -[:STUDIED_IN_CROP]-> Crop
        await client.merge_relationship(
            "Gene", "gene_id", gene_id,
            "STUDIED_IN_CROP",
            "Crop", "species", species,
        )

        # Relationship: Gene -[:BELONGS_TO_PATHWAY]-> Pathway
        pathway_id = gene.get("pathway")
        if pathway_id:
            await client.merge_relationship(
                "Gene", "gene_id", gene_id,
                "BELONGS_TO_PATHWAY",
                "Pathway", "pathway_id", pathway_id,
            )

        # Ortholog relationships
        for orth in gene.get("orthologs", []):
            # Create a lightweight Gene node for the Arabidopsis ortholog
            orth_id = f"At_{orth}"
            await client.merge_node(
                "Gene", "gene_id", orth_id,
                {"annotation": orth, "organism": "Arabidopsis thaliana"},
            )
            await client.merge_relationship(
                "Gene", "gene_id", gene_id,
                "ORTHOLOG_OF",
                "Gene", "gene_id", orth_id,
                {"source": "literature_inference"},
            )

        count += 1

    logger.info("Created/merged %d Gene nodes", count)
    return count


async def create_pathway_nodes(
    client: Neo4jClient, pathways: list[dict]
) -> int:
    """Create Pathway nodes and link genes."""
    count = 0
    for pw in pathways:
        pathway_id = pw.get("pathway_id")
        if not pathway_id or pathway_id == "INDEX":
            continue

        props = {
            "title": pw.get("title", pathway_id),
            "tldr": pw.get("tldr", "")[:500],
            "gene_count": pw.get("gene_count", len(pw.get("genes", []))),
            "source_file": pw.get("source_file", ""),
            "last_updated": pw.get("last_updated", ""),
        }
        await client.merge_node("Pathway", "pathway_id", pathway_id, props)
        count += 1

    logger.info("Created/merged %d Pathway nodes", count)
    return count


async def create_theme_nodes(
    client: Neo4jClient, themes: list[dict]
) -> int:
    """Create Theme nodes and link genes and pathways to them."""
    count = 0
    for th in themes:
        theme_id = th.get("theme_id")
        if not theme_id or theme_id == "INDEX":
            continue

        props = {
            "title": th.get("title", theme_id),
            "tldr": th.get("tldr", "")[:500],
            "source_file": th.get("source_file", ""),
            "last_updated": th.get("last_updated", ""),
        }
        await client.merge_node("Theme", "theme_id", theme_id, props)
        count += 1

    logger.info("Created/merged %d Theme nodes", count)
    return count


async def link_genes_to_themes(
    client: Neo4jClient, genes: list[dict], themes: list[dict]
) -> int:
    """Create HAS_THEME relationships between genes and themes.

    Uses a mapping from pathway names to the most relevant theme.
    """
    # Build pathway -> theme mapping based on known associations
    pathway_theme_map = {
        "defense_immunity": "defense_downshift",
        "epigenetic_regulation": "epigenetic_remodeling",
        "ros_redox": "ros_optimization",
        "hormone_signaling": "hormone_nodes",
        "transport_ion_homeostasis": "transport_ion_homeostasis",
        "metabolic": "metabolic_priming",
        "metabolic_priming": "metabolic_priming",
    }

    theme_ids = {th["theme_id"] for th in themes if th.get("theme_id")}
    count = 0

    for gene in genes:
        gene_id = gene.get("gene_id")
        pathway = gene.get("pathway", "")
        mapped_theme = pathway_theme_map.get(pathway)

        if gene_id and mapped_theme and mapped_theme in theme_ids:
            await client.merge_relationship(
                "Gene", "gene_id", gene_id,
                "HAS_THEME",
                "Theme", "theme_id", mapped_theme,
            )
            count += 1

    logger.info("Created %d Gene-Theme relationships", count)
    return count


async def create_claim_nodes(
    client: Neo4jClient, claims: list[dict]
) -> int:
    """Create Claim nodes from synthesis file extractions."""
    count = 0
    for claim in claims:
        claim_id = claim.get("claim_id")
        if not claim_id:
            continue

        props = {
            "text": claim["text"][:1000],
            "source": claim.get("source_file", ""),
            "evidence_level": claim.get("evidence_level", "inferred"),
        }
        await client.merge_node("Claim", "claim_id", claim_id, props)
        count += 1

    logger.info("Created/merged %d Claim nodes", count)
    return count


# ---------------------------------------------------------------------------
# Supplementary: load genes from targets_config.json as fallback
# ---------------------------------------------------------------------------


def load_genes_from_config() -> list[dict]:
    """Load gene entries from targets_config.json as a supplementary source."""
    if not TARGETS_CONFIG.exists():
        logger.warning("targets_config.json not found at %s", TARGETS_CONFIG)
        return []

    try:
        data = json.loads(TARGETS_CONFIG.read_text(encoding="utf-8"))
    except Exception as exc:
        logger.error("Failed to parse targets_config.json: %s", exc)
        return []

    genes = []
    for entry in data.get("targets", []):
        genes.append({
            "gene_id": entry.get("gene_id", ""),
            "annotation": entry.get("annotation", ""),
            "pathway": entry.get("pathway", ""),
            "priority": entry.get("priority", "").lower(),
            "chromosome": entry.get("chromosome", ""),
            "source_file": "targets_config.json",
        })
    return genes


# ---------------------------------------------------------------------------
# Main migration orchestrator
# ---------------------------------------------------------------------------


async def main():
    """Run the full markdown-to-graph migration."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    logger.info("Starting markdown-to-graph migration")
    logger.info("Knowledge base: %s", KNOWLEDGE_BASE)

    client = Neo4jClient(uri=NEO4J_URI, user=NEO4J_USER, password=NEO4J_PASSWORD)
    await client.connect()

    try:
        # --- Parse all markdown sources ---

        # 1. Parse target files from all priority directories
        target_dirs = [KB_TARGETS_HIGH, KB_TARGETS_MEDIUM, KB_TARGETS_LOW]
        genes: list[dict] = []
        gene_ids_seen: set[str] = set()

        for tdir in target_dirs:
            if not tdir.exists():
                logger.warning("Target directory not found: %s", tdir)
                continue
            for md_file in sorted(tdir.glob("*.md")):
                if md_file.name == "INDEX.md":
                    continue
                gene = parse_target_file(md_file)
                if gene and gene.get("gene_id") and gene["gene_id"] not in gene_ids_seen:
                    genes.append(gene)
                    gene_ids_seen.add(gene["gene_id"])

        # Supplement with targets_config.json entries not found in markdown
        config_genes = load_genes_from_config()
        for cg in config_genes:
            if cg.get("gene_id") and cg["gene_id"] not in gene_ids_seen:
                genes.append(cg)
                gene_ids_seen.add(cg["gene_id"])

        logger.info("Parsed %d unique genes from markdown + config", len(genes))

        # 2. Parse pathway files
        pathways: list[dict] = []
        if KB_PATHWAYS.exists():
            for md_file in sorted(KB_PATHWAYS.glob("*.md")):
                if md_file.name == "INDEX.md":
                    continue
                pw = parse_pathway_file(md_file)
                if pw:
                    pathways.append(pw)
        logger.info("Parsed %d pathways", len(pathways))

        # 3. Parse theme files
        themes: list[dict] = []
        if KB_THEMES.exists():
            for md_file in sorted(KB_THEMES.glob("*.md")):
                if md_file.name == "INDEX.md":
                    continue
                th = parse_theme_file(md_file)
                if th:
                    themes.append(th)
        logger.info("Parsed %d themes", len(themes))

        # 4. Parse synthesis files for claims
        claims: list[dict] = []
        if KB_SYNTHESIS.exists():
            for md_file in sorted(KB_SYNTHESIS.glob("*.md")):
                file_claims = parse_synthesis_claims(md_file)
                claims.extend(file_claims)
        logger.info("Extracted %d claims from synthesis files", len(claims))

        # --- Create graph nodes and relationships ---

        # Crop node
        await create_crop_node(client, ORGANISM, TREATMENT)

        # Pathway nodes (create before genes so relationship targets exist)
        pw_count = await create_pathway_nodes(client, pathways)

        # Theme nodes
        th_count = await create_theme_nodes(client, themes)

        # Gene nodes (with STUDIED_IN_CROP and BELONGS_TO_PATHWAY rels)
        gene_count = await create_gene_nodes(client, genes, ORGANISM)

        # Gene -> Theme relationships
        gt_count = await link_genes_to_themes(client, genes, themes)

        # Claim nodes
        claim_count = await create_claim_nodes(client, claims)

        # --- Summary ---
        summary = {
            "genes": gene_count,
            "pathways": pw_count,
            "themes": th_count,
            "claims": claim_count,
            "gene_theme_rels": gt_count,
        }
        logger.info("Migration complete: %s", json.dumps(summary))
        return summary

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
