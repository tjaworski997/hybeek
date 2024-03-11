import json

from src.app import POSTGRESQL
from src.modules.db_sql.models.item_data_model import ItemDataModel
import psycopg2

conn = psycopg2.connect(
    database=POSTGRESQL.database,
    user=POSTGRESQL.user,
    password=POSTGRESQL.password,
    host=POSTGRESQL.host,
    port=POSTGRESQL.port,

)

cur = conn.cursor()


def add_or_update(item: ItemDataModel, with_commit=True):
    delete(item.application_id, item.dataset_id, item.entity_id, False)

    cur.execute(
        "INSERT INTO items (application_id, dataset_id, entity_id, content, content_normalized, data, processed)"
        "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        "RETURNING id",
        (
            item.application_id,
            item.dataset_id,
            item.entity_id,
            item.content,
            item.content_normalized,
            item.data,
            item.processed
        ))

    row_id = cur.fetchone()[0]

    if item.chunks not in [None, []]:
        for chunk in item.chunks:
            cur.execute("INSERT INTO items_chunks (item_id, no, content_normalized) "
                        "VALUES (%s, %s, %s)",
                        (
                            row_id,
                            chunk.no,
                            chunk.content_normalized
                        ))
    conn.commit()


def delete(application_id, dataset_id, entity_id, with_commit=True):
    print(application_id, dataset_id, entity_id)

    cur.execute("SELECT id from items where application_id = %s and dataset_id = %s and entity_id = %s",
                (application_id, dataset_id, entity_id))

    item = cur.fetchone()

    if item is None:
        return

    item_id = item[0]

    cur.execute("DELETE from items where id = %s",
                (item_id,))

    if with_commit:
        conn.commit()
