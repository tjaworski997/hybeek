from src.modules.db_sql.models.item_chunk_model import ItemChunkModel
from src.modules.db_sql.models.item_model import ItemModel
from src.modules.db_sql.postgresql.items_service import add


def add_test():
    chunks = [
        ItemChunkModel(
            no=1,
            content_normalized="content_normalized_1"
        ),
        ItemChunkModel(
            no=2,
            content_normalized="content_normalized_2"
        )
    ]

    item = ItemModel(
        type=1,
        title="title",
        content="content",
        content_normalized="content_normalized",
        data=None,
        chunks=chunks)

    add(item)


add_test()
