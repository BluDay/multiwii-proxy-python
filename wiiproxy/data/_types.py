from typing import Generic, NamedTuple, TypeVar

T = TypeVar('T')

class Coord2D(NamedTuple):
    """Represents 2D geographics coordinates with longitude and latitude values.

    Attributes
    ----------
    latitude : float
        The latitude value of the coordinate.
    longitude : float
        The longitude value of the coordinate.
    """
    latitude: float

    longitude: float

class PidValues(NamedTuple, Generic[T]):
    """Represents PID values.
    
    Attributes
    ----------
    proportional : T
        The proportional (P) component of the PID controller.
    integral : T
        The integral (I) component of the PID controller.
    derivative : T 
        The derivative (D) component of the PID controller.
    """
    proportional: T

    integral: T

    derivative: T

class Point2D(NamedTuple, Generic[T]):
    """Represents a 2D point.

    Attributes
    ----------
    x : T
        The x-coordinate of the point.
    y : T
        The y-coordinate of the point.
    """
    x: T
    y: T

class Point3D(NamedTuple, Generic[T]):
    """Represents a 3D point.
    
    Attributes
    ----------
    x : T
        The x-coordinate of the point.
    y : T
        The y-coordinate of the point.
    z : T
        The z-coordinate of the point.
    """
    x: T
    y: T
    z: T
