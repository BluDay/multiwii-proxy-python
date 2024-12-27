"""
Test suite for the MspRc and MspRcTuning classes.

This suite tests the functionality of the MspRc and MspRcTuning classes, ensuring correct parsing,
serialization, and handling of RC values and tuning parameters in the MultiWii flight controller.
"""

from multiwii.data import MspRc, MspRcTuning

import pytest

def test_msp_rc_parse():
    """
    Test that MspRc.parse correctly parses a tuple of data values into an MspRc instance.
    """
    data = (
        1000, 2000, 1500, 1200, 1800, 1600, 1400, 1300
    )

    result = MspRc.parse(data)
    
    assert isinstance(result, MspRc)
    assert result.roll == 1000
    assert result.pitch == 2000
    assert result.yaw == 1500
    assert result.throttle == 1200
    assert result.aux1 == 1800
    assert result.aux2 == 1600
    assert result.aux3 == 1400
    assert result.aux4 == 1300

def test_msp_rc_parse_invalid_data():
    """
    Test that MspRc.parse raises an error when provided with invalid data (less than required number of elements).
    """
    data = (
        1000, 2000, 1500, 1200, 1800  # Invalid length (5 values)
    )
    
    with pytest.raises(TypeError):
        MspRc.parse(data)

def test_msp_rc_as_serializable():
    """
    Test that MspRc.as_serializable returns the correct tuple of serializable values.
    """
    rc = MspRc(
        roll=1000,
        pitch=2000,
        yaw=1500,
        throttle=1200,
        aux1=1800,
        aux2=1600,
        aux3=1400,
        aux4=1300
    )

    serializable_data = rc.as_serializable()
    
    assert isinstance(serializable_data, tuple)
    assert serializable_data == (
        1000, 2000, 1500, 1200, 1800, 1600, 1400, 1300
    )

def test_msp_rc_as_serializable_empty():
    """
    Test that MspRc.as_serializable handles an empty instance correctly.
    """
    rc = MspRc(
        roll=0,
        pitch=0,
        yaw=0,
        throttle=0,
        aux1=0,
        aux2=0,
        aux3=0,
        aux4=0
    )

    serializable_data = rc.as_serializable()
    
    assert serializable_data == (0, 0, 0, 0, 0, 0, 0, 0)

def test_msp_rc_tuning_parse():
    """
    Test that MspRcTuning.parse correctly parses a tuple of data values into an MspRcTuning instance.
    """
    data = (
        100, 200, 300, 400, 500, 600, 700
    )

    result = MspRcTuning.parse(data)
    
    assert isinstance(result, MspRcTuning)
    assert result.rate == 100
    assert result.expo == 200
    assert result.roll_pitch_rate == 300
    assert result.yaw_rate == 400
    assert result.dynamic_throttle_pid == 500
    assert result.throttle_mid == 600
    assert result.throttle_expo == 700

def test_msp_rc_tuning_parse_invalid_data():
    """
    Test that MspRcTuning.parse raises an error when provided with invalid data (less than required number of elements).
    """
    data = (
        100, 200, 300, 400, 500  # Invalid length (5 values)
    )
    
    with pytest.raises(TypeError):
        MspRcTuning.parse(data)

def test_msp_rc_tuning_as_serializable():
    """
    Test that MspRcTuning.as_serializable returns the correct tuple of serializable values.
    """
    rc_tuning = MspRcTuning(
        rate=100,
        expo=200,
        roll_pitch_rate=300,
        yaw_rate=400,
        dynamic_throttle_pid=500,
        throttle_mid=600,
        throttle_expo=700
    )

    serializable_data = rc_tuning.as_serializable()
    
    assert isinstance(serializable_data, tuple)
    assert serializable_data == (
        100, 200, 300, 400, 500, 600, 700
    )

def test_msp_rc_tuning_as_serializable_empty():
    """
    Test that MspRcTuning.as_serializable handles an empty instance correctly.
    """
    rc_tuning = MspRcTuning(
        rate=0,
        expo=0,
        roll_pitch_rate=0,
        yaw_rate=0,
        dynamic_throttle_pid=0,
        throttle_mid=0,
        throttle_expo=0
    )

    serializable_data = rc_tuning.as_serializable()
    
    assert serializable_data == (0, 0, 0, 0, 0, 0, 0)
