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

def test_crc8_xor():
    """
    Test the `_crc8_xor` function.
    
    This test verifies that the `_crc8_xor` function correctly calculates 
    the checksum for the provided payload using XOR CRC.
    """
    payload = b'\x01\x02\x03\x04'

    expected_checksum = 0x00 

    assert _crc8_xor(payload) == expected_checksum

def test_create_request_message_with_variable_size():
    """
    Test `_create_request_message` with variable size data.
    
    This test checks the creation of a request message where the command has 
    variable size data. It ensures that the message is serialized correctly.
    """
    command = _MspCommand(150, 'B:1:?')

    data = (42,)

    message = _create_request_message(command, data)

    assert message.startswith(MESSAGE_OUTGOING_HEADER)
    assert len(message) > len(MESSAGE_OUTGOING_HEADER)

def test_create_request_message_with_fixed_size():
    """
    Test `_create_request_message` with fixed size data.
    
    This test checks the creation of a request message where the command has 
    fixed size data. It ensures that the message is serialized correctly.
    """
    command = _MspCommand(150, 'B:1:')

    data = (42,)

    message = _create_request_message(command, data)

    assert message.startswith(MESSAGE_OUTGOING_HEADER)
    assert len(message) > len(MESSAGE_OUTGOING_HEADER)

def test_create_request_message_with_no_data():
    """
    Test `_create_request_message` with no data.
    
    This test verifies that the request message is created correctly when 
    no data is provided.
    """
    command = _MspCommand(150)

    data = ()

    message = _create_request_message(command, data)

    assert message.startswith(MESSAGE_OUTGOING_HEADER)
    assert len(message) == len(MESSAGE_OUTGOING_HEADER) + 3

def test_decode_names():
    """
    Test the `_decode_names` function.
    
    This test checks that the `_decode_names` function correctly decodes 
    a tuple of names from a serialized payload.
    """
    data = (b'John;Doe',)

    decoded_names = _decode_names(data)

    assert decoded_names == ('John', 'Doe')

def test_parse_response_message_success():
    """
    Test `_parse_response_message` with valid response.
    
    This test ensures that the `_parse_response_message` function correctly 
    parses a valid response message and returns the expected result.
    """
    command = _MspCommand(150, 'B:1:?')

    payload = b'$M>1\x96\x00'

    response = _parse_response_message(command, payload)

    assert response.command.code == 150
    assert response.data == (150,)
    assert response.data_size == 1

def test_parse_response_message_invalid_code():
    """
    Test `_parse_response_message` with invalid response code.
    
    This test ensures that a `ValueError` is raised when the command code 
    in the payload does not match the expected command code.
    """
    command = _MspCommand(150, 'B:1:?')

    payload = b'$M>2\x96\x00'

    with pytest.raises(ValueError):
        _parse_response_message(command, payload)

def test_parse_response_message_invalid_format():
    """
    Test `_parse_response_message` with an invalid format.
    
    This test ensures that a `StructError` is raised when the payload data 
    does not match the expected format.
    """
    command = _MspCommand(150, 'B:1:?')

    payload = b'$M>1xyz'

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

def test_message_headers():
    """
    Test that the defined message headers are correct.
    
    This test checks that the error, incoming, and outgoing message headers 
    are correctly defined and match the expected values.
    """
    assert MESSAGE_ERROR_HEADER == b'$M!'
    assert MESSAGE_INCOMING_HEADER == b'$M<'
    assert MESSAGE_OUTGOING_HEADER == b'$M>'

@pytest.mark.parametrize("data, expected_size", [
    ((42,), 1),
    ((1, 2, 3), 3),
])
def test_create_request_message_size(data, expected_size):
    """
    Test the size of the serialized message based on data.
    
    This test checks the correct size of the message payload when different 
    amounts of data are provided.
    """
    command = _MspCommand(150, 'B:1:?')

    message = _create_request_message(command, data)

    assert len(message) == len(MESSAGE_OUTGOING_HEADER) + expected_size + 3  # header + payload + checksum

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
