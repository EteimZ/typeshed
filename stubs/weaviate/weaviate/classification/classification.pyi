from .config_builder import ConfigBuilder as ConfigBuilder
from weaviate.connect import Connection as Connection
from weaviate.util import get_valid_uuid as get_valid_uuid

class Classification:
    def __init__(self, connection: Connection) -> None: ...
    def schedule(self) -> ConfigBuilder: ...
    def get(self, classification_uuid: str) -> dict: ...
    def is_complete(self, classification_uuid: str) -> bool: ...
    def is_failed(self, classification_uuid: str) -> bool: ...
    def is_running(self, classification_uuid: str) -> bool: ...
