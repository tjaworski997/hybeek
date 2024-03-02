from src.modules.embeddings.embeddings_service import get_embeddings

print("test 1")

vectors = get_embeddings(["mój pies ma na imię michał", "dwa lub trzy", "słońce świeci w niedzielę"])

print(vectors)
