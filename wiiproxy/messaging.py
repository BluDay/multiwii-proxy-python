from .command import Command

from typing import Final
from struct import calcsize, pack as struct_pack

# --------------------------------------- CONSTANTS ----------------------------------------

_ENDIANNESS: Final[str] = '<'

_PAYLOAD_STRUCT_FORMAT:  Final[str] = _ENDIANNESS + 'BH'

_CHECKSUM_STRUCT_FORMAT: Final[str] = _ENDIANNESS + 'B'

MESSAGE_ERROR_HEADER:    Final[bytes] = b'$M!' # 0x24, 0x4d, 0x21

MESSAGE_INCOMING_HEADER: Final[bytes] = b'$M<' # 0x24, 0x4d, 0x3c

MESSAGE_OUTGOING_HEADER: Final[bytes] = b'$M>' # 0x24, 0x4d, 0x3e

# --------------------------------------- FUNCTIONS ----------------------------------------

def _create_payload_struct_format(data_struct_format: str) -> str:
    """Creates a `struct` payload format string using the provided data structure format.

    Returns
    -------
    str
        The complete payload format string to be used with `struct`.
    """
    data_size = calcsize(_ENDIANNESS + data_struct_format)

    return _ENDIANNESS + 'B' if data_size <= 0xff else 'H'

def calculate_checksum(payload: bytes) -> int:
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

    for byte in data: checksum ^= byte

    return checksum & 0xff

def create_message(command: Command, data: tuple[int]) -> bytes:
    """Constructs a serializes message and returns it.

    Attributes
    ----------
    command : Command
        An instance of Command representing the MSP command used to create the message.

    Returns
    -------
    bytes
        The full message in bytes.
    """
    data_size = command.struct_format_size

    # TODO: Update the data size if command has an indeterminate data size.

    payload = struct_pack(
        _PAYLOAD_STRUCT_FORMAT + command.struct_format,
        command.code,
        data_size,
        *data
    )

    checksum = struct_pack(
        _CHECKSUM_STRUCT_FORMAT,
        calculate_checksum(serialized_payload)
    )

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
