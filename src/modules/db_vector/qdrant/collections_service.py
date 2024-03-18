from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct, models
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


def get_by_filter(collection_name: str, dataset_id: str, entity_id: str):
    res = client.scroll(
        collection_name=collection_name,
        scroll_filter=models.Filter(
            must=[
                models.FieldCondition(
                    key="dataset_id",
                    match=models.MatchValue(value=dataset_id),
                ),
                models.FieldCondition(
                    key="entity_id",
                    match=models.MatchValue(value=entity_id),
                ),
            ]
        ),
    )

    ids = []
    for x in res[0]:
        ids.append(x.id)

    return ids


def add_or_update(item: ItemModel):
    create_collection_if_not_exists(item.application_id)
    to_delete_ids = get_by_filter(item.application_id, item.dataset_id, item.entity_id)

    vectors = get_embeddings(item.chunks)

    points = []

    for idx, vector in enumerate(vectors):
        payload = {
            "dataset_id": item.dataset_id,
            "entity_id": item.entity_id,
            "data": json.dumps(item.data)
        }

        idx = uuid.uuid4()
        points.append(
            PointStruct(
                id=str(idx),
                vector=vector,
                payload=payload
            ))

    update_operations = []

    if len(to_delete_ids) > 0:
        update_operations.append(models.DeleteOperation(
            delete=models.PointIdsList(points=to_delete_ids)
        ))

    update_operations.append(models.UpsertOperation(
        upsert=models.PointsList(
            points=points
        )
    ))

    client.batch_update_points(
        collection_name=item.application_id,
        update_operations=update_operations)


def delete(application_id, dataset_id, entity_id):
    to_delete_ids = get_by_filter(application_id, dataset_id, entity_id)
    if len(to_delete_ids) > 0:
        client.delete(
            collection_name=application_id,
            points_selector=models.PointIdsList(
                points=to_delete_ids
            ),
        )


def delete_collection(application_id: str):
    client.delete_collection(application_id)
