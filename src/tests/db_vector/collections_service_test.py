from src.api.modules.db_vector.qdrant.collections_service import get_by_filter

# collection_name = "test"
# text = "Szybki brązowy lis skacze nad leniwym psem."
# vector = get_embeddings([text])[0]
#
# create_collection_if_not_exists(collection_name)
# add_vectors_to_collection(collection_name, vector, {"a": 1})


res = get_by_filter("whisli", "kb", "a1203")

ids = []

for x in res[0]:
    ids.append(x.id)

print(ids)
