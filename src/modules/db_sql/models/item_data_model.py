from typing import List

from src.modules.db_sql.models.item_chunk_data_model import ItemChunkDataModel


class ItemDataModel:
    id: str
    type: int
    title: str
    content: str
    content_normalized: str
    data: {}
    chunks: list[ItemChunkDataModel]

    def __init__(self, type, title, content, content_normalized, data: None, chunks=None):
        self.type = type
        self.title = title
        self.content = content
        self.content_normalized = content_normalized
        self.data = data
        self.chunks = chunks
