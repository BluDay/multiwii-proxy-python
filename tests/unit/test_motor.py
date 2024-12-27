"""
Test suite generated using ChatGPT-4o mini.

This suite contains various tests for the MspMotor and MspMotorPins classes to ensure correct 
functionality. It covers different edge cases, invalid inputs, and verifies the expected 
behavior of properties, methods, and attributes for parsing and serializing motor-related data 
from a MultiWii flight controller.
"""

from multiwii.data import MspMotor, MspMotorPins

import pytest

def test_msp_motor_parse():
    """
    Test that MspMotor.parse correctly parses a tuple of data values into an MspMotor instance.
    """
    data = (1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800)

    result = MspMotor.parse(data)
    
    assert isinstance(result, MspMotor)
    assert result.motor1 == 1000
    assert result.motor2 == 1200
    assert result.motor3 == 1300
    assert result.motor4 == 1400
    assert result.motor5 == 1500
    assert result.motor6 == 1600
    assert result.motor7 == 1700
    assert result.motor8 == 1800

def test_msp_motor_as_serializable():
    """
    Test that MspMotor.as_serializable returns the correct tuple of motor speed values.
    """
    motor = MspMotor(1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800)

    serializable_data = motor.as_serializable()
    
    assert isinstance(serializable_data, tuple)
    assert serializable_data == (1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800)

def test_msp_motor_parse_invalid_data():
    """
    Test that MspMotor.parse raises an error when provided with invalid data (less than 8 elements).
    """
    data = (1000, 1200, 1300, 1400, 1500)
    
    with pytest.raises(TypeError):
        MspMotor.parse(data)

def test_msp_motor_pins_parse():
    """
    Test that MspMotorPins.parse correctly parses a tuple of data values into an MspMotorPins instance.
    """
    data = (1, 2, 3, 4, 5, 6, 7, 8)

    result = MspMotorPins.parse(data)
    
    assert isinstance(result, MspMotorPins)
    assert result.motor1 == 1
    assert result.motor2 == 2
    assert result.motor3 == 3
    assert result.motor4 == 4
    assert result.motor5 == 5
    assert result.motor6 == 6
    assert result.motor7 == 7
    assert result.motor8 == 8

def test_msp_motor_pins_as_serializable():
    """
    Test that MspMotorPins.as_serializable returns the correct tuple of motor pin values.
    """
    motor_pins = MspMotorPins(1, 2, 3, 4, 5, 6, 7, 8)

    serializable_data = motor_pins.as_serializable()
    
    assert isinstance(serializable_data, tuple)
    assert serializable_data == (1, 2, 3, 4, 5, 6, 7, 8)

def test_msp_motor_pins_parse_invalid_data():
    """
    Test that MspMotorPins.parse raises an error when provided with invalid data (less than 8 elements).
    """
    data = (1, 2, 3, 4, 5)
    
    with pytest.raises(TypeError):
        MspMotorPins.parse(data)

def test_msp_motor_as_serializable_empty():
    """
    Test that MspMotor.as_serializable handles an empty instance correctly.
    """
    motor = MspMotor(0, 0, 0, 0, 0, 0, 0, 0)

    serializable_data = motor.as_serializable()
    
    assert serializable_data == (0, 0, 0, 0, 0, 0, 0, 0)

def test_msp_motor_pins_as_serializable_empty():
    """
    Test that MspMotorPins.as_serializable handles an empty instance correctly.
    """
    motor_pins = MspMotorPins(0, 0, 0, 0, 0, 0, 0, 0)

    serializable_data = motor_pins.as_serializable()
    
    assert serializable_data == (0, 0, 0, 0, 0, 0, 0, 0)
