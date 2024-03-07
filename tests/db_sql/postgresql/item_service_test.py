import json

from src.modules.db_sql.models.item_chunk_data_model import ItemChunkDataModel
from src.modules.db_sql.models.item_data_model import ItemDataModel
from src.modules.db_sql.postgresql.items_service import add_or_update


def add_test():
    chunks = [
        ItemChunkDataModel(
            no=1,
            content_normalized="content_normalized_1"
        ),
        ItemChunkDataModel(
            no=2,
            content_normalized="content_normalized_2"
        )
    ]

    data = {"test": True, "name": "tomek.nowakowski"}
    data_json = json.dumps(data)

    item = ItemDataModel(
        application_id='appId',
        dataset_id="products",
        entity_id="a1203",
        content="content",
        content_normalized="content_normalized",
        data=data_json,
        chunks=chunks,
        processed=False)

    add_or_update(item)


add_test()
