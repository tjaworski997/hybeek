from src.api.modules.db_vector.qdrant.search_service import search as db_vector_search


def search(collection_name: str, dataset_id: str, search_expression: str, top: int):
    return db_vector_search(collection_name, dataset_id, search_expression, top)
