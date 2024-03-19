# to run the server fast api: uvicorn src.api.main:app --reload

from typing import Union

from fastapi import FastAPI

from src.api.modules.api.models.ItemApiModel import ItemApiModel
from src.api.modules.models.item_model import ItemModel
from src.api.modules.services.items_service import add_or_update as service_add_or_update, delete as service_delete, \
    delete_application as service_delete_application
from src.api.modules.services.search_service import search as service_search

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


@app.get("/search")
def search(application_id: str, dataset_id: str, search_expression: str, top: int):
    return service_search(application_id, dataset_id, search_expression, top)


@app.delete("/items/")
def delete(application_id: str, dataset_id: str, entity_id: str):
    service_delete(application_id, dataset_id, entity_id)


@app.delete("/applications/")
def delete_application(application_id: str):
    service_delete_application(application_id)
