from .command import Command

from typing import Final, NamedTuple
from struct import pack

# --------------------------------------- CONSTANTS ----------------------------------------

MESSAGE_ERROR_HEADER:    Final[bytes] = b'$M!' # 0x24, 0x4d, 0x21

MESSAGE_INCOMING_HEADER: Final[bytes] = b'$M<' # 0x24, 0x4d, 0x3c

MESSAGE_OUTGOING_HEADER: Final[bytes] = b'$M>' # 0x24, 0x4d, 0x3e

# ---------------------------------------- CLASSES -----------------------------------------

class _MspParsedMessageData(NamedTuple):
    """Represents a tuple with the data size and values for a received MSP message.

    Attributes
    ----------
    command : Command
        The targeted MSP command.
    size : int
        The size of the received data.
    values : tuple[int]
        A tuple of parsed data values.
    """
    command: Command

    size: int

    values: tuple[int]

class MspMessageError(Exception):
    """Represents a specific errors related to MSP messages."""
    pass

# --------------------------------------- FUNCTIONS ----------------------------------------

def crc8_xor(payload: bytes) -> int:
    """Calculates the checksum for the payload using an XOR CRC.

    Parameters
    ----------
    payload : bytes
        Bytes of the full payload (including the command code and size).

    Returns
    -------
    int
        The checksum for the provided payload.
    """
    checksum = 0

    for byte in payload: checksum ^= byte

    return checksum & 0xff

def create_request_message(command: Command, data: tuple[int]) -> bytes:
    """Constructs a serializes message and returns it.

    Attributes
    ----------
    command : Command
        An instance of Command representing the MSP command used to create the message.
    data : tuple[int]
        The data values to serialize and include in the payload.

    Returns
    -------
    bytes
        The full message in bytes.
    """
    code = command.code
    size = 0

    payload_content = b''

    if data:
        if command.has_variable_size:
            size = len(data) / command.data_field_count
        else:
            size = command.data_size

        payload_content = pack(command.data_struct_format, *data)

    payload_header = pack('<2B', size, code)

    payload = payload_header + payload_content

    checksum = pack('<B', crc8_xor(payload))

    return MESSAGE_OUTGOING_HEADER + payload + checksum

def decode_names(data: tuple) -> tuple[str]:
    """Decodes the deserialized string value and splits it to a tuple.

    Parameters
    ----------
    data : tuple
        The `struct` unpacked payload tuple to decode.

    Raises
    ------
    TypeError
        If `data` is not of type `tuple`.
    UnicodeDecodeError
        If the bytes cannot be decoded into ASCII characters.

    Returns
    -------
    tuple[str]
        A tuple of decoded names.
    """
    return tuple(data[0].decode('ascii').split(';'))
