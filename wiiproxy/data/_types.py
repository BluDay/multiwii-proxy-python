from typing import Generic, NamedTuple, TypeVar

T = TypeVar('T')

class Coordinates(NamedTuple):
    """Represents 2D geographics coordinates with longitude and latitude values."""

    # -------------------------------------- ATTRIBUTES ----------------------------------------

    latitude: float
    """float: The latitude value of the coordinate."""

    longitude: float
    """float: The longitude value of the coordinate."""

class Pid(NamedTuple, Generic[T]):
    """Represents PID values."""

    # -------------------------------------- ATTRIBUTES ----------------------------------------

    proportional: T
    """T: The proportional (P) component of the PID controller."""

    integral: T
    """T: The integral (I) component of the PID controller."""

    derivative: T
    """T: The derivative (D) component of the PID controller."""

class Point2D(NamedTuple, Generic[T]):
    """Represents a 2D point."""

    # -------------------------------------- ATTRIBUTES ----------------------------------------

    x: T
    """T: The x-coordinate of the point."""

    y: T
    """T: The y-coordinate of the point."""

class Point3D(NamedTuple, Generic[T]):
    """Represents a 3D point."""

    # -------------------------------------- ATTRIBUTES ----------------------------------------

    x: T
    """T: The x-coordinate of the point."""

    y: T
    """T: The y-coordinate of the point."""

    z: T
    """T: The z-coordinate of the point."""
