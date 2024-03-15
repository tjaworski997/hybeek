from pydantic import BaseModel


class ItemModel:
    application_id: str
    dataset_id: str
    entity_id: str
    content: str
    data: object
    chunks: []

    def __init__(self, application_id, dataset_id, entity_id, content, data):
        self.application_id = application_id
        self.dataset_id = dataset_id
        self.entity_id = entity_id
        self.content = content
        self.data = data
        self.chunks = []
