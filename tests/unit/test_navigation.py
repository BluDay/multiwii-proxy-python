from multiwii.data import (
    Coordinates,
    MspCompGps,
    MspRawGps,
    MspWaypoint
)

import pytest

@pytest.mark.parametrize(
    "data, expected_values",
    [
        (
            (1000, 45, 1),
            (1000, 45, 1)
        ),
    ]
)
def test_msp_comp_gps_parse(data, expected_values):
    result = MspCompGps.parse(data)
    
    assert isinstance(result, MspCompGps)
    assert result.distance_to_home == expected_values[0]
    assert result.direction_to_home == expected_values[1]
    assert result.update_status == expected_values[2]

@pytest.mark.parametrize(
    "data",
    [
        (1000, 45),
    ]
)
def test_msp_comp_gps_parse_invalid_data(data):
    with pytest.raises(TypeError):
        MspCompGps.parse(data)

@pytest.mark.parametrize(
    "data, expected_values",
    [
        (
            (1, 6, 123456789, 987654321, 100, 150, 270),
            (1, 6, 12.3456789, 98.7654321, 100, [5], 27.0)
        ),
    ]
)
def test_msp_raw_gps_parse(data, expected_values):
    result = MspRawGps.parse(data)
    
    assert isinstance(result, MspRawGps)
    assert result.fix == expected_values[0]
    assert result.satellites == expected_values[1]
    assert result.coordinates.latitude == expected_values[2]
    assert result.coordinates.longitude == expected_values[3]
    assert result.altitude == expected_values[4]
    assert result.speed == expected_values[5]
    assert result.ground_course == expected_values[6]

@pytest.mark.parametrize(
    "gps_values, expected_serializable",
    [
        (
            MspRawGps(1, 6, Coordinates(123456789, 987654321), 100, 150, 270),
            (1, 6, 123456789, 987654321, 100, 150, 2700)
        ),
    ]
)
def test_msp_raw_gps_as_serializable(gps_values, expected_serializable):
    serializable_data = gps_values.as_serializable()
    
    assert isinstance(serializable_data, tuple)
    assert serializable_data == expected_serializable

@pytest.mark.parametrize(
    "data",
    [
        (1, 6, 123456789, 987654321, 100, 150),
    ]
)
def test_msp_raw_gps_parse_invalid_data(data):
    with pytest.raises(TypeError):
        MspRawGps.parse(data)

@pytest.mark.parametrize(
    "data, expected_values",
    [
        (
            (1, 123456789, 987654321, 100, 90, 60, 1),
            (1, 12.3456789, 98.7654321, 100, 90, 60, 1)
        ),
    ]
)
def test_msp_waypoint_parse(data, expected_values):
    result = MspWaypoint.parse(data)
    
    assert isinstance(result, MspWaypoint)
    assert result.number == expected_values[0]
    assert result.coordinates.latitude == expected_values[1]
    assert result.coordinates.longitude == expected_values[2]
    assert result.altitude_hold == expected_values[3]
    assert result.heading == expected_values[4]
    assert result.time_to_stay == expected_values[5]
    assert result.status_flag == expected_values[6]

@pytest.mark.parametrize(
    "waypoint_values, expected_serializable",
    [
        (
            MspWaypoint(1, Coordinates(123456789, 987654321), 100, 90, 60, 1),
            (1, 123456789, 987654321, 100, 90, 60, 1)
        ),
    ]
)
def test_msp_waypoint_as_serializable(waypoint_values, expected_serializable):
    serializable_data = waypoint_values.as_serializable()
    
    assert isinstance(serializable_data, tuple)
    assert serializable_data == expected_serializable

@pytest.mark.parametrize(
    "data",
    [
        (1, 123456789, 987654321, 100, 90, 60),
    ]
)
def test_msp_waypoint_parse_invalid_data(data):
    with pytest.raises(TypeError):
        MspWaypoint.parse(data)

@pytest.mark.parametrize(
    "gps_values, expected_serializable",
    [
        (
            MspRawGps(0, 0, Coordinates(0, 0), 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0)
        ),
    ]
)
def test_msp_raw_gps_as_serializable_empty(gps_values, expected_serializable):
    serializable_data = gps_values.as_serializable()
    
    assert serializable_data == expected_serializable

@pytest.mark.parametrize(
    "comp_gps_values, expected_serializable",
    [
        (
            MspCompGps(0, 0, 0),
            (0, 0, 0)
        ),
    ]
)
def test_msp_comp_gps_as_serializable_empty(comp_gps_values, expected_serializable):
    serializable_data = comp_gps_values.as_serializable()
    
    assert serializable_data == expected_serializable

@pytest.mark.parametrize(
    "waypoint_values, expected_serializable",
    [
        (
            MspWaypoint(0, Coordinates(0, 0), 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0)
        ),
    ]
)
def test_msp_waypoint_as_serializable_empty(waypoint_values, expected_serializable):
    serializable_data = waypoint_values.as_serializable()
    
    assert serializable_data == expected_serializable
