"""
Test suite generated using ChatGPT-4o mini.

This suite contains various tests for the MspAnalog, MspIdent, MspMisc, MspSetMisc, and 
MspStatus classes to ensure correct functionality. It covers different edge cases, 
invalid inputs, and verifies the expected behavior of properties, methods, and attributes 
for parsing, compiling, and serializing MultiWii data commands.
"""

from multiwii.config import (
    MultiWiiCapability,
    MultiWiiMultitype,
    MultiWiiSensor
)

from multiwii.data import (
    MspAnalog,
    MspIdent,
    MspMisc,
    MspSetMisc,
    MspStatus
)

import pytest

def test_msp_analog_parse():
    """
    Test that MspAnalog.parse correctly parses a tuple of data values into an MspAnalog instance.
    """
    data = (120.0, 500, 80, 1500)

    result = MspAnalog.parse(data)
    
    assert isinstance(result, MspAnalog)
    assert result.voltage == 12.0
    assert result.power_meter_sum == 500
    assert result.rssi == 80
    assert result.amperage == 1500

def test_msp_ident_parse():
    """
    Test that MspIdent.parse correctly parses a tuple of data values into an MspIdent instance.
    """
    data = (1, 2, 0b101, 3)

    result = MspIdent.parse(data)
    
    assert isinstance(result, MspIdent)
    assert result.version == 1
    assert result.multitype == MultiWiiMultitype.TYPE_2
    assert len(result.capabilities) == 3
    assert result.navigation_version == 3

def test_msp_misc_parse():
    """
    Test that MspMisc.parse correctly parses a tuple of data values into an MspMisc instance.
    """
    data = (1, 2, 3, 4, 5, 6, 7, 80, 9, 10, 11, 12)

    result = MspMisc.parse(data)
    
    assert isinstance(result, MspMisc)
    assert result.power_trigger == 1
    assert result.throttle_failsafe == 2
    assert result.throttle_idle == 3
    assert result.throttle_min == 4
    assert result.throttle_max == 5
    assert result.power_logger_arm == 6
    assert result.power_logger_lifetime == 7
    assert result.magnetometer_declination == 8.0
    assert result.battery_scale == 9
    assert result.battery_warning_1 == 1.0
    assert result.battery_warning_2 == 1.1
    assert result.battery_critical == 1.2

def test_msp_set_misc_as_serializable():
    """
    Test that MspSetMisc.as_serializable returns the correct tuple of integer values.
    """
    misc = MspSetMisc(
        power_trigger=1,
        throttle_min=2,
        throttle_max=3,
        min_command=4,
        throttle_failsafe=5,
        power_logger_arm=6,
        power_logger_lifetime=7,
        magnetometer_declination=8.0,
        battery_scale=9,
        battery_warning_1=10.0,
        battery_warning_2=11.0,
        battery_critical=12.0
    )
    
    serializable_data = misc.as_serializable()

    assert isinstance(serializable_data, tuple)
    assert len(serializable_data) == 12
    assert serializable_data == (
        1, 2, 3, 4, 5, 6, 7, 80, 9, 100, 110, 120
    )

def test_msp_status_parse():
    """
    Test that MspStatus.parse correctly parses a tuple of data values into an MspStatus instance.
    """
    data = (1000, 5, 0b1010, 3, 7)

    result = MspStatus.parse(data)
    
    assert isinstance(result, MspStatus)
    assert result.cycle_time == 1000
    assert result.i2c_errors == 5
    assert len(result.sensors) == 2
    assert result.status_flag == 3
    assert result.global_config == 7

def test_msp_analog_parse_invalid_data():
    """
    Test that MspAnalog.parse raises an error when provided with invalid data.
    """
    with pytest.raises(TypeError):
        MspAnalog.parse("invalid_data")

def test_msp_ident_parse_invalid_data():
    """
    Test that MspIdent.parse raises an error when provided with invalid data.
    """
    with pytest.raises(ValueError):
        MspIdent.parse(("invalid", "data", "tuple"))

def test_msp_misc_parse_invalid_data():
    """
    Test that MspMisc.parse raises an error when provided with incomplete or invalid data.
    """
    with pytest.raises(ValueError):
        MspMisc.parse((1, 2, 3))

def test_msp_set_misc_as_serializable_empty():
    """
    Test that MspSetMisc.as_serializable handles an empty instance correctly.
    """
    misc = MspSetMisc(
        power_trigger=0,
        throttle_min=0,
        throttle_max=0,
        min_command=0,
        throttle_failsafe=0,
        power_logger_arm=0,
        power_logger_lifetime=0,
        magnetometer_declination=0.0,
        battery_scale=0,
        battery_warning_1=0.0,
        battery_warning_2=0.0,
        battery_critical=0.0
    )
    
    serializable_data = misc.as_serializable()

    assert serializable_data == (
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    )

def test_msp_status_parse_invalid_data():
    """
    Test that MspStatus.parse raises an error when provided with invalid data.
    """
    with pytest.raises(ValueError):
        MspStatus.parse(("invalid", "data", "tuple"))
