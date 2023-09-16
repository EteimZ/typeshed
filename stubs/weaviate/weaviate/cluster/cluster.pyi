from typing import Optional
from weaviate.connect import Connection as Connection
from weaviate.exceptions import EmptyResponseException as EmptyResponseException

class Cluster:
    def __init__(self, connection: Connection) -> None: ...
    def get_nodes_status(self, class_name: Optional[str] = ...) -> list: ...
