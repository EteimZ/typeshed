from .get import GetBuilder as GetBuilder
from typing import List
from weaviate.connect import Connection as Connection
from weaviate.gql.filter import GraphQL as GraphQL

class MultiGetBuilder(GraphQL):
    get_builder: List[GetBuilder]
    def __init__(self, get_builder: List[GetBuilder], connection: Connection) -> None: ...
    def build(self) -> str: ...
