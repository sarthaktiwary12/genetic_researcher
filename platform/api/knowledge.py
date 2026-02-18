"""Knowledge graph API routes.

Endpoints for querying genes, pathways, themes, and claims from the
Neo4j knowledge graph. Includes a raw Cypher endpoint for advanced users.
"""

import logging
from typing import Optional

from fastapi import APIRouter, Request, HTTPException, Query
from fastapi.responses import JSONResponse

from platform.dependencies import get_deps
from platform.models import (
    GeneResponse,
    PathwayResponse,
    CypherQuery,
    GraphQueryResponse,
)

logger = logging.getLogger(__name__)

router = APIRouter()


def _neo4j_unavailable() -> JSONResponse:
    """Standard 503 response when Neo4j is not connected."""
    return JSONResponse(
        status_code=503,
        content={"detail": "Knowledge graph service unavailable (Neo4j not connected)"},
    )


@router.get("/genes", response_model=list[GeneResponse])
async def list_genes(
    request: Request,
    pathway: Optional[str] = Query(None, description="Filter by pathway name"),
    priority: Optional[str] = Query(None, description="Filter by priority: high, medium, low"),
    crop: Optional[str] = Query(None, description="Filter by crop/organism"),
    limit: int = Query(50, le=500, description="Maximum results to return"),
):
    """List genes from the knowledge graph with optional filters."""
    deps = get_deps(request)
    if deps.neo4j is None:
        return _neo4j_unavailable()

    try:
        conditions = []
        params: dict = {"limit": limit}

        if pathway:
            conditions.append("(g)-[:BELONGS_TO]->(:Pathway {name: $pathway})")
            params["pathway"] = pathway
        if priority:
            conditions.append("g.priority = $priority")
            params["priority"] = priority
        if crop:
            conditions.append("g.organism = $crop")
            params["crop"] = crop

        where_clause = ""
        if conditions:
            where_clause = "WHERE " + " AND ".join(conditions)

        query = f"""
        MATCH (g:Gene)
        {where_clause}
        RETURN g.gene_id AS gene_id,
               g.annotation AS annotation,
               g.pathway AS pathway,
               g.priority AS priority,
               g.organism AS organism,
               g.tldr AS tldr
        ORDER BY g.priority, g.gene_id
        LIMIT $limit
        """

        records = await deps.neo4j.run_query(query, params)
        return [GeneResponse(**r) for r in records]
    except Exception as e:
        logger.error(f"Failed to list genes: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to query genes: {e}")


