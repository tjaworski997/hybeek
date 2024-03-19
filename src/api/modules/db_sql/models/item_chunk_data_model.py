class ItemChunkDataModel:
    id: str
    item_id: int
    no: int
    content_normalized: str

    def __init__(self, no, content_normalized):
        self.no = no
        self.content_normalized = content_normalized
