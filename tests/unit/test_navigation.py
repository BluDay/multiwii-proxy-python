"""
Test suite generated using ChatGPT-4o mini.

This suite contains various tests for the MspCompGps, MspRawGps, and MspWaypoint classes to ensure 
correct functionality. It covers different edge cases, invalid inputs, and verifies the expected 
behavior of properties, methods, and attributes for parsing and serializing GPS-related data 
from a MultiWii flight controller.
"""

from multiwii.data import (
    Coordinates,
    MspCompGps,
    MspRawGps,
    MspWaypoint
)

import pytest

def test_msp_comp_gps_parse():
    """
    Test that MspCompGps.parse correctly parses a tuple of data values into an MspCompGps instance.
    """
    data = (1000, 45, 1)

    result = MspCompGps.parse(data)
    
    assert isinstance(result, MspCompGps)
    assert result.distance_to_home == 1000
    assert result.direction_to_home == 45
    assert result.update_status == 1

def test_msp_comp_gps_parse_invalid_data():
    """
    Test that MspCompGps.parse raises an error when provided with invalid data (less than 3 elements).
    """
    data = (1000, 45)
    
    with pytest.raises(TypeError):
        MspCompGps.parse(data)

def test_msp_raw_gps_parse():
    """
    Test that MspRawGps.parse correctly parses a tuple of data values into an MspRawGps instance.
    """
    data = (1, 6, 123456789, 987654321, 100, 150, 270)

    result = MspRawGps.parse(data)
    
    assert isinstance(result, MspRawGps)
    assert result.fix == 1
    assert result.satellites == 6
    assert result.coordinates.latitude == 12.3456789
    assert result.coordinates.longitude == 98.7654321
    assert result.altitude == 100
    assert result.speed == [5]
    assert result.ground_course == 27.0

def test_msp_raw_gps_as_serializable():
    """
    Test that MspRawGps.as_serializable returns the correct tuple of serializable values.
    """
    gps = MspRawGps(1, 6, Coordinates(123456789, 987654321), 100, 150, 270)

    serializable_data = gps.as_serializable()
    
    assert isinstance(serializable_data, tuple)
    assert serializable_data == (1, 6, 123456789, 987654321, 100, 150, 2700)

def test_msp_raw_gps_parse_invalid_data():
    """
    Test that MspRawGps.parse raises an error when provided with invalid data (less than 7 elements).
    """
    data = (1, 6, 123456789, 987654321, 100, 150)
    
    with pytest.raises(TypeError):
        MspRawGps.parse(data)

def test_msp_waypoint_parse():
    """
    Test that MspWaypoint.parse correctly parses a tuple of data values into an MspWaypoint instance.
    """
    data = (1, 123456789, 987654321, 100, 90, 60, 1)

    result = MspWaypoint.parse(data)
    
    assert isinstance(result, MspWaypoint)
    assert result.number == 1
    assert result.coordinates.latitude == 12.3456789
    assert result.coordinates.longitude == 98.7654321
    assert result.altitude_hold == 100
    assert result.heading == 90
    assert result.time_to_stay == 60
    assert result.status_flag == 1

def test_msp_waypoint_as_serializable():
    """
    Test that MspWaypoint.as_serializable returns the correct tuple of serializable values.
    """
    waypoint = MspWaypoint(1, Coordinates(123456789, 987654321), 100, 90, 60, 1)

    serializable_data = waypoint.as_serializable()
    
    assert isinstance(serializable_data, tuple)
    assert serializable_data == (1, 123456789, 987654321, 100, 90, 60, 1)

def test_msp_waypoint_parse_invalid_data():
    """
    Test that MspWaypoint.parse raises an error when provided with invalid data (less than 7 elements).
    """
    data = (1, 123456789, 987654321, 100, 90, 60)
    
    with pytest.raises(TypeError):
        MspWaypoint.parse(data)

def test_msp_raw_gps_as_serializable_empty():
    """
    Test that MspRawGps.as_serializable handles an empty instance correctly.
    """
    gps = MspRawGps(0, 0, Coordinates(0, 0), 0, 0, 0)

    serializable_data = gps.as_serializable()
    
    assert serializable_data == (0, 0, 0, 0, 0, 0, 0)

def test_msp_comp_gps_as_serializable_empty():
    """
    Test that MspCompGps.as_serializable handles an empty instance correctly.
    """
    comp_gps = MspCompGps(0, 0, 0)

    serializable_data = comp_gps.as_serializable()
    
    assert serializable_data == (0, 0, 0)

def test_msp_waypoint_as_serializable_empty():
    """
    Test that MspWaypoint.as_serializable handles an empty instance correctly.
    """
    waypoint = MspWaypoint(0, Coordinates(0, 0), 0, 0, 0, 0)

    serializable_data = waypoint.as_serializable()
    
    assert serializable_data == (0, 0, 0, 0, 0, 0, 0)
