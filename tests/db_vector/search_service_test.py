from src.modules.db_vector.qdrant.search_service import search

result = search("whisli", "kb", "miasto kraków", 3)

for x in result:
    print(x)
