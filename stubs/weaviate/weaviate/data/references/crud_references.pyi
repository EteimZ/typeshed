from typing import List, Optional, Union
from weaviate.connect import Connection as Connection
from weaviate.data.replication import ConsistencyLevel as ConsistencyLevel
from weaviate.error_msgs import REF_DEPRECATION_NEW_V14_CLS_NS_W as REF_DEPRECATION_NEW_V14_CLS_NS_W, REF_DEPRECATION_OLD_V14_FROM_CLS_NS_W as REF_DEPRECATION_OLD_V14_FROM_CLS_NS_W, REF_DEPRECATION_OLD_V14_TO_CLS_NS_W as REF_DEPRECATION_OLD_V14_TO_CLS_NS_W
from weaviate.exceptions import UnexpectedStatusCodeException as UnexpectedStatusCodeException
from weaviate.util import get_valid_uuid as get_valid_uuid

class Reference:
    def __init__(self, connection: Connection) -> None: ...
    def delete(self, from_uuid: str, from_property_name: str, to_uuid: str, from_class_name: Optional[str] = ..., to_class_name: Optional[str] = ..., consistency_level: Optional[ConsistencyLevel] = ..., tenant: Optional[str] = ...) -> None: ...
    def update(self, from_uuid: str, from_property_name: str, to_uuids: Union[List[str], str], from_class_name: Optional[str] = ..., to_class_names: Union[List[str], str, None] = ..., consistency_level: Optional[ConsistencyLevel] = ..., tenant: Optional[str] = ...) -> None: ...
    def add(self, from_uuid: str, from_property_name: str, to_uuid: str, from_class_name: Optional[str] = ..., to_class_name: Optional[str] = ..., consistency_level: Optional[ConsistencyLevel] = ..., tenant: Optional[str] = ...) -> None: ...
