class ItemModel:
    application_id: str
    dataset_id: str
    entity_id: str
    content: str

    def __init__(self, application_id, dataset_id, entity_id, content):
        self.application_id = application_id
        self.dataset_id = dataset_id
        self.entity_id = entity_id
        self.content = content
