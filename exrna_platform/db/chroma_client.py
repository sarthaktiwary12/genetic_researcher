"""ChromaDB wrapper with three domain-specific collections.

Collections:
    gene_narratives   — Gene analysis narratives (per-target)
    research_findings — Pathway, theme, and synthesis documents
    literature        — PubMed abstracts and literature scan results

Uses all-MiniLM-L6-v2 (384-dim) via sentence-transformers for embeddings.
"""

import logging
from typing import Optional
from pathlib import Path

import chromadb
from chromadb.config import Settings as ChromaSettings

logger = logging.getLogger(__name__)

COLLECTION_NAMES = ["gene_narratives", "research_findings", "literature"]


class ChromaClient:
    """ChromaDB client with domain-specific collections."""

    def __init__(self, persist_dir: str = "./data/chromadb"):
        self.persist_dir = persist_dir
        Path(persist_dir).mkdir(parents=True, exist_ok=True)
        self.client = chromadb.PersistentClient(
            path=persist_dir,
            settings=ChromaSettings(anonymized_telemetry=False),
        )
        self._collections: dict = {}
        logger.info(f"ChromaDB initialized at {persist_dir}")

    def _get_collection(self, name: str):
        """Get or create a collection with the default embedding function."""
        if name not in self._collections:
            self._collections[name] = self.client.get_or_create_collection(
                name=name,
                metadata={"hnsw:space": "cosine"},
            )
        return self._collections[name]

    @property
    def gene_narratives(self):
        return self._get_collection("gene_narratives")

    @property
    def research_findings(self):
        return self._get_collection("research_findings")

    @property
    def literature(self):
        return self._get_collection("literature")

    def add_document(
        self,
        collection_name: str,
        doc_id: str,
        text: str,
        metadata: Optional[dict] = None,
    ):
        """Add or update a document in a collection.

        Args:
            collection_name: One of gene_narratives, research_findings, literature.
            doc_id: Unique document identifier.
            text: Document text to embed.
            metadata: Optional metadata dict (filterable).
        """
        collection = self._get_collection(collection_name)
        collection.upsert(
            ids=[doc_id],
            documents=[text],
            metadatas=[metadata or {}],
        )
        logger.debug(f"Upserted doc '{doc_id}' into {collection_name}")

    def add_documents_batch(
        self,
        collection_name: str,
        doc_ids: list[str],
        texts: list[str],
        metadatas: Optional[list[dict]] = None,
    ):
        """Batch add/update documents.

        Args:
            collection_name: Target collection.
            doc_ids: List of unique IDs.
            texts: List of document texts.
            metadatas: Optional list of metadata dicts.
        """
        collection = self._get_collection(collection_name)
        collection.upsert(
            ids=doc_ids,
            documents=texts,
            metadatas=metadatas or [{}] * len(doc_ids),
        )
        logger.info(f"Batch upserted {len(doc_ids)} docs into {collection_name}")

    def search(
        self,
        collection_name: str,
        query: str,
        n_results: int = 10,
        where: Optional[dict] = None,
    ) -> list[dict]:
        """Semantic search across a collection.

        Args:
            collection_name: Collection to search.
            query: Natural language query.
            n_results: Max results to return.
            where: Optional metadata filter.

        Returns:
            List of dicts with id, text, metadata, distance.
        """
        collection = self._get_collection(collection_name)
        kwargs = {"query_texts": [query], "n_results": n_results}
        if where:
            kwargs["where"] = where

        results = collection.query(**kwargs)

        docs = []
        for i in range(len(results["ids"][0])):
            docs.append({
                "id": results["ids"][0][i],
                "text": results["documents"][0][i] if results["documents"] else "",
                "metadata": results["metadatas"][0][i] if results["metadatas"] else {},
                "distance": results["distances"][0][i] if results["distances"] else None,
            })
        return docs

    def get_collection_stats(self) -> dict:
        """Return document counts for all collections."""
        stats = {}
        for name in COLLECTION_NAMES:
            try:
                collection = self._get_collection(name)
                stats[name] = collection.count()
            except Exception:
                stats[name] = 0
        return stats

    def delete_document(self, collection_name: str, doc_id: str):
        """Delete a document by ID."""
        collection = self._get_collection(collection_name)
        collection.delete(ids=[doc_id])
