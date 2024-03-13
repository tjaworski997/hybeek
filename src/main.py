# to run the server fast api: uvicorn src.main:app --reload

from typing import Union

from fastapi import FastAPI

from src.modules.api.models.ItemApiModel import ItemApiModel
from src.modules.models.item_model import ItemModel
from src.modules.services.items_service import add_or_update as service_add_or_update

app = FastAPI()


@app.get("/")
def read_root():
    return {"Info": "Hybeek API v0.1"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/")
def add_or_update(item: ItemApiModel):
    data = ItemModel(
        application_id=item.application_id,
        dataset_id=item.dataset_id,
        entity_id=item.entity_id,
        content=item.content,
        data=item.data
    )

    service_add_or_update(data)
