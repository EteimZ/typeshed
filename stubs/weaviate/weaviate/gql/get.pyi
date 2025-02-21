from typing import Dict, List, Optional, Tuple, Union
from weaviate import util as util
from weaviate.connect import Connection as Connection
from weaviate.data.replication import ConsistencyLevel as ConsistencyLevel
from weaviate.exceptions import AdditionalPropertiesException as AdditionalPropertiesException
from weaviate.gql.filter import Ask as Ask, Filter as Filter, GraphQL as GraphQL, MediaType as MediaType, NearAudio as NearAudio, NearDepth as NearDepth, NearIMU as NearIMU, NearImage as NearImage, NearObject as NearObject, NearText as NearText, NearThermal as NearThermal, NearVector as NearVector, NearVideo as NearVideo, Sort as Sort, Where as Where
from weaviate.types import UUID as UUID
from weaviate.util import BaseEnum as BaseEnum, file_encoder_b64 as file_encoder_b64, get_valid_uuid as get_valid_uuid, image_encoder_b64 as image_encoder_b64

class BM25:
    query: str
    properties: Optional[List[str]]
    def __init__(self, query, properties) -> None: ...

class HybridFusion(str, BaseEnum):
    RANKED: str
    RELATIVE_SCORE: str

class Hybrid:
    query: str
    alpha: Optional[float]
    vector: Optional[List[float]]
    properties: Optional[List[str]]
    fusion_type: Optional[HybridFusion]
    def __init__(self, query, alpha, vector, properties, fusion_type) -> None: ...

class GroupBy:
    path: List[str]
    groups: int
    objects_per_group: int
    def __init__(self, path, groups, objects_per_group) -> None: ...

class LinkTo:
    link_on: str
    linked_class: str
    properties: List[Union[str, 'LinkTo']]
    def __init__(self, link_on, linked_class, properties) -> None: ...
PROPERTIES = Union[List[Union[str, LinkTo]], str]

class AdditionalProperties:
    uuid: bool
    vector: bool
    creationTimeUnix: bool
    lastUpdateTimeUnix: bool
    distance: bool
    certainty: bool
    score: bool
    explainScore: bool
    def __init__(self, uuid, vector, creationTimeUnix, lastUpdateTimeUnix, distance, certainty, score, explainScore) -> None: ...

class GetBuilder(GraphQL):
    def __init__(self, class_name: str, properties: Optional[PROPERTIES], connection: Connection) -> None: ...
    def with_autocut(self, autocut: int) -> GetBuilder: ...
    def with_tenant(self, tenant: str) -> GetBuilder: ...
    def with_after(self, after_uuid: UUID) -> GetBuilder: ...
    def with_where(self, content: dict) -> GetBuilder: ...
    @property
    def name(self) -> str: ...
    def with_near_text(self, content: dict) -> GetBuilder: ...
    def with_near_vector(self, content: dict) -> GetBuilder: ...
    def with_near_object(self, content: dict) -> GetBuilder: ...
    def with_near_image(self, content: dict, encode: bool = ...) -> GetBuilder: ...
    def with_near_audio(self, content: dict, encode: bool = ...) -> GetBuilder: ...
    def with_near_video(self, content: dict, encode: bool = ...) -> GetBuilder: ...
    def with_near_depth(self, content: dict, encode: bool = ...) -> GetBuilder: ...
    def with_near_thermal(self, content: dict, encode: bool = ...) -> GetBuilder: ...
    def with_near_imu(self, content: dict, encode: bool = ...) -> GetBuilder: ...
    def with_limit(self, limit: int) -> GetBuilder: ...
    def with_offset(self, offset: int) -> GetBuilder: ...
    def with_ask(self, content: dict) -> GetBuilder: ...
    def with_additional(self, properties: Union[List, str, Dict[str, Union[List[str], str]], Tuple[dict, dict], AdditionalProperties]) -> GetBuilder: ...
    def with_sort(self, content: Union[list, dict]) -> GetBuilder: ...
    def with_bm25(self, query: str, properties: Optional[List[str]] = ...) -> GetBuilder: ...
    def with_hybrid(self, query: str, alpha: Optional[float] = ..., vector: Optional[List[float]] = ..., properties: Optional[List[str]] = ..., fusion_type: Optional[HybridFusion] = ...) -> GetBuilder: ...
    def with_group_by(self, properties: List[str], groups: int, objects_per_group: int) -> GetBuilder: ...
    def with_generate(self, single_prompt: Optional[str] = ..., grouped_task: Optional[str] = ..., grouped_properties: Optional[List[str]] = ...) -> GetBuilder: ...
    def with_alias(self, alias: str) -> GetBuilder: ...
    def with_consistency_level(self, consistency_level: ConsistencyLevel) -> GetBuilder: ...
    def build(self, wrap_get: bool = ...) -> str: ...
    def do(self) -> dict: ...
