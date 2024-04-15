from dataclasses import dataclass
from typing      import Generic, NamedTuple, TypeVar

T = TypeVar('T')

@dataclass
class Point2D(NamedTuple, Generic[T]):
    """A tuple of x and y integer values for a 2D point."""
    x: T
    y: T

@dataclass
class Point3D(NamedTuple, Generic[T]):
    """A tuple of x, y and z integer values for a 3D point."""
    x: T
    y: T
    z: T
