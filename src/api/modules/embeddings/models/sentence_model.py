class SentenceModel:
    vector = []

    def __init__(self, idx, content, document_id, document_type, chunk_part: int):
        self.idx = idx
        self.content = content
        self.document_id = document_id
        self.document_type = document_type
        self.chunk_part = chunk_part
