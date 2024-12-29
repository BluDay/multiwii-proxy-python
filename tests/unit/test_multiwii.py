from multiwii import MultiWii

from multiwii.messaging import _MspResponseMessage, MspMessageError

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

from multiwii.data import MspAltitude, MspRc

from serial        import Serial
from time          import sleep
from unittest.mock import MagicMock

import pytest

@pytest.fixture
def mock_serial():
    return MagicMock(spec=Serial)

@pytest.fixture
def multiwii(mock_serial):
    return MultiWii(mock_serial)

@pytest.mark.parametrize("serial_port", ['invalid_serial_port'])
def test_init_with_invalid_serial_port(serial_port):
    with pytest.raises(TypeError):
        MultiWii(serial_port)

@pytest.mark.parametrize("mock_serial", [MagicMock(spec=Serial)])
def test_init_with_valid_serial_port(mock_serial):
    multiwii = MultiWii(mock_serial)

    assert multiwii.serial_port == mock_serial
    assert multiwii.message_write_read_delay == MultiWii.DEFAULT_MESSAGE_WRITE_READ_DELAY

def test_command_to_data_structure_type_map(multiwii):
    map_ = multiwii.command_to_data_structure_type_map

    assert isinstance(map_, dict)
    assert MSP_ALTITUDE in map_
    assert map_[MSP_ALTITUDE] == MspAltitude

@pytest.mark.parametrize("valid_delay", [0.01])
def test_set_message_write_read_delay_valid(multiwii, valid_delay):
    multiwii.message_write_read_delay = valid_delay

    assert multiwii.message_write_read_delay == valid_delay

@pytest.mark.parametrize("invalid_delay", ['string'])
def test_set_message_write_read_delay_invalid_type(multiwii, invalid_delay):
    with pytest.raises(TypeError):
        multiwii.message_write_read_delay = invalid_delay

@pytest.mark.parametrize("negative_delay", [-0.01])
def test_set_message_write_read_delay_negative_value(multiwii, negative_delay):
    with pytest.raises(ValueError):
        multiwii.message_write_read_delay = negative_delay

def test_read_response_message_invalid_header(multiwii, mock_serial):
    mock_serial.read.return_value = b'123'

    with pytest.raises(MspMessageError):
        multiwii._read_response_message(MSP_ALTITUDE)

def test_read_response_message_invalid_command_code(multiwii, mock_serial):
    mock_serial.read.return_value = b'\x01\x01\x01'

    with pytest.raises(MspMessageError):
        multiwii._read_response_message(MSP_ALTITUDE)

def test_read_response_message_invalid_checksum(multiwii, mock_serial):
    mock_serial.read.return_value = b'\x01\x01\x01\x02'

    with pytest.raises(MspMessageError):
        multiwii._read_response_message(MSP_ALTITUDE)

def test_get_data_valid(multiwii, mock_serial):
    response_message = _MspResponseMessage(
        MSP_ALTITUDE,
        b'\x01\x01\x01\x03\x00\x05',
        6
    )

    multiwii._read_response_message = MagicMock(return_value=response_message)
    
    data = multiwii.get_data(MSP_ALTITUDE)

    assert data == response_message.data

@pytest.mark.parametrize("error_message", ['Invalid command'])
def test_get_data_invalid_command(multiwii, mock_serial, error_message):
    multiwii._read_response_message = MagicMock(
        side_effect=MspMessageError(error_message)
    )

    with pytest.raises(MspMessageError):
        multiwii.get_data(MSP_ALTITUDE)

def test_arm_function(multiwii, mock_serial):
    multiwii.set_raw_rc = MagicMock()

    multiwii.arm()

    assert multiwii.set_raw_rc.call_count > 0

def test_disarm_function(multiwii, mock_serial):
    multiwii.set_raw_rc = MagicMock()

    multiwii.disarm()

    assert multiwii.set_raw_rc.call_count > 0

def test_bind_transmitter_and_receiver(multiwii, mock_serial):
    multiwii._send_request_message = MagicMock()

    multiwii.bind_transmitter_and_receiver()

    multiwii._send_request_message.assert_called_once_with(MSP_BIND)

def test_calibrate_accelerometer(multiwii, mock_serial):
    multiwii._send_request_message = MagicMock()

    multiwii.calibrate_accelerometer()

    multiwii._send_request_message.assert_called_once_with(MSP_ACC_CALIBRATION)

def test_calibrate_magnetometer(multiwii, mock_serial):
    multiwii._send_request_message = MagicMock()

    multiwii.calibrate_magnetometer()

    multiwii._send_request_message.assert_called_once_with(MSP_ACC_CALIBRATION)

def test_save_config_to_eeprom(multiwii, mock_serial):
    multiwii._send_request_message = MagicMock()

    multiwii.save_config_to_eeprom()

    multiwii._send_request_message.assert_called_once_with(MSP_EEPROM_WRITE)

@pytest.mark.parametrize("setting_value", [1])
def test_select_setting_valid(multiwii, mock_serial, setting_value):
    multiwii._send_request_message = MagicMock()

    multiwii.select_setting(setting_value)

    multiwii._send_request_message.assert_called_once_with(
        MSP_SELECT_SETTING,
        data=(setting_value,)
    )

@pytest.mark.parametrize("invalid_setting", [5])
def test_select_setting_invalid_value(multiwii, invalid_setting):
    with pytest.raises(ValueError):
        multiwii.select_setting(invalid_setting)

def test_set_boxes(multiwii, mock_serial):
    data = MagicMock()

    data.as_serializable = MagicMock(return_value=('serializable_data',))

    multiwii._send_request_message = MagicMock()

    multiwii.set_boxes(data)

    multiwii._send_request_message.assert_called_once_with(
        MSP_SET_BOX,
        ('serializable_data',)
    )

@pytest.mark.parametrize("heading_value", [90])
def test_set_head_valid(multiwii, mock_serial, heading_value):
    multiwii._send_request_message = MagicMock()

    multiwii.set_head(heading_value)

    multiwii._send_request_message.assert_called_once_with(
        MSP_SET_HEAD,
        data=(heading_value,)
    )

@pytest.mark.parametrize("invalid_heading", [200])
def test_set_head_invalid_value(multiwii, invalid_heading):
    with pytest.raises(ValueError):
        multiwii.set_head(invalid_heading)

def test_set_pid_values(multiwii, mock_serial):
    data = MagicMock()

    data.as_serializable = MagicMock(return_value=('serializable_data',))

    multiwii._send_request_message = MagicMock()

    multiwii.set_pid_values(data)

    multiwii._send_request_message.assert_called_once_with(
        MSP_SET_PID,
        ('serializable_data',)
    )
