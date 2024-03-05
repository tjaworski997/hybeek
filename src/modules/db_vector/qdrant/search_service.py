from qdrant_client import QdrantClient
from qdrant_client.models import Distance
from qdrant_client.http import models

from src.app import QDRANT

client = QdrantClient(host=QDRANT.host, port=QDRANT.port)


def search(collection_name: str, document_type: str, vector: [], top: int):
    query_filter = models.Filter(
        must=[
            models.FieldCondition(
                key="document_type",
                match=models.MatchValue(
                    value=document_type
                ),
            )
        ]
    )

    hits = client.search_groups(
        collection_name=collection_name,
        query_vector=vector,
        group_by="document_id",
        query_filter=query_filter,
        limit=top,
        group_size=1
    )
    return hits
