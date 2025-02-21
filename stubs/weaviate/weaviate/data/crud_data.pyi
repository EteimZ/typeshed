import uuid as uuid_lib
from typing import Any, Dict, List, Optional, Sequence, Union
from weaviate.connect import Connection as Connection
from weaviate.data.references import Reference as Reference
from weaviate.data.replication import ConsistencyLevel as ConsistencyLevel
from weaviate.error_msgs import DATA_DEPRECATION_NEW_V14_CLS_NS_W as DATA_DEPRECATION_NEW_V14_CLS_NS_W, DATA_DEPRECATION_OLD_V14_CLS_NS_W as DATA_DEPRECATION_OLD_V14_CLS_NS_W
from weaviate.exceptions import ObjectAlreadyExistsException as ObjectAlreadyExistsException, UnexpectedStatusCodeException as UnexpectedStatusCodeException
from weaviate.types import UUID as UUID
from weaviate.util import get_valid_uuid as get_valid_uuid, get_vector as get_vector

class DataObject:
    reference: Reference
    def __init__(self, connection: Connection) -> None: ...
    def create(self, data_object: Union[dict, str], class_name: str, uuid: Union[str, uuid_lib.UUID, None] = ..., vector: Optional[Sequence] = ..., consistency_level: Optional[ConsistencyLevel] = ..., tenant: Optional[str] = ...) -> str: ...
    def update(self, data_object: Union[dict, str], class_name: str, uuid: Union[str, uuid_lib.UUID], vector: Optional[Sequence] = ..., consistency_level: Optional[ConsistencyLevel] = ..., tenant: Optional[str] = ...) -> None: ...
    def replace(self, data_object: Union[dict, str], class_name: str, uuid: Union[str, uuid_lib.UUID], vector: Optional[Sequence] = ..., consistency_level: Optional[ConsistencyLevel] = ..., tenant: Optional[str] = ...) -> None: ...
    def get_by_id(self, uuid: Union[str, uuid_lib.UUID], additional_properties: Optional[List[str]] = ..., with_vector: bool = ..., class_name: Optional[str] = ..., node_name: Optional[str] = ..., consistency_level: Optional[ConsistencyLevel] = ..., tenant: Optional[str] = ...) -> Optional[dict]: ...
    def get(self, uuid: Union[str, uuid_lib.UUID, None] = ..., additional_properties: Optional[List[str]] = ..., with_vector: bool = ..., class_name: Optional[str] = ..., node_name: Optional[str] = ..., consistency_level: Optional[ConsistencyLevel] = ..., limit: Optional[int] = ..., after: Optional[UUID] = ..., offset: Optional[int] = ..., sort: Optional[Dict[str, Union[str, bool, List[bool], List[str]]]] = ..., tenant: Optional[str] = ...) -> Optional[Dict[str, Any]]: ...
    def delete(self, uuid: Union[str, uuid_lib.UUID], class_name: Optional[str] = ..., consistency_level: Optional[ConsistencyLevel] = ..., tenant: Optional[str] = ...) -> None: ...
    def exists(self, uuid: Union[str, uuid_lib.UUID], class_name: Optional[str] = ..., consistency_level: Optional[ConsistencyLevel] = ..., tenant: Optional[str] = ...) -> bool: ...
    def validate(self, data_object: Union[dict, str], class_name: str, uuid: Union[str, uuid_lib.UUID, None] = ..., vector: Optional[Sequence] = ...) -> dict: ...
