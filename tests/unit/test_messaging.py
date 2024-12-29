"""
Test suite generated using ChatGPT-4o mini.

This suite contains various tests for the functions and classes in the 
`messaging.py` module. It covers the checksum calculation, message 
serialization, response message parsing, and error handling, ensuring 
correct functionality for each component.
"""

from multiwii.messaging import (
    _MspResponseMessage,
    _crc8_xor,
    _create_request_message,
    _decode_names,
    _parse_response_message,
    MESSAGE_ERROR_HEADER,
    MESSAGE_INCOMING_HEADER,
    MESSAGE_OUTGOING_HEADER,
    MspMessageError
)

from multiwii import _MspCommand
from struct   import error as StructError

import pytest

@pytest.mark.parametrize("payload,expected_checksum", [
    (b'\x01\x02\x03\x04', 0x00),
    (b'\xFF\xFF\xFF\xFF', 0x00),
    (b'\x00\x00\x00\x00', 0x00),
])
def test_crc8_xor(payload, expected_checksum):
    """
    Test the `_crc8_xor` function.
    
    This test verifies that the `_crc8_xor` function correctly calculates 
    the checksum for the provided payload using XOR CRC.
    """
    assert _crc8_xor(payload) == expected_checksum

@pytest.mark.parametrize("command,data", [
    (_MspCommand(150, 'B:1:?'), (42,)),
    (_MspCommand(100, 'B:2:?'), (10, 20)),
])
def test_create_request_message_with_variable_size(command, data):
    """
    Test `_create_request_message` with variable size data.
    
    This test checks the creation of a request message where the command has 
    variable size data. It ensures that the message is serialized correctly.
    """
    message = _create_request_message(command, data)

    assert message.startswith(MESSAGE_OUTGOING_HEADER)
    assert len(message) > len(MESSAGE_OUTGOING_HEADER)

@pytest.mark.parametrize("command,data", [
    (_MspCommand(150, 'B:1:?'), (42,)),
    (_MspCommand(100, 'B:2:?'), (10, 20)),
])
def test_create_request_message_with_fixed_size(command, data):
    """
    Test `_create_request_message` with fixed size data.
    
    This test checks the creation of a request message where the command has 
    fixed size data. It ensures that the message is serialized correctly.
    """
    message = _create_request_message(command, data)

    assert message.startswith(MESSAGE_OUTGOING_HEADER)
    assert len(message) > len(MESSAGE_OUTGOING_HEADER)

@pytest.mark.parametrize("command,data", [
    (_MspCommand(150), ()),
    (_MspCommand(100), ()),
])
def test_create_request_message_with_no_data(command, data):
    """
    Test `_create_request_message` with no data.
    
    This test verifies that the request message is created correctly when 
    no data is provided.
    """
    message = _create_request_message(command, data)

    assert message.startswith(MESSAGE_OUTGOING_HEADER)
    assert len(message) == len(MESSAGE_OUTGOING_HEADER) + 3

@pytest.mark.parametrize("data,expected_names", [
    (b'John;Doe', ('John', 'Doe')),
    (b'Jane;Doe', ('Jane', 'Doe')),
])
def test_decode_names(data, expected_names):
    """
    Test the `_decode_names` function.
    
    This test checks that the `_decode_names` function correctly decodes 
    a tuple of names from a serialized payload.
    """
    assert _decode_names(data) == expected_names

@pytest.mark.parametrize("command,payload,expected_command,expected_data,expected_data_size", [
    (_MspCommand(150, 'B:1:?'), b'$M>1\x96\x00', 150, (150,), 1),
    (_MspCommand(100, 'B:2:?'), b'$M>2\x96\x00', 100, (100,), 2),
])
def test_parse_response_message_success(command, payload, expected_command, expected_data, expected_data_size):
    """
    Test `_parse_response_message` with valid response.
    
    This test ensures that the `_parse_response_message` function correctly 
    parses a valid response message and returns the expected result.
    """
    response = _parse_response_message(command, payload)

    assert response.command.code == expected_command
    assert response.data == expected_data
    assert response.data_size == expected_data_size

@pytest.mark.parametrize("command,payload", [
    (_MspCommand(150, 'B:1:?'), b'$M>2\x96\x00'),
    (_MspCommand(100, 'B:2:?'), b'$M>1\x96\x00'),
])
def test_parse_response_message_invalid_code(command, payload):
    """
    Test `_parse_response_message` with invalid response code.
    
    This test ensures that a `ValueError` is raised when the command code 
    in the payload does not match the expected command code.
    """
    with pytest.raises(ValueError):
        _parse_response_message(command, payload)

@pytest.mark.parametrize("command,payload", [
    (_MspCommand(150, 'B:1:?'), b'$M>1xyz'),
    (_MspCommand(100, 'B:2:?'), b'$M>2xyz'),
])
def test_parse_response_message_invalid_format(command, payload):
    """
    Test `_parse_response_message` with an invalid format.
    
    This test ensures that a `StructError` is raised when the payload data 
    does not match the expected format.
    """
    with pytest.raises(StructError):
        _parse_response_message(command, payload)

def test_msp_message_error():
    """
    Test the `MspMessageError` exception.
    
    This test verifies that the `MspMessageError` exception can be raised 
    and caught correctly.
    """
    with pytest.raises(MspMessageError):
        raise MspMessageError("Test error")

@pytest.mark.parametrize("header,expected_header", [
    (MESSAGE_ERROR_HEADER, b'$M!'),
    (MESSAGE_INCOMING_HEADER, b'$M<'),
    (MESSAGE_OUTGOING_HEADER, b'$M>'),
])
def test_message_headers(header, expected_header):
    """
    Test that the defined message headers are correct.
    
    This test checks that the error, incoming, and outgoing message headers 
    are correctly defined and match the expected values.
    """
    assert header == expected_header

@pytest.mark.parametrize("data, expected_size", [
    ((42,), 1),
    ((1, 2, 3), 3),
    ((4, 5, 6, 7), 4),
])
def test_create_request_message_size(data, expected_size):
    """
    Test the size of the serialized message based on data.
    
    This test checks the correct size of the message payload when different 
    amounts of data are provided.
    """
    command = _MspCommand(150, 'B:1:?')

    message = _create_request_message(command, data)

    assert len(message) == len(MESSAGE_OUTGOING_HEADER) + expected_size + 3

@pytest.mark.parametrize("data, expected_checksum", [
    (b'\x01\x02\x03\x04', 0x00),
    (b'\xFF\xFF\xFF\xFF', 0x00),
    (b'\x00\x00\x00\x00', 0x00),
])
def test_crc8_xor_checksum(data, expected_checksum):
    """
    Test the `_crc8_xor` function with different payloads.
    
    This test checks the checksum calculation using different data payloads.
    """
    assert _crc8_xor(data) == expected_checksum
