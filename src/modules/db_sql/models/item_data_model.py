from typing import List

from src.modules.db_sql.models.item_chunk_data_model import ItemChunkDataModel


class ItemDataModel:
    application_id: str
    dataset_id: str
    entity_id: str
    content: str
    content_normalized: str
    data: object
    chunks: list[ItemChunkDataModel]
    processed: bool

    def __init__(self, application_id, dataset_id, entity_id, content, content_normalized, data: object, chunks=None,
                 processed=False):
        self.application_id = application_id
        self.dataset_id = dataset_id
        self.entity_id = entity_id
        self.content = content
        self.content_normalized = content_normalized
        self.data = data
        self.chunks = chunks
        self.processed = processed
