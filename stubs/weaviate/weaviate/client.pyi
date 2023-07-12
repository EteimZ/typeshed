from .auth import AuthCredentials as AuthCredentials
from .backup import Backup as Backup
from .batch import Batch as Batch
from .classification import Classification as Classification
from .cluster import Cluster as Cluster
from .config import Config as Config
from .connect.connection import Connection as Connection, TIMEOUT_TYPE_RETURN as TIMEOUT_TYPE_RETURN
from .contextionary import Contextionary as Contextionary
from .data import DataObject as DataObject
from .embedded import EmbeddedDB as EmbeddedDB, EmbeddedOptions as EmbeddedOptions
from .exceptions import UnexpectedStatusCodeException as UnexpectedStatusCodeException
from .gql import Query as Query
from .schema import Schema as Schema
from .types import NUMBERS as NUMBERS
from typing import Any, Dict, Optional, Tuple, Union

TIMEOUT_TYPE = Union[Tuple[NUMBERS, NUMBERS], NUMBERS]

class Client:
    classification: Classification
    schema: Schema
    contextionary: Contextionary
    batch: Batch
    data_object: DataObject
    query: Query
    backup: Backup
    cluster: Cluster
    def __init__(self, url: Optional[str] = ..., auth_client_secret: Optional[AuthCredentials] = ..., timeout_config: TIMEOUT_TYPE = ..., proxies: Union[dict, str, None] = ..., trust_env: bool = ..., additional_headers: Optional[dict] = ..., startup_period: Optional[int] = ..., embedded_options: Optional[EmbeddedOptions] = ..., additional_config: Optional[Config] = ...) -> None: ...
    def is_ready(self) -> bool: ...
    def is_live(self) -> bool: ...
    def get_meta(self) -> dict: ...
    def get_open_id_configuration(self) -> Optional[Dict[str, Any]]: ...
    @property
    def timeout_config(self) -> TIMEOUT_TYPE_RETURN: ...
    def __del__(self) -> None: ...
