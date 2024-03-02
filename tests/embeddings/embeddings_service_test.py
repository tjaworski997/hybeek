from src.modules.db_vector.qdrant.collections import create_collection_if_not_exists, add_vectors_to_collection
from src.modules.db_vector.qdrant.search import search
from src.modules.embeddings.models.sentence_model import SentenceModel
from src.modules.embeddings.embeddings_service import get_embeddings

collection_name = "test"
vector_size = 768

sentences = [
    SentenceModel(1, "Szybki brązowy lis skacze nad leniwym psem.", "1", "towary", 0),
    SentenceModel(2, "Pokolenie młodzieżowe nie pije alkoholu.", "2", "towary", 0),
    SentenceModel(3, "Oni wolą palić papierosy.", "2", "towary", 1),
    SentenceModel(5, "100 razy pisać kod w javie jest bez sensu.", "3", "towary", 0),
    SentenceModel(6, "Kraków to spore miasto, warto je zwiedzać? ilość zabytków nie jest duża.", "4", "towary", 0),
]

texts = [sentence.content for sentence in sentences]
vectors = get_embeddings(texts)

for idx, vector in enumerate(vectors):
    sentences[idx].vector = vector

create_collection_if_not_exists(collection_name, vector_size)

for sentence in sentences:
    payload = {
        "document_id": sentence.document_id,
        "document_type": sentence.document_type,
        "chunk_id": sentence.chunk_part,
        "content": sentence.content,
    }

    add_vectors_to_collection(collection_name, sentence.idx, sentence.vector, payload)

search_vector = get_embeddings(["nałóg"])[0]

res = search(collection_name, "towary", search_vector, 3)

for hit in res.groups:
    print(hit)
