from weaviate.connect import Connection as Connection
from weaviate.exceptions import UnexpectedStatusCodeException as UnexpectedStatusCodeException

class Property:
    def __init__(self, connection: Connection) -> None: ...
    def create(self, schema_class_name: str, schema_property: dict) -> None: ...
