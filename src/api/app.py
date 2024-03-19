class App:
    __conf = {
        ""
    }


class QDRANT:
    host: str = "localhost"
    port: int = 6333
    vector_size: int = 768


class POSTGRESQL:
    host = "localhost"
    port = 5432
    user = "postgres"
    password = "postgres"
    database = "hybeek"
