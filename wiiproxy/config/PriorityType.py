from enum import IntEnum, unique

@unique
class PriorityType(IntEnum):
    """Represents the priority level of an enqueued command."""
    Inactive = 0
    Low      = 1
    Normal   = 2
    High     = 3
    Critical = 4