@router.get("/genes/{gene_id}", response_model=dict)
async def get_gene(request: Request, gene_id: str):
    """Get gene details including all relationships."""
    deps = get_deps(request)
    if deps.neo4j is None:
        return _neo4j_unavailable()

    try:
        # Get gene properties
        gene_query = """
        MATCH (g:Gene {gene_id: $gene_id})
        RETURN g
        """
        gene_records = await deps.neo4j.run_query(gene_query, {"gene_id": gene_id})
        if not gene_records:
            raise HTTPException(status_code=404, detail=f"Gene {gene_id} not found")

        gene_data = gene_records[0]["g"]

        # Get all relationships
        rel_query = """
        MATCH (g:Gene {gene_id: $gene_id})-[r]->(target)
        RETURN type(r) AS relationship, labels(target) AS target_labels, properties(target) AS target_props
        UNION
        MATCH (source)-[r]->(g:Gene {gene_id: $gene_id})
        RETURN type(r) AS relationship, labels(source) AS target_labels, properties(source) AS target_props
        """
        rel_records = await deps.neo4j.run_query(rel_query, {"gene_id": gene_id})

        return {
            "gene": gene_data,
            "relationships": rel_records,
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get gene {gene_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to query gene: {e}")


@router.get("/pathways", response_model=list[PathwayResponse])
async def list_pathways(request: Request):
    """List all pathways with gene counts."""
    deps = get_deps(request)
    if deps.neo4j is None:
        return _neo4j_unavailable()

    try:
        query = """
        MATCH (p:Pathway)
        OPTIONAL MATCH (g:Gene)-[:BELONGS_TO]->(p)
        RETURN p.pathway_id AS pathway_id,
               p.name AS name,
               count(g) AS gene_count,
               p.tldr AS tldr
        ORDER BY gene_count DESC
        """
        records = await deps.neo4j.run_query(query)
        return [PathwayResponse(**r) for r in records]
    except Exception as e:
        logger.error(f"Failed to list pathways: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to query pathways: {e}")


@router.get("/pathways/{pathway_id}", response_model=dict)
async def get_pathway(request: Request, pathway_id: str):
    """Get pathway details with associated genes."""
    deps = get_deps(request)
    if deps.neo4j is None:
        return _neo4j_unavailable()

    try:
        query = """
        MATCH (p:Pathway {pathway_id: $pathway_id})
        OPTIONAL MATCH (g:Gene)-[:BELONGS_TO]->(p)
        RETURN p.pathway_id AS pathway_id,
               p.name AS name,
               p.tldr AS tldr,
               collect({
                   gene_id: g.gene_id,
                   annotation: g.annotation,
                   priority: g.priority
               }) AS genes
        """
        records = await deps.neo4j.run_query(query, {"pathway_id": pathway_id})
        if not records:
            raise HTTPException(status_code=404, detail=f"Pathway {pathway_id} not found")

        result = records[0]
        # Filter out null gene entries from the collect
        result["genes"] = [g for g in result["genes"] if g.get("gene_id")]
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get pathway {pathway_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to query pathway: {e}")


@router.get("/themes", response_model=list[dict])
async def list_themes(request: Request):
    """List all cross-cutting themes."""
    deps = get_deps(request)
    if deps.neo4j is None:
        return _neo4j_unavailable()

    try:
        query = """
        MATCH (t:Theme)
        OPTIONAL MATCH (t)-[:RELATES_TO]->(g:Gene)
        RETURN t.theme_id AS theme_id,
               t.name AS name,
               t.description AS description,
               count(g) AS gene_count
        ORDER BY gene_count DESC
        """
        records = await deps.neo4j.run_query(query)
        return records
    except Exception as e:
        logger.error(f"Failed to list themes: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to query themes: {e}")


@router.get("/claims", response_model=list[dict])
async def list_claims(
    request: Request,
    evidence_level: Optional[str] = Query(None, description="Filter: known, inferred, speculative"),
    limit: int = Query(50, le=500),
):
    """List claims from the knowledge graph, optionally filtered by evidence level."""
    deps = get_deps(request)
    if deps.neo4j is None:
        return _neo4j_unavailable()

    try:
        conditions = []
        params: dict = {"limit": limit}

        if evidence_level:
            conditions.append("c.evidence_level = $evidence_level")
            params["evidence_level"] = evidence_level

        where_clause = ""
        if conditions:
            where_clause = "WHERE " + " AND ".join(conditions)

        query = f"""
        MATCH (c:Claim)
        {where_clause}
        RETURN c
        ORDER BY c.evidence_level, c.created_at DESC
        LIMIT $limit
        """
        records = await deps.neo4j.run_query(query, params)
        return [r["c"] for r in records]
    except Exception as e:
        logger.error(f"Failed to list claims: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to query claims: {e}")


@router.post("/cypher", response_model=GraphQueryResponse)
async def execute_cypher(request: Request, body: CypherQuery):
    """Execute a raw Cypher query against the knowledge graph.

    WARNING: This endpoint is for advanced users. Queries are executed
    as read-only transactions.
    """
    deps = get_deps(request)
    if deps.neo4j is None:
        return _neo4j_unavailable()

    try:
        records = await deps.neo4j.run_query(body.query, body.parameters)
        return GraphQueryResponse(records=records, count=len(records))
    except Exception as e:
        logger.error(f"Cypher query failed: {e}", exc_info=True)
        raise HTTPException(status_code=400, detail=f"Cypher query failed: {e}")
