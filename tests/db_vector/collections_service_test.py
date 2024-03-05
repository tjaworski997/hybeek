from src.modules.db_vector.qdrant.collections_service import create_collection_if_not_exists, add_vectors_to_collection
from src.modules.embeddings.embeddings_service import get_embeddings

collection_name = "test"
text = "Szybki brązowy lis skacze nad leniwym psem."
vector = get_embeddings([text])[0]

create_collection_if_not_exists(collection_name)
add_vectors_to_collection(collection_name, vector, {"a": 1})
