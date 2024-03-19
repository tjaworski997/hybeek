from src.api.modules.services.search_service import search

res = search("whisli", "kb", "kraków ludność", 3)

for hit in res:
    print(hit.entity_id, hit.score)
