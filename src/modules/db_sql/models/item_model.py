from typing import List

from src.modules.db_sql.models.item_chunk_model import ItemChunkModel


class ItemModel:
    id: str
    type: int
    title: str
    content: str
    content_normalized: str
    data: {}
    chunks: list[ItemChunkModel]

    def __init__(self, type, title, content, content_normalized, data: None, chunks=None):
        self.type = type
        self.title = title
        self.content = content
        self.content_normalized = content_normalized
        self.data = data
        self.chunks = chunks
