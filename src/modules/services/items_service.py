from src.modules.content.content_cleaner_service import clean_content
from src.modules.content.sentences_service import get_sentences_from_content
from src.modules.db_sql.models.item_chunk_data_model import ItemChunkDataModel
from src.modules.db_sql.models.item_data_model import ItemDataModel
from src.modules.db_vector.qdrant.collections import \
    create_collection_if_not_exists as db_vector_create_collection_if_not_exists, \
    add_vectors_to_collection as db_vector_add_vectors_to_collection
from src.modules.services.models.item_model import ItemModel
from src.modules.db_sql.postgresql.items_service import add as db_sql_add

max_chunk_size = 512


def add(item: ItemModel):
    # sql

    chunks = []

    if len(item.content) <= max_chunk_size:
        chunks.append(ItemChunkDataModel(0, item.content))
    else:
        sentences = get_sentences_from_content(item.content)
        for idx, sentence in enumerate(sentences):
            clean_sentence = clean_content(sentence)
            chunks.append(ItemChunkDataModel(idx, clean_sentence))

    item_data = ItemDataModel(
        application_id=item.application_id,
        dataset_id=item.dataset_id,
        entity_id=item.entity_id,
        content=item.content,
        content_normalized=clean_content(item.content),
        data=item.data,
        chunks=chunks,
        processed=False
    )

    db_sql_add(item_data)

    # vector

    db_vector_create_collection_if_not_exists(item.application_id)

    db_vector_add_vectors_to_collection()
