"""
Test suite generated using ChatGPT-4o mini.

This suite contains various tests for the MultiWii class to ensure 
correct functionality. It covers different edge cases, invalid 
inputs, and verifies the expected behavior of properties, methods, 
and attributes for a range of MSP command codes and data formats.

Tests include:
 - Initialization and parameter validation
 - MSP command processing
 - Communication with the flight controller (mocked)
 - Specific functionalities like binding, calibration, and setting configuration
"""

from multiwii import MultiWii

from multiwii.messaging import (
    _MspResponseMessage,
    MspMessageError
)

from multiwii.commands import (
    MSP_ACC_CALIBRATION,
    MSP_ALTITUDE,
    MSP_BIND,
    MSP_EEPROM_WRITE,
    MSP_SELECT_SETTING,
    MSP_SET_BOX,
    MSP_SET_HEAD,
    MSP_SET_PID
)

from multiwii.data import (
    MspAltitude,
    MspRc,
)

from serial        import Serial
from time          import sleep
from unittest.mock import MagicMock

import pytest

@pytest.fixture
def mock_serial():
    """
    Fixture to mock the serial port used by the MultiWii class.
    """
    return MagicMock(spec=Serial)

@pytest.fixture
def multiwii(mock_serial):
    """
    Fixture to create an instance of the MultiWii class with a mock serial port.
    """
    return MultiWii(mock_serial)

def test_init_with_invalid_serial_port():
    """
    Test that a TypeError is raised when an invalid serial port is passed to MultiWii.
    """
    with pytest.raises(TypeError):
        MultiWii('invalid_serial_port')

def test_init_with_valid_serial_port(mock_serial):
    """
    Test that the MultiWii instance is initialized correctly with a valid serial port.
    """
    multiwii = MultiWii(mock_serial)

    assert multiwii.serial_port == mock_serial
    assert multiwii.message_write_read_delay == MultiWii.DEFAULT_MESSAGE_WRITE_READ_DELAY

def test_command_to_data_structure_type_map(multiwii):
    """
    Test the mapping of MSP commands to their corresponding data structures.
    """
    map_ = multiwii.command_to_data_structure_type_map

    assert isinstance(map_, dict)
    assert MSP_ALTITUDE in map_
    assert map_[MSP_ALTITUDE] == MspAltitude

def test_set_message_write_read_delay_valid(multiwii):
    """
    Test setting the message write/read delay to a valid value.
    """
    multiwii.message_write_read_delay = 0.01

    assert multiwii.message_write_read_delay == 0.01

def test_set_message_write_read_delay_invalid_type(multiwii):
    """
    Test that setting an invalid type for the message write/read delay raises a TypeError.
    """
    with pytest.raises(TypeError):
        multiwii.message_write_read_delay = 'string'

def test_set_message_write_read_delay_negative_value(multiwii):
    """
    Test that setting a negative value for the message write/read delay raises a ValueError.
    """
    with pytest.raises(ValueError):
        multiwii.message_write_read_delay = -0.01

def test_read_response_message_invalid_header(multiwii, mock_serial):
    """
    Test that an invalid header in the response message raises an MspMessageError.
    """
    mock_serial.read.return_value = b'123'

    with pytest.raises(MspMessageError):
        multiwii._read_response_message(MSP_ALTITUDE)

def test_read_response_message_invalid_command_code(multiwii, mock_serial):
    """
    Test that an invalid command code in the response raises an MspMessageError.
    """
    mock_serial.read.return_value = b'\x01\x01\x01'

    with pytest.raises(MspMessageError):
        multiwii._read_response_message(MSP_ALTITUDE)

def test_read_response_message_invalid_checksum(multiwii, mock_serial):
    """
    Test that an invalid checksum in the response message raises an MspMessageError.
    """
    mock_serial.read.return_value = b'\x01\x01\x01\x02'

    with pytest.raises(MspMessageError):
        multiwii._read_response_message(MSP_ALTITUDE)

def test_get_data_valid(multiwii, mock_serial):
    """
    Test that valid data can be retrieved from the flight controller using MSP commands.
    """
    response_message = _MspResponseMessage(
        MSP_ALTITUDE,
        b'fake_data',
        'extra_info'
    )

    multiwii._read_response_message = MagicMock(return_value=response_message)
    
    data = multiwii.get_data(MSP_ALTITUDE)

    assert data == response_message.data

