from pydantic import BaseModel


class ItemApiModel(BaseModel):
    application_id: str
    dataset_id: str
    entity_id: str
    content: str
    data: str | None = None
