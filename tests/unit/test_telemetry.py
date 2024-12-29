from multiwii.data import MspAltitude, MspAttitude, MspRawImu, Point3D

import pytest

@pytest.mark.parametrize(
    "data, expected_estimation, expected_pressure_variation",
    [
        (
            (12345, 678),
            12345,
            678
        ),
    ]
)
def test_msp_altitude_parse(data, expected_estimation, expected_pressure_variation):
    result = MspAltitude.parse(data)
    
    assert isinstance(result, MspAltitude)
    assert result.estimation == expected_estimation
    assert result.pressure_variation == expected_pressure_variation

@pytest.mark.parametrize(
    "data",
    [
        (12345,),
    ]
)
def test_msp_altitude_parse_invalid_data(data):
    with pytest.raises(TypeError):
        MspAltitude.parse(data)

@pytest.mark.parametrize(
    "data, expected_pitch, expected_roll, expected_yaw",
    [
        (
            (2000, 1500, 0, 180),
            200.0,
            150.0,
            180
        ),
    ]
)
def test_msp_attitude_parse(data, expected_pitch, expected_roll, expected_yaw):
    result = MspAttitude.parse(data)
    
    assert isinstance(result, MspAttitude)
    assert result.pitch_angle == expected_pitch
    assert result.roll_angle == expected_roll
    assert result.yaw_angle == expected_yaw

@pytest.mark.parametrize(
    "data",
    [
        (2000, 1500),
    ]
)
def test_msp_attitude_parse_invalid_data(data):
    with pytest.raises(TypeError):
        MspAttitude.parse(data)

@pytest.mark.parametrize(
    "data, expected_accelerometer, expected_gyroscope, expected_magnetometer",
    [
        (
            (
                1000, 1500, 2000,
                3000, 3500, 4000,
                5000, 5500, 6000
            ),
            Point3D(1000, 1500, 2000),
            Point3D(3000, 3500, 4000),
            Point3D(5000, 5500, 6000),
        ),
    ]
)
def test_msp_raw_imu_parse(data, expected_accelerometer, expected_gyroscope, expected_magnetometer):
    result = MspRawImu.parse(data)
    
    assert isinstance(result, MspRawImu)
    assert result.accelerometer == expected_accelerometer
    assert result.gyroscope == expected_gyroscope
    assert result.magnetometer == expected_magnetometer

@pytest.mark.parametrize(
    "data, expected_accelerometer, expected_gyroscope, expected_magnetometer",
    [
        (
            (
                1000, 1500, 2000,
                3000, 3500, 4000,
                5000, 5500, 6000
            ),
            Point3D(500.0, 750.0, 1000.0),
            Point3D(1500.0, 1750.0, 2000.0),
            Point3D(2500.0, 2750.0, 3000.0),
        ),
    ]
)
def test_msp_raw_imu_parse_with_units(data, expected_accelerometer, expected_gyroscope, expected_magnetometer):
    result = MspRawImu.parse(
        data,
        accelerometer_unit=2.0,
        gyroscope_unit=2.0,
        magnetometer_unit=2.0
    )
    
    assert isinstance(result, MspRawImu)
    assert result.accelerometer == expected_accelerometer
    assert result.gyroscope == expected_gyroscope
    assert result.magnetometer == expected_magnetometer

@pytest.mark.parametrize(
    "data",
    [
        (
            1000, 1500, 2000,
            3000, 3500, 4000,
            5000, 5500
        ),
    ]
)
def test_msp_raw_imu_parse_invalid_data(data):
    with pytest.raises(TypeError):
        MspRawImu.parse(data)
