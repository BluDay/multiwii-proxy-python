from enum import IntEnum, unique

@unique
class CommandPriority(IntEnum):
    """Represents the priority level for a MSP command."""
    Inactive = 0
    Low      = 1
    Normal   = 2
    High     = 3
    Critical = 4
