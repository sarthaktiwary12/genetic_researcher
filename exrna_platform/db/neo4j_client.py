"""Async Neo4j driver wrapper with connection pooling."""

import logging
from typing import Optional, Any

from neo4j import AsyncGraphDatabase, AsyncDriver

logger = logging.getLogger(__name__)


class Neo4jClient:
    """Async Neo4j client with connection pooling and query helpers."""

    def __init__(self, uri: str, user: str, password: str):
        self.uri = uri
        self.user = user
        self.password = password
        self._driver: Optional[AsyncDriver] = None

    async def connect(self):
        """Initialize the driver and verify connectivity."""
        self._driver = AsyncGraphDatabase.driver(
            self.uri, auth=(self.user, self.password)
        )
        await self._driver.verify_connectivity()
        logger.info(f"Connected to Neo4j at {self.uri}")

    async def close(self):
        """Close the driver."""
        if self._driver:
            await self._driver.close()
            self._driver = None
            logger.info("Neo4j connection closed")

    @property
    def driver(self) -> AsyncDriver:
        if not self._driver:
            raise RuntimeError("Neo4j client not connected. Call connect() first.")
        return self._driver

    async def run_query(
        self,
        query: str,
        parameters: Optional[dict[str, Any]] = None,
        database: str = "neo4j",
    ) -> list[dict]:
        """Execute a Cypher query and return results as list of dicts.

        Args:
            query: Cypher query string.
            parameters: Query parameters.
            database: Target database name.

        Returns:
            List of record dictionaries.
        """
        async with self.driver.session(database=database) as session:
            result = await session.run(query, parameters or {})
            records = await result.data()
            return records

    async def run_write(
        self,
        query: str,
        parameters: Optional[dict[str, Any]] = None,
        database: str = "neo4j",
    ) -> dict:
        """Execute a write transaction and return summary counters.

        Args:
            query: Cypher write query.
            parameters: Query parameters.
            database: Target database name.

        Returns:
            Summary counters dict.
        """
        async with self.driver.session(database=database) as session:
            result = await session.run(query, parameters or {})
            summary = await result.consume()
            counters = summary.counters
            return {
                "nodes_created": counters.nodes_created,
                "nodes_deleted": counters.nodes_deleted,
                "relationships_created": counters.relationships_created,
                "relationships_deleted": counters.relationships_deleted,
                "properties_set": counters.properties_set,
            }

    async def merge_node(
        self,
        label: str,
        key_property: str,
        key_value: Any,
        properties: Optional[dict] = None,
    ) -> dict:
        """MERGE a node by its unique key, setting additional properties.

        Args:
            label: Node label (e.g., 'Gene').
            key_property: Unique property name (e.g., 'gene_id').
            key_value: Value for the unique property.
            properties: Additional properties to set.

        Returns:
            Write summary counters.
        """
        props = properties or {}
        set_clause = ""
        if props:
            set_parts = [f"n.{k} = ${k}" for k in props]
            set_clause = "SET " + ", ".join(set_parts)

        query = f"""
        MERGE (n:{label} {{{key_property}: $key_value}})
        {set_clause}
        RETURN n
        """
        params = {"key_value": key_value, **props}
        return await self.run_write(query, params)

    async def merge_relationship(
        self,
        from_label: str,
        from_key: str,
        from_value: Any,
        rel_type: str,
        to_label: str,
        to_key: str,
        to_value: Any,
        properties: Optional[dict] = None,
    ) -> dict:
        """MERGE a relationship between two nodes.

        Args:
            from_label: Source node label.
            from_key: Source node key property.
            from_value: Source node key value.
            rel_type: Relationship type (e.g., 'BELONGS_TO').
            to_label: Target node label.
            to_key: Target node key property.
            to_value: Target node key value.
            properties: Relationship properties.

        Returns:
            Write summary counters.
        """
        props = properties or {}
        set_clause = ""
        if props:
            set_parts = [f"r.{k} = ${k}" for k in props]
            set_clause = "SET " + ", ".join(set_parts)

        query = f"""
        MATCH (a:{from_label} {{{from_key}: $from_value}})
        MATCH (b:{to_label} {{{to_key}: $to_value}})
        MERGE (a)-[r:{rel_type}]->(b)
        {set_clause}
        RETURN type(r) as rel_type
        """
        params = {"from_value": from_value, "to_value": to_value, **props}
        return await self.run_write(query, params)
