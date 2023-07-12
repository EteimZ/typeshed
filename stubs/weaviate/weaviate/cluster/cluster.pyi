from weaviate.connect import Connection as Connection
from weaviate.exceptions import EmptyResponseException as EmptyResponseException, UnexpectedStatusCodeException as UnexpectedStatusCodeException

class Cluster:
    def __init__(self, connection: Connection) -> None: ...
    def get_nodes_status(self) -> list: ...
