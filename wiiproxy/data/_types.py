from typing      import Generic, NamedTuple, TypeVar

T = TypeVar('T')

class Coord2D(NamedTuple):
    """Represents 2D coordinates with longitude and latitude values."""
    latitude:  float
    longitude: float

class PidValues(NamedTuple, Generic[T]):
    """Represents PID values."""
    p: T
    i: T
    d: T

class Point2D(NamedTuple, Generic[T]):
    """Represents a 2D point."""
    x: T
    y: T

class Point3D(NamedTuple, Generic[T]):
    """Represents a 3D point."""
    x: T
    y: T
    z: T
