from src.modules.content.content_cleaner_service import clean_content
from src.modules.content.sentences_service import get_sentences_from_content
from src.modules.db_sql.models.item_chunk_data_model import ItemChunkDataModel
from src.modules.db_sql.models.item_data_model import ItemDataModel
from src.modules.db_vector.qdrant.collections_service import add as db_vector_add, \
    add_or_update as db_vector_add_or_update
from src.modules.models.item_model import ItemModel
from src.modules.db_sql.postgresql.items_service import add_or_update as db_sql_add
from src.modules.db_sql.postgresql.items_service import delete as db_sql_delete

max_chunk_size = 512


def add_or_update(item: ItemModel):
    sentences = get_sentences_from_content(item.content)
    for idx, sentence in enumerate(sentences):
        clean_sentence = clean_content(sentence)
        item.chunks.append(clean_sentence)

    # sql

    item_chunks_data = []
    for idx, chunk in enumerate(item.chunks):
        item_chunk_data = ItemChunkDataModel(
            no=idx,
            content_normalized=chunk
        )
        item_chunks_data.append(item_chunk_data)

    item_data = ItemDataModel(
        application_id=item.application_id,
        dataset_id=item.dataset_id,
        entity_id=item.entity_id,
        content=item.content,
        content_normalized=clean_content(item.content),
        data=item.data,
        chunks=item_chunks_data,
        processed=False
    )

    db_sql_add(item_data)

    # vector

    db_vector_add_or_update(item)


def delete(application_id, dataset_id, entity_id):
    db_sql_delete(application_id, dataset_id, entity_id)
