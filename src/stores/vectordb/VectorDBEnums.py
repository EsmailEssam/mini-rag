from enum import Enum

class VectorDBEnums(Enum):
    QDRANT = "qdrant"

class DistanceMethodEnum(Enum):
    COSINE = "cosine"
    DOT = "dot"