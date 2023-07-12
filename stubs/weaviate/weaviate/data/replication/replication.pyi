from enum import Enum

class ConsistencyLevel(str, Enum):
    ALL: str
    ONE: str
    QUORUM: str
