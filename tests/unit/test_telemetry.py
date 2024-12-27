"""
Test suite generated using ChatGPT-4o mini.

This suite contains various tests for the MspAltitude, MspAttitude, and MspRawImu classes to ensure 
correct functionality. It covers different edge cases, invalid inputs, and verifies the expected 
behavior of properties, methods, and attributes related to altitude, attitude, and raw IMU data 
for the MultiWii flight controller.
"""

from multiwii.data import (
    MspAltitude,
    MspAttitude,
    MspRawImu,
    Point3D
)

import pytest

def test_msp_altitude_parse():
    """
    Test parsing of the MSP_ALTITUDE command data.
    
    This test ensures that the `MspAltitude.parse()` method correctly parses
    a tuple of altitude-related data and creates an instance of `MspAltitude`.
    """
    data = (12345, 678)

    result = MspAltitude.parse(data)

    assert isinstance(result, MspAltitude)
    assert result.estimation == 12345
    assert result.pressure_variation == 678

def test_msp_altitude_parse_invalid_data():
    """
    Test invalid data input to the `MspAltitude.parse()` method.
    
    This test ensures that the method raises a TypeError when given
    insufficient data (less than expected number of values).
    """
    data = (12345,)

    with pytest.raises(TypeError):
        MspAltitude.parse(data)

def test_msp_attitude_parse():
    """
    Test parsing of the MSP_ATTITUDE command data.

    This test ensures that the `MspAttitude.parse()` method correctly parses
    a tuple of attitude-related data and creates an instance of `MspAttitude`.
    """
    data = (2000, 1500, 0, 180)
    
    result = MspAttitude.parse(data)
    
    assert isinstance(result, MspAttitude)
    assert result.pitch_angle == 200.0
    assert result.roll_angle == 150.0
    assert result.yaw_angle == 180

def test_msp_attitude_parse_invalid_data():
    """
    Test invalid data input to the `MspAttitude.parse()` method.

    This test ensures that the method raises a TypeError when given
    insufficient data (less than expected number of values).
    """
    data = (2000, 1500)

    with pytest.raises(TypeError):
        MspAttitude.parse(data)

def test_msp_raw_imu_parse():
    """
    Test parsing of the MSP_RAW_IMU command data.

    This test ensures that the `MspRawImu.parse()` method correctly parses
    a tuple of IMU-related data and creates an instance of `MspRawImu`.
    """
    data = (
        1000, 1500, 2000, 3000, 3500, 4000, 5000, 5500, 6000
    )

    result = MspRawImu.parse(data)

    assert isinstance(result, MspRawImu)
    
    assert isinstance(result.accelerometer, Point3D)
    assert result.accelerometer.x == 1000
    assert result.accelerometer.y == 1500
    assert result.accelerometer.z == 2000
    
    assert isinstance(result.gyroscope, Point3D)
    assert result.gyroscope.x == 3000
    assert result.gyroscope.y == 3500
    assert result.gyroscope.z == 4000

    assert isinstance(result.magnetometer, Point3D)
    assert result.magnetometer.x == 5000
    assert result.magnetometer.y == 5500
    assert result.magnetometer.z == 6000

def test_msp_raw_imu_parse_with_units():
    """
    Test parsing of the MSP_RAW_IMU command data with unit conversion.

    This test ensures that the `MspRawImu.parse()` method handles unit 
    conversion for accelerometer, gyroscope, and magnetometer correctly.
    """
    data = (
        1000, 1500, 2000, 3000, 3500, 4000, 5000, 5500, 6000
    )

    result = MspRawImu.parse(
        data,
        accelerometer_unit=2.0,
        gyroscope_unit=2.0,
        magnetometer_unit=2.0
    )

    assert isinstance(result, MspRawImu)
    assert isinstance(result.accelerometer, Point3D)
    assert result.accelerometer.x == 500.0  # 1000 / 2.0
    assert result.accelerometer.y == 750.0  # 1500 / 2.0
    assert result.accelerometer.z == 1000.0  # 2000 / 2.0
    assert isinstance(result.gyroscope, Point3D)
    assert result.gyroscope.x == 1500.0  # 3000 / 2.0
    assert result.gyroscope.y == 1750.0  # 3500 / 2.0
    assert result.gyroscope.z == 2000.0  # 4000 / 2.0
    assert isinstance(result.magnetometer, Point3D)
    assert result.magnetometer.x == 2500.0  # 5000 / 2.0
    assert result.magnetometer.y == 2750.0  # 5500 / 2.0
    assert result.magnetometer.z == 3000.0  # 6000 / 2.0

def test_msp_raw_imu_parse_invalid_data():
    """
    Test invalid data input to the `MspRawImu.parse()` method.

    This test ensures that the method raises a TypeError when given
    insufficient data (less than expected number of values).
    """
    data = (
        1000, 1500, 2000, 3000, 3500, 4000, 5000, 5500
    )

    with pytest.raises(TypeError):
        MspRawImu.parse(data)
