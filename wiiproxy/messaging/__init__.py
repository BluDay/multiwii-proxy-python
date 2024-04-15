from .msp_commands import MspCommands

from .msp_message_direction import MspMessageDirection
from .msp_message_header    import MspMessageHeader
from .msp_message_payload   import MspMessagePayload

@staticmethod
def get_command_codes() -> tuple[int]:
    """Gets an immutable list of all command codes."""
    return (value for value in vars(MspCommands) if 'MSP' in value[:3])
