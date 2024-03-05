from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct
from qdrant_client.models import Distance, VectorParams

import json
import uuid

from src.app import QDRANT
from src.modules.embeddings.embeddings_service import get_embeddings
from src.modules.models.item_model import ItemModel

client = QdrantClient(host=QDRANT.host, port=QDRANT.port)


def create_collection_if_not_exists(collection_name: str):
    collections_res = client.get_collections()
    collection_names = [collection.name for collection in collections_res.collections]
    if collection_name not in collection_names:
        print("Creating collection with name:", collection_name, "and vector size:", QDRANT.vector_size)
        client.recreate_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=QDRANT.vector_size, distance=Distance.COSINE),
        )


def add_vectors_to_collection(collection_name: str, vector: [], payload: dict):
    idx = uuid.uuid4()
    client.upsert(
        collection_name=collection_name,
        points=[
            PointStruct(
                id=str(idx),
                vector=vector,
                payload=payload
            )
        ]
    )


def add(item: ItemModel):
    create_collection_if_not_exists(item.application_id)

    vectors = get_embeddings(item.chunks)

    for idx, vector in enumerate(vectors):
        payload = {
            "dataset_id": item.dataset_id,
            "entity_id": item.entity_id
        }
        add_vectors_to_collection(item.application_id, vector, payload)
