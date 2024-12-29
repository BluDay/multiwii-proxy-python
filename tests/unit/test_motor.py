from multiwii.data import MspMotor, MspMotorPins

import pytest

@pytest.mark.parametrize("data, expected_motor_values", [
    (
        (1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800),
        (1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800)
    ),
    (
        (2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700),
        (2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700)
    ),
    (
        (3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700),
        (3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700)
    )
])
def test_msp_motor_parse(data, expected_motor_values):
    result = MspMotor.parse(data)
    
    assert isinstance(result, MspMotor)
    assert result.motor1 == expected_motor_values[0]
    assert result.motor2 == expected_motor_values[1]
    assert result.motor3 == expected_motor_values[2]
    assert result.motor4 == expected_motor_values[3]
    assert result.motor5 == expected_motor_values[4]
    assert result.motor6 == expected_motor_values[5]
    assert result.motor7 == expected_motor_values[6]
    assert result.motor8 == expected_motor_values[7]

@pytest.mark.parametrize("motor_data, expected_serializable", [
    (
        (1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800),
        (1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800)
    ),
    (
        (2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700),
        (2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700)
    ),
    (
        (3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700),
        (3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700)
    )
])
def test_msp_motor_as_serializable(motor_data, expected_serializable):
    motor = MspMotor(*motor_data)

    serializable_data = motor.as_serializable()
    
    assert isinstance(serializable_data, tuple)
    assert serializable_data == expected_serializable

@pytest.mark.parametrize("invalid_data", [
    (1000, 1200, 1300, 1400, 1500),
    (1000, 1200),
    (1000, 1200, 1300, 1400),
    (1000,)
])
def test_msp_motor_parse_invalid_data(invalid_data):
    with pytest.raises(TypeError):
        MspMotor.parse(invalid_data)

@pytest.mark.parametrize("data, expected_motor_pin_values", [
    (
        (1, 2, 3, 4, 5, 6, 7, 8),
        (1, 2, 3, 4, 5, 6, 7, 8)
    ),
    (
        (9, 10, 11, 12, 13, 14, 15, 16),
        (9, 10, 11, 12, 13, 14, 15, 16)
    ),
    (
        (17, 18, 19, 20, 21, 22, 23, 24),
        (17, 18, 19, 20, 21, 22, 23, 24)
    )
])
def test_msp_motor_pins_parse(data, expected_motor_pin_values):
    result = MspMotorPins.parse(data)
    
    assert isinstance(result, MspMotorPins)
    assert result.motor1 == expected_motor_pin_values[0]
    assert result.motor2 == expected_motor_pin_values[1]
    assert result.motor3 == expected_motor_pin_values[2]
    assert result.motor4 == expected_motor_pin_values[3]
    assert result.motor5 == expected_motor_pin_values[4]
    assert result.motor6 == expected_motor_pin_values[5]
    assert result.motor7 == expected_motor_pin_values[6]
    assert result.motor8 == expected_motor_pin_values[7]

@pytest.mark.parametrize("motor_pin_data, expected_serializable", [
    (
        (1, 2, 3, 4, 5, 6, 7, 8),
        (1, 2, 3, 4, 5, 6, 7, 8)
    ),
    (
        (9, 10, 11, 12, 13, 14, 15, 16),
        (9, 10, 11, 12, 13, 14, 15, 16)
    ),
    (
        (17, 18, 19, 20, 21, 22, 23, 24),
        (17, 18, 19, 20, 21, 22, 23, 24)
    )
])
def test_msp_motor_pins_as_serializable(motor_pin_data, expected_serializable):
    motor_pins = MspMotorPins(*motor_pin_data)

    serializable_data = motor_pins.as_serializable()
    
    assert isinstance(serializable_data, tuple)
    assert serializable_data == expected_serializable

@pytest.mark.parametrize("invalid_pin_data", [
    (1, 2, 3, 4, 5),
    (1, 2),
    (1, 2, 3, 4),
    (1,)
])
def test_msp_motor_pins_parse_invalid_data(invalid_pin_data):
    with pytest.raises(TypeError):
        MspMotorPins.parse(invalid_pin_data)

@pytest.mark.parametrize("motor_data, expected_serializable", [
    (
        (0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0)
    ),
])
def test_msp_motor_as_serializable_empty(motor_data, expected_serializable):
    motor = MspMotor(*motor_data)

    serializable_data = motor.as_serializable()
    
    assert serializable_data == expected_serializable

@pytest.mark.parametrize("motor_pin_data, expected_serializable", [
    (
        (0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0)
    ),
])
def test_msp_motor_pins_as_serializable_empty(motor_pin_data, expected_serializable):
    motor_pins = MspMotorPins(*motor_pin_data)

    serializable_data = motor_pins.as_serializable()
    
    assert serializable_data == expected_serializable
