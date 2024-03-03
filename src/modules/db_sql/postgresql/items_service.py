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


def add(item: ItemDataModel):
    cur.execute("INSERT INTO items (type, title, content, content_normalized, data) "
                "VALUES (%s, %s, %s, %s, %s) "
                "RETURNING id",
                (
                    item.type,
                    item.title,
                    item.content,
                    item.content_normalized,
                    item.data
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
