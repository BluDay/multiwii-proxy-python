from multiwii.data import MspServo, MspServoConf, MspServoConfItem

import pytest

@pytest.mark.parametrize(
    "data, expected_values",
    [
        ((1000, 1500, 2000, 2500), (1000, 1500, 2000, 2500)),
    ]
)
def test_msp_servo_parse(data, expected_values):
    result = MspServo.parse(data)
    
    assert isinstance(result, MspServo)
    
    assert result.values == expected_values

@pytest.mark.parametrize(
    "data",
    [
        (1000, 1500),
    ]
)
def test_msp_servo_parse_invalid_data(data):
    with pytest.raises(TypeError):
        MspServo.parse(data)

@pytest.mark.parametrize(
    "values, expected_serializable",
    [
        ((1000, 1500, 2000, 2500), (1000, 1500, 2000, 2500)),
    ]
)
def test_msp_servo_as_serializable(values, expected_serializable):
    servo = MspServo(values=values)
    
    serializable_data = servo.as_serializable()
    
    assert isinstance(serializable_data, tuple)
    assert serializable_data == expected_serializable

@pytest.mark.parametrize(
    "values, expected_serializable",
    [
        ((), ()),
    ]
)
def test_msp_servo_as_serializable_empty(values, expected_serializable):
    servo = MspServo(values=())
    
    serializable_data = servo.as_serializable()
    
    assert serializable_data == expected_serializable

@pytest.mark.parametrize(
    "data, expected_values",
    [
        (
            (1000, 1500, 2000, 2500, 1100, 1600, 2100, 2600),
            [
                MspServoConfItem(min=1000, max=1500, middle=2000, rate=2500),
                MspServoConfItem(min=1100, max=1600, middle=2100, rate=2600),
            ]
        ),
    ]
)
def test_msp_servo_conf_parse(data, expected_values):
    result = MspServoConf.parse(data)
    
    assert isinstance(result, MspServoConf)
    
    assert len(result.values) == len(expected_values)
    
    for i, item in enumerate(result.values):
        assert item.min == expected_values[i].min
        assert item.max == expected_values[i].max
        assert item.middle == expected_values[i].middle
        assert item.rate == expected_values[i].rate

@pytest.mark.parametrize(
    "data",
    [
        (1000, 1500, 2000, 2500, 1100, 1600),
    ]
)
def test_msp_servo_conf_parse_invalid_data(data):
    with pytest.raises(TypeError):
        MspServoConf.parse(data)

@pytest.mark.parametrize(
    "conf_item_1, conf_item_2, expected_serializable",
    [
        (
            MspServoConfItem(min=1000, max=1500, middle=2000, rate=2500),
            MspServoConfItem(min=1100, max=1600, middle=2100, rate=2600),
            (1000, 1500, 2000, 2500, 1100, 1600, 2100, 2600),
        ),
    ]
)
def test_msp_servo_conf_as_serializable(conf_item_1, conf_item_2, expected_serializable):
    servo_conf = MspServoConf(values=(conf_item_1, conf_item_2))
    
    serializable_data = servo_conf.as_serializable()
    
    assert isinstance(serializable_data, tuple)
    assert serializable_data == expected_serializable

@pytest.mark.parametrize(
    "conf_item, expected_serializable",
    [
        (MspServoConfItem(min=0, max=0, middle=0, rate=0), (0, 0, 0, 0)),
    ]
)
def test_msp_servo_conf_as_serializable_empty(conf_item, expected_serializable):
    servo_conf = MspServoConf(values=(conf_item,))
    
    serializable_data = servo_conf.as_serializable()
    
    assert serializable_data == expected_serializable