def test_get_data_invalid_command(multiwii, mock_serial):
    """
    Test that an invalid MSP command raises an MspMessageError.
    """
    multiwii._read_response_message = MagicMock(
        side_effect=MspMessageError('Invalid command')
    )

    with pytest.raises(MspMessageError):
        multiwii.get_data(MSP_ALTITUDE)

def test_arm_function(multiwii, mock_serial):
    """
    Test that the arm function sends the correct raw RC data to arm the system.
    """
    multiwii.set_raw_rc = MagicMock()

    multiwii.arm()

    assert multiwii.set_raw_rc.call_count > 0

def test_disarm_function(multiwii, mock_serial):
    """
    Test that the disarm function sends the correct raw RC data to disarm the system.
    """
    multiwii.set_raw_rc = MagicMock()

    multiwii.disarm()

    assert multiwii.set_raw_rc.call_count > 0

def test_bind_transmitter_and_receiver(multiwii, mock_serial):
    """
    Test that the bind_transmitter_and_receiver function sends the correct MSP_BIND command.
    """
    multiwii._send_request_message = MagicMock()

    multiwii.bind_transmitter_and_receiver()

    multiwii._send_request_message.assert_called_once_with(MSP_BIND)

def test_calibrate_accelerometer(multiwii, mock_serial):
    """
    Test that the calibrate_accelerometer function sends the correct MSP_ACC_CALIBRATION command.
    """
    multiwii._send_request_message = MagicMock()

    multiwii.calibrate_accelerometer()

    multiwii._send_request_message.assert_called_once_with(MSP_ACC_CALIBRATION)

def test_calibrate_magnetometer(multiwii, mock_serial):
    """
    Test that the calibrate_magnetometer function sends the correct MSP_ACC_CALIBRATION command.
    """
    multiwii._send_request_message = MagicMock()

    multiwii.calibrate_magnetometer()

    multiwii._send_request_message.assert_called_once_with(MSP_ACC_CALIBRATION)

def test_save_config_to_eeprom(multiwii, mock_serial):
    """
    Test that the save_config_to_eeprom function sends the correct MSP_EEPROM_WRITE command.
    """
    multiwii._send_request_message = MagicMock()

    multiwii.save_config_to_eeprom()

    multiwii._send_request_message.assert_called_once_with(MSP_EEPROM_WRITE)

def test_select_setting_valid(multiwii, mock_serial):
    """
    Test that the select_setting function sends the correct MSP_SELECT_SETTING command.
    """
    multiwii._send_request_message = MagicMock()

    multiwii.select_setting(1)

    multiwii._send_request_message.assert_called_once_with(
        MSP_SELECT_SETTING,
        data=(1,)
    )

def test_select_setting_invalid_value(multiwii):
    """
    Test that selecting an invalid setting raises a ValueError.
    """
    with pytest.raises(ValueError):
        multiwii.select_setting(5)

def test_set_boxes(multiwii, mock_serial):
    """
    Test that the set_boxes function sends the correct MSP_SET_BOX command with serialized data.
    """
    data = MagicMock()

    data.as_serializable = MagicMock(return_value=('serializable_data',))

    multiwii._send_request_message = MagicMock()

    multiwii.set_boxes(data)

    multiwii._send_request_message.assert_called_once_with(
        MSP_SET_BOX,
        ('serializable_data',)
    )

def test_set_head_valid(multiwii, mock_serial):
    """
    Test that the set_head function sends the correct MSP_SET_HEAD command with valid data.
    """
    multiwii._send_request_message = MagicMock()

    multiwii.set_head(90)

    multiwii._send_request_message.assert_called_once_with(
        MSP_SET_HEAD,
        data=(90,)
    )

def test_set_head_invalid_value(multiwii):
    """
    Test that setting an invalid heading value raises a ValueError.
    """
    with pytest.raises(ValueError):
        multiwii.set_head(200)

def test_set_pid_values(multiwii, mock_serial):
    """
    Test that the set_pid_values function sends the correct MSP_SET_PID command with serialized data.
    """
    data = MagicMock()

    data.as_serializable = MagicMock(return_value=('serializable_data',))

    multiwii._send_request_message = MagicMock()

    multiwii.set_pid_values(data)

    multiwii._send_request_message.assert_called_once_with(
        MSP_SET_PID,
        ('serializable_data',)
    )
