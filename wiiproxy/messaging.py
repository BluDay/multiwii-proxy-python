from .command import Command

from typing import Final, NamedTuple
from struct import pack

# --------------------------------------- CONSTANTS ----------------------------------------

MESSAGE_ERROR_HEADER:    Final[bytes] = b'$M!' # 0x24, 0x4d, 0x21

MESSAGE_INCOMING_HEADER: Final[bytes] = b'$M<' # 0x24, 0x4d, 0x3c

MESSAGE_OUTGOING_HEADER: Final[bytes] = b'$M>' # 0x24, 0x4d, 0x3e

# ---------------------------------------- CLASSES -----------------------------------------

class _MspResponseMessage(NamedTuple):
    """Represents a tuple with the data size and values for a received MSP message.

    Attributes
    ----------
    command : Command
        An instance of Command of the targeted MSP command.
    data : tuple[int]
        A tuple of parsed data values.
    raw_data_size : int
        The size of the unserialized data values.
    """
    command: Command

    data: tuple[int]

    raw_data_size: int

class MspMessageError(Exception):
    """Represents a specific errors related to MSP messages."""
    pass

# --------------------------------------- FUNCTIONS ----------------------------------------

def _crc8_xor(payload: bytes) -> int:
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

def _create_request_message(command: Command, data: tuple[int]) -> bytes:
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
    command_code = command.code

    data_size = 0

    payload_content = b''

    if data:
        if command.has_variable_size:
            data_size = len(data) / command.data_field_count
        else:
            data_size = command.data_size

        payload_content = pack(command.data_struct_format, *data)

    payload_header = pack('<2B', data_size, command_code)

    payload = payload_header + payload_content

    checksum = pack('<B', _crc8_xor(payload))

    return MESSAGE_OUTGOING_HEADER + payload + checksum

def _decode_names(data: tuple) -> tuple[str]:
    """Decodes the deserialized string value and splits it to a tuple.

    Parameters
    ----------
    data : tuple
        The `struct` unpacked payload tuple to decode.

    Returns
    -------
    tuple[str]
        A tuple of decoded names.
    """
    return tuple(data[0].decode('ascii').split(';'))

def _parse_response_message(command: Command, payload: bytes) -> _MspResponseMessage:
    """Parses the payload of a response message for a given command.

    Attributes
    ----------
    command : Command
        An instance of Command representing the MSP command for the response message.
    payload : bytes
        The received payload buffer from a response message.

    Raises
    ------
    ValueError
        If the command code in the payload does not match the code of the provided
        command.

    Returns
    -------
    _MspResponseMessage
        A named tuple with the command, parsed data and additional information.
    """
    received_command_code = payload[1]

    if received_command_code != command.code:
        raise ValueError(
            'Payload with an invalid command code detected. ({}, {})'.format(
                command.code,
                received_command_code
            )
        )

    raw_data_size = payload[0]

    parsed_data = unpack(command.data_struct_format, payload)

    return _MspResponseMessage(command, parsed_data, raw_data_size)
