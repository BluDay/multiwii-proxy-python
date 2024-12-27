"""
Test suite generated using ChatGPT-4o mini.

This suite contains various tests for the MspServo and MspServoConf classes to ensure 
correct functionality. It covers different edge cases, invalid inputs, and verifies 
the expected behavior of properties, methods, and attributes related to servo and 
servo configuration commands for the MultiWii flight controller.
"""

from multiwii.data import (
    MspServo,
    MspServoConf,
    MspServoConfItem
)

import pytest

def test_msp_servo_parse():
    """
    Test parsing of the MSP_SERVO command data.
    This test ensures that the `MspServo.parse()` method correctly
    parses a tuple of servo values and creates an instance of `MspServo`.
    """
    # Test data for the servo values
    data = (1000, 1500, 2000, 2500)
    
    # Parse the data using the `parse` class method
    result = MspServo.parse(data)
    
    # Ensure the result is an instance of MspServo
    assert isinstance(result, MspServo)
    # Ensure the parsed values match the expected input data
    assert result.values == (1000, 1500, 2000, 2500)

def test_msp_servo_parse_invalid_data():
    """
    Test invalid data input to the `MspServo.parse()` method.
    This test ensures that the method raises a TypeError when given
    insufficient data (less than expected number of values).
    """
    # Invalid data with fewer than expected values
    data = (1000, 1500)
    
    # Ensure that a TypeError is raised when parsing the invalid data
    with pytest.raises(TypeError):
        MspServo.parse(data)

def test_msp_servo_as_serializable():
    """
    Test the `as_serializable()` method of the `MspServo` class.
    This test ensures that the `MspServo` instance can be correctly
    serialized into a tuple of integer values.
    """
    # Create an instance of MspServo with specific values
    servo = MspServo(values=(1000, 1500, 2000, 2500))
    
    # Serialize the instance to tuple
    serializable_data = servo.as_serializable()
    
    # Ensure the serialized data matches the original values
    assert isinstance(serializable_data, tuple)
    assert serializable_data == (1000, 1500, 2000, 2500)

def test_msp_servo_as_serializable_empty():
    """
    Test the `as_serializable()` method with an empty `MspServo` instance.
    This ensures that the method can handle empty configurations correctly.
    """
    # Create an empty MspServo instance
    servo = MspServo(values=())
    
    # Serialize the empty instance
    serializable_data = servo.as_serializable()
    
    # Ensure the serialized data is an empty tuple
    assert serializable_data == ()

def test_msp_servo_conf_parse():
    """
    Test parsing of the MSP_SERVO_CONF command data.
    This test ensures that the `MspServoConf.parse()` method correctly
    parses a tuple of servo configuration values and creates an instance
    of `MspServoConf`.
    """
    # Test data for the servo configuration values
    data = (1000, 1500, 2000, 2500, 1100, 1600, 2100, 2600)
    
    # Parse the data using the `parse` class method
    result = MspServoConf.parse(data)
    
    # Ensure the result is an instance of MspServoConf
    assert isinstance(result, MspServoConf)
    # Ensure the number of servo configuration items is as expected
    assert len(result.values) == 2
    # Ensure the first item has the expected values
    assert result.values[0].min == 1000
    assert result.values[0].max == 1500
    assert result.values[0].middle == 2000
    assert result.values[0].rate == 2500
    # Ensure the second item has the expected values
    assert result.values[1].min == 1100
    assert result.values[1].max == 1600
    assert result.values[1].middle == 2100
    assert result.values[1].rate == 2600

def test_msp_servo_conf_parse_invalid_data():
    """
    Test invalid data input to the `MspServoConf.parse()` method.
    This test ensures that the method raises a TypeError when given
    insufficient data for parsing.
    """
    # Invalid data with fewer than expected values (not enough for a full configuration)
    data = (1000, 1500, 2000, 2500, 1100, 1600)
    
    # Ensure that a TypeError is raised when parsing the invalid data
    with pytest.raises(TypeError):
        MspServoConf.parse(data)

def test_msp_servo_conf_as_serializable():
    """
    Test the `as_serializable()` method of the `MspServoConf` class.
    This test ensures that the `MspServoConf` instance can be correctly
    serialized into a tuple of integer values.
    """
    # Create two configuration items for testing
    conf_item_1 = MspServoConfItem(min=1000, max=1500, middle=2000, rate=2500)
    conf_item_2 = MspServoConfItem(min=1100, max=1600, middle=2100, rate=2600)
    
    # Create an instance of MspServoConf with the configuration items
    servo_conf = MspServoConf(values=(conf_item_1, conf_item_2))
    
    # Serialize the instance to tuple
    serializable_data = servo_conf.as_serializable()
    
    # Ensure the serialized data matches the expected tuple of values
    assert isinstance(serializable_data, tuple)
    assert serializable_data == (
        1000, 1500, 2000, 2500, 1100, 1600, 2100, 2600
    )

def test_msp_servo_conf_as_serializable_empty():
    """
    Test the `as_serializable()` method with an empty `MspServoConf` instance.
    This ensures that the method can handle empty servo configurations correctly.
    """
    # Create an empty MspServoConf instance
    conf_item_1 = MspServoConfItem(min=0, max=0, middle=0, rate=0)
    servo_conf = MspServoConf(values=(conf_item_1,))
    
    # Serialize the empty instance
    serializable_data = servo_conf.as_serializable()
    
    # Ensure the serialized data is the expected tuple for empty configuration
    assert serializable_data == (0, 0, 0, 0)
