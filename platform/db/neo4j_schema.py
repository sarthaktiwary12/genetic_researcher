"""Neo4j schema creation: node types, relationship types, constraints, indexes.

Node Types (9):
    Gene, Pathway, Theme, Crop, Phenotype, Paper, Claim, Campaign, Experiment

Relationship Types (10):
    BELONGS_TO_PATHWAY, HAS_THEME, STUDIED_IN_CROP, AFFECTS_PHENOTYPE,
    CITED_IN_PAPER, SUPPORTED_BY_CLAIM, ORTHOLOG_OF, INTERACTS_WITH,
    PRODUCED_BY_CAMPAIGN, TESTED_IN_EXPERIMENT
"""

import logging
from platform.db.neo4j_client import Neo4jClient

logger = logging.getLogger(__name__)

# Unique constraints
CONSTRAINTS = [
    ("Gene", "gene_id"),
    ("Pathway", "pathway_id"),
    ("Theme", "theme_id"),
    ("Crop", "species"),
    ("Phenotype", "phenotype_id"),
    ("Paper", "doi"),
    ("Claim", "claim_id"),
    ("Campaign", "campaign_id"),
    ("Experiment", "experiment_id"),
]

# Composite indexes for frequent queries
INDEXES = [
    ("Gene", ["gene_id", "crop"]),
    ("Gene", ["priority"]),
    ("Gene", ["pathway"]),
    ("Claim", ["evidence_level"]),
    ("Paper", ["year"]),
    ("Campaign", ["status"]),
]


async def create_schema(client: Neo4jClient) -> dict:
    """Create all constraints and indexes in Neo4j.

    Args:
        client: Connected Neo4j client.

    Returns:
        Summary of created constraints and indexes.
    """
    created = {"constraints": 0, "indexes": 0, "errors": []}

    # Create uniqueness constraints
    for label, prop in CONSTRAINTS:
        constraint_name = f"unique_{label.lower()}_{prop}"
        query = f"""
        CREATE CONSTRAINT {constraint_name} IF NOT EXISTS
        FOR (n:{label}) REQUIRE n.{prop} IS UNIQUE
        """
        try:
            await client.run_write(query)
            created["constraints"] += 1
            logger.info(f"Created constraint: {constraint_name}")
        except Exception as e:
            created["errors"].append(f"{constraint_name}: {e}")
            logger.warning(f"Constraint {constraint_name} error: {e}")

    # Create indexes
    for label, props in INDEXES:
        index_name = f"idx_{label.lower()}_{'_'.join(props)}"
        prop_list = ", ".join(f"n.{p}" for p in props)
        query = f"""
        CREATE INDEX {index_name} IF NOT EXISTS
        FOR (n:{label}) ON ({prop_list})
        """
        try:
            await client.run_write(query)
            created["indexes"] += 1
            logger.info(f"Created index: {index_name}")
        except Exception as e:
            created["errors"].append(f"{index_name}: {e}")
            logger.warning(f"Index {index_name} error: {e}")

    # Full-text index for gene search
    try:
        await client.run_write("""
        CREATE FULLTEXT INDEX gene_fulltext IF NOT EXISTS
        FOR (n:Gene) ON EACH [n.gene_id, n.annotation, n.organism]
        """)
        created["indexes"] += 1
        logger.info("Created full-text index: gene_fulltext")
    except Exception as e:
        created["errors"].append(f"gene_fulltext: {e}")

    # Full-text index for claims
    try:
        await client.run_write("""
        CREATE FULLTEXT INDEX claim_fulltext IF NOT EXISTS
        FOR (n:Claim) ON EACH [n.text, n.source]
        """)
        created["indexes"] += 1
        logger.info("Created full-text index: claim_fulltext")
    except Exception as e:
        created["errors"].append(f"claim_fulltext: {e}")

    logger.info(
        f"Schema creation complete: {created['constraints']} constraints, "
        f"{created['indexes']} indexes, {len(created['errors'])} errors"
    )
    return created


async def drop_schema(client: Neo4jClient) -> dict:
    """Drop all custom constraints and indexes. Use with caution."""
    dropped = {"constraints": 0, "indexes": 0}

    for label, prop in CONSTRAINTS:
        constraint_name = f"unique_{label.lower()}_{prop}"
        try:
            await client.run_write(f"DROP CONSTRAINT {constraint_name} IF EXISTS")
            dropped["constraints"] += 1
        except Exception:
            pass

    for label, props in INDEXES:
        index_name = f"idx_{label.lower()}_{'_'.join(props)}"
        try:
            await client.run_write(f"DROP INDEX {index_name} IF EXISTS")
            dropped["indexes"] += 1
        except Exception:
            pass

    for ft_index in ["gene_fulltext", "claim_fulltext"]:
        try:
            await client.run_write(f"DROP INDEX {ft_index} IF EXISTS")
            dropped["indexes"] += 1
        except Exception:
            pass

    return dropped
