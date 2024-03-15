from qdrant_client import QdrantClient
from qdrant_client.models import Distance
from qdrant_client.http import models

from src.app import QDRANT
from src.modules.embeddings.embeddings_service import get_embeddings
from src.modules.models.search_result_model import SearchResultModel

client = QdrantClient(host=QDRANT.host, port=QDRANT.port)


def search(collection_name: str, dataset_id: str, search_expression: str, top: int):
    vector = get_embeddings([search_expression])[0]

    print(collection_name)
    print(dataset_id)
    print(vector)

    query_filter = models.Filter(
        must=[
            models.FieldCondition(
                key="dataset_id",
                match=models.MatchValue(
                    value=dataset_id
                ),
            )
        ]
    )

    hits = client.search_groups(
        collection_name=collection_name,
        query_vector=vector,
        group_by="entity_id",
        query_filter=query_filter,
        limit=top,
        group_size=1
    )

    result = []

    for hit in hits.groups:
        result.append(
            SearchResultModel(hit.hits[0].payload["entity_id"], hit.hits[0].score, hit.hits[0].payload["data"]))

    return result
