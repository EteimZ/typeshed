import abc
from abc import ABC, abstractmethod
from typing import Set, Union
from weaviate.connect import Connection as Connection
from weaviate.error_msgs import FILTER_BEACON_V14_CLS_NS_W as FILTER_BEACON_V14_CLS_NS_W
from weaviate.exceptions import UnexpectedStatusCodeException as UnexpectedStatusCodeException
from weaviate.util import get_vector as get_vector

VALUE_TYPES: Set[str]

class GraphQL(ABC, metaclass=abc.ABCMeta):
    def __init__(self, connection: Connection) -> None: ...
    @abstractmethod
    def build(self) -> str: ...
    def do(self) -> dict: ...

class Filter(ABC, metaclass=abc.ABCMeta):
    def __init__(self, content: dict) -> None: ...
    @property
    def content(self): ...

class NearText(Filter):
    def __init__(self, content: dict) -> None: ...

class NearVector(Filter):
    def __init__(self, content: dict) -> None: ...

class NearObject(Filter):
    obj_id: str
    def __init__(self, content: dict, is_server_version_14: bool) -> None: ...

class Ask(Filter):
    def __init__(self, content: dict) -> None: ...

class NearImage(Filter):
    def __init__(self, content: dict) -> None: ...

class Sort(Filter):
    def __init__(self, content: Union[dict, list]) -> None: ...
    def add(self, content: Union[dict, list]) -> None: ...

class Where(Filter):
    is_filter: bool
    def __init__(self, content: dict) -> None: ...
