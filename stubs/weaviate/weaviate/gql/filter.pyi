import abc
from abc import ABC, abstractmethod
from enum import Enum
from typing import Union, Set, List
from weaviate.connect import Connection as Connection
from weaviate.error_msgs import FILTER_BEACON_V14_CLS_NS_W as FILTER_BEACON_V14_CLS_NS_W
from weaviate.util import get_vector as get_vector

VALUE_LIST_TYPES: Set[str]
VALUE_ARRAY_TYPES: Set[str]
VALUE_PRIMITIVE_TYPES: Set[str]
ALL_VALUE_TYPES: Set[str]
VALUE_TYPES: Set[str]
WHERE_OPERATORS: List[str]

class MediaType(Enum):
    IMAGE: str
    AUDIO: str
    VIDEO: str
    THERMAL: str
    DEPTH: str
    IMU: str

class GraphQL(ABC, metaclass=abc.ABCMeta):
    def __init__(self, connection: Connection) -> None: ...
    @abstractmethod
    def build(self) -> str: ...
    def do(self) -> dict: ...

class Filter(ABC, metaclass=abc.ABCMeta):
    def __init__(self, content: dict) -> None: ...
    @property
    def content(self) -> dict: ...

class NearText(Filter):
    def __init__(self, content: dict) -> None: ...

class NearVector(Filter):
    def __init__(self, content: dict) -> None: ...

class NearObject(Filter):
    obj_id: str
    def __init__(self, content: dict, is_server_version_14: bool) -> None: ...

class Ask(Filter):
    def __init__(self, content: dict) -> None: ...

class NearMedia(Filter):
    def __init__(self, content: dict, media_type: MediaType) -> None: ...

class NearImage(NearMedia):
    def __init__(self, content: dict) -> None: ...

class NearVideo(NearMedia):
    def __init__(self, content: dict) -> None: ...

class NearAudio(NearMedia):
    def __init__(self, content: dict) -> None: ...

class NearDepth(NearMedia):
    def __init__(self, content: dict) -> None: ...

class NearThermal(NearMedia):
    def __init__(self, content: dict) -> None: ...

class NearIMU(NearMedia):
    def __init__(self, content: dict) -> None: ...

class Sort(Filter):
    def __init__(self, content: Union[dict, list]) -> None: ...
    def add(self, content: Union[dict, list]) -> None: ...

class Where(Filter):
    is_filter: bool
    def __init__(self, content: dict) -> None: ...
