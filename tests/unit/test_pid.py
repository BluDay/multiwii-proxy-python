"""
Test suite for the MspPid and MspPidNames classes.

This suite tests the functionality of the MspPid and MspPidNames classes, ensuring correct parsing,
serialization, and handling of PID values and names in the MultiWii flight controller.
"""

from multiwii.data import (
    MspPid,
    MspPidNames,
    Pid
)

from multiwii.messaging import _decode_names

import pytest

def test_msp_pid_parse():
    """
    Test that MspPid.parse correctly parses a tuple of data values into an MspPid instance.
    """
    data = (
        100, 200, 300,
        400, 500, 600,
        700, 800, 900,
        1000, 1100, 1200,
        1300, 1400, 1500,
        1600, 1700, 1800,
        1900, 2000, 2100,
        2200, 2300, 2400,
        2500, 2600, 2700,
        2800, 2900, 3000
    )
    
    result = MspPid.parse(data)
    
    assert isinstance(result, MspPid)
    assert result.roll.p == 100
    assert result.roll.i == 200
    assert result.roll.d == 300
    assert result.pitch.p == 400
    assert result.pitch.i == 500
    assert result.pitch.d == 600
    assert result.yaw.p == 700
    assert result.yaw.i == 800
    assert result.yaw.d == 900

def test_msp_pid_parse_invalid_data():
    """
    Test that MspPid.parse raises an error when provided with invalid data (less than required number of elements).
    """
    data = (100, 200, 300, 400, 500)
    
    with pytest.raises(TypeError):
        MspPid.parse(data)

def test_msp_pid_as_serializable():
    """
    Test that MspPid.as_serializable returns the correct tuple of serializable values.
    """
    pid = MspPid(
        roll=Pid(100, 200, 300),
        pitch=Pid(400, 500, 600),
        yaw=Pid(700, 800, 900),
        altitude_hold=Pid(1000, 1100, 1200),
        position_hold=Pid(1300, 1400, 1500),
        position_rate=Pid(1600, 1700, 1800),
        navigation_rate=Pid(1900, 2000, 2100),
        level_mode=Pid(2200, 2300, 2400),
        magnetometer=Pid(2500, 2600, 2700),
        velocity=Pid(2800, 2900, 3000)
    )

    serializable_data = pid.as_serializable()
    
    assert isinstance(serializable_data, tuple)
    assert serializable_data == (
        100, 200, 300, 400, 500, 600, 700, 800, 900,
        1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800,
        1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 
        2800, 2900, 3000
    )

def test_msp_pid_as_serializable_empty():
    """
    Test that MspPid.as_serializable handles an empty instance correctly.
    """
    pid = MspPid(
        roll=Pid(0, 0, 0),
        pitch=Pid(0, 0, 0),
        yaw=Pid(0, 0, 0),
        altitude_hold=Pid(0, 0, 0),
        position_hold=Pid(0, 0, 0),
        position_rate=Pid(0, 0, 0),
        navigation_rate=Pid(0, 0, 0),
        level_mode=Pid(0, 0, 0),
        magnetometer=Pid(0, 0, 0),
        velocity=Pid(0, 0, 0)
    )

    serializable_data = pid.as_serializable()
    
    assert serializable_data == (
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0
    )

def test_msp_pidnames_parse():
    """
    Test that MspPidNames.parse correctly parses a tuple of data values into an MspPidNames instance.
    """
    data = ("Roll", "Pitch", "Yaw", "AltitudeHold", "PositionHold")

    result = MspPidNames.parse(data)
    
    assert isinstance(result, MspPidNames)
    assert result.names == ("Roll", "Pitch", "Yaw", "AltitudeHold", "PositionHold")

def test_msp_pidnames_parse_invalid_data():
    """
    Test that MspPidNames.parse raises an error when provided with invalid data (non-string elements).
    """
    data = (1, 2, 3)
    
    with pytest.raises(TypeError):
        MspPidNames.parse(data)

def test_msp_pidnames_empty():
    """
    Test that MspPidNames handles empty names correctly.
    """
    data = ()

    result = MspPidNames.parse(data)
    
    assert isinstance(result, MspPidNames)
    assert result.names == ()

def test_msp_pidnames_as_serializable():
    """
    Test that MspPidNames.as_serializable returns the correct tuple of names.
    """
    pid_names = MspPidNames(names=("Roll", "Pitch", "Yaw"))

    serializable_data = pid_names.as_serializable()
    
    assert serializable_data == ("Roll", "Pitch", "Yaw")
