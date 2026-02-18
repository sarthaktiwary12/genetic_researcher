"""Semantic search API routes.

Endpoints for searching across ChromaDB collections using
natural language queries with optional metadata filters.
"""

import logging

from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse

from platform.dependencies import get_deps
from platform.models import SearchRequest, SearchResult, SearchResponse

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/", response_model=SearchResponse)
async def semantic_search(request: Request, body: SearchRequest):
    """Perform semantic search across a ChromaDB collection.

    Available collections: gene_narratives, research_findings, literature.
    """
    deps = get_deps(request)
    if deps.chroma is None:
        return JSONResponse(
            status_code=503,
            content={"detail": "Search service unavailable (ChromaDB not initialized)"},
        )

    try:
        results = deps.chroma.search(
            collection_name=body.collection,
            query=body.query,
            n_results=body.n_results,
            where=body.filters,
        )

        search_results = [
            SearchResult(
                id=r["id"],
                text=r["text"],
                metadata=r.get("metadata", {}),
                distance=r.get("distance"),
            )
            for r in results
        ]

        return SearchResponse(
            results=search_results,
            total=len(search_results),
            collection=body.collection,
        )
    except Exception as e:
        logger.error(f"Search failed: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Search failed: {e}")


@router.get("/collections", response_model=dict)
async def list_collections(request: Request):
    """List available ChromaDB collections with document counts."""
    deps = get_deps(request)
    if deps.chroma is None:
        return JSONResponse(
            status_code=503,
            content={"detail": "Search service unavailable (ChromaDB not initialized)"},
        )

    try:
        stats = deps.chroma.get_collection_stats()
        return {
            "collections": [
                {"name": name, "document_count": count}
                for name, count in stats.items()
            ],
            "total_documents": sum(stats.values()),
        }
    except Exception as e:
        logger.error(f"Failed to list collections: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to list collections: {e}")
