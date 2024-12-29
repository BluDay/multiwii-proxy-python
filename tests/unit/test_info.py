from multiwii.config import (
    MultiWiiCapability,
    MultiWiiMultitype,
    MultiWiiSensor
)

from multiwii.data import (
    MspAnalog,
    MspIdent,
    MspMisc,
    MspSetMisc,
    MspStatus
)

import pytest

@pytest.mark.parametrize("data, expected_values", [
    (
        (120.0, 500, 80, 1500),
        (12.0, 500, 80, 1500)
    ),
    (
        (100.0, 1000, 50, 2000),
        (10.0, 1000, 50, 2000)
    ),
    (
        (50.0, 250, 90, 1000),
        (5.0, 250, 90, 1000)
    )
])
def test_msp_analog_parse(data, expected_values):
    result = MspAnalog.parse(data)

    assert isinstance(result, MspAnalog)
    assert result.voltage == expected_values[0]
    assert result.power_meter_sum == expected_values[1]
    assert result.rssi == expected_values[2]
    assert result.amperage == expected_values[3]

@pytest.mark.parametrize("data, expected_values", [
    (
        (1, 2, 0b101, 3),
        (1, MultiWiiMultitype.TYPE_2, 3)
    ),
    (
        (2, 1, 0b110, 4),
        (2, MultiWiiMultitype.TYPE_1, 4)
    ),
    (
        (3, 4, 0b111, 5),
        (3, MultiWiiMultitype.TYPE_3, 5)
    )
])
def test_msp_ident_parse(data, expected_values):
    result = MspIdent.parse(data)

    assert isinstance(result, MspIdent)
    assert result.version == expected_values[0]
    assert result.multitype == expected_values[1]
    assert len(result.capabilities) == 3
    assert result.navigation_version == expected_values[2]

@pytest.mark.parametrize("data, expected_values", [
    (
        (1, 2, 3, 4, 5, 6, 7, 80, 9, 10, 11, 12),
        (1, 2, 3, 4, 5, 6, 7, 8.0, 9, 1.0, 1.1, 1.2)
    ),
    (
        (10, 20, 30, 40, 50, 60, 70, 160, 90, 100, 110, 120),
        (10, 20, 30, 40, 50, 60, 70, 8.0, 90, 1.0, 1.1, 1.2)
    ),
    (
        (100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200),
        (100, 200, 300, 400, 500, 600, 700, 8.0, 900, 1.0, 1.1, 1.2)
    )
])
def test_msp_misc_parse(data, expected_values):
    result = MspMisc.parse(data)

    assert isinstance(result, MspMisc)
    assert result.power_trigger == expected_values[0]
    assert result.throttle_failsafe == expected_values[1]
    assert result.throttle_idle == expected_values[2]
    assert result.throttle_min == expected_values[3]
    assert result.throttle_max == expected_values[4]
    assert result.power_logger_arm == expected_values[5]
    assert result.power_logger_lifetime == expected_values[6]
    assert result.magnetometer_declination == expected_values[7]
    assert result.battery_scale == expected_values[8]
    assert result.battery_warning_1 == expected_values[9]
    assert result.battery_warning_2 == expected_values[10]
    assert result.battery_critical == expected_values[11]

@pytest.mark.parametrize("misc_data, expected_serializable", [
    (
        (1, 2, 3, 4, 5, 6, 7, 80, 9, 100, 110, 120),
        (1, 2, 3, 4, 5, 6, 7, 80, 9, 100, 110, 120)
    ),
    (
        (10, 20, 30, 40, 50, 60, 70, 160, 90, 100, 110, 120),
        (10, 20, 30, 40, 50, 60, 70, 160, 90, 100, 110, 120)
    ),
    (
        (100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200),
        (100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200)
    )
])
def test_msp_set_misc_as_serializable(misc_data, expected_serializable):
    misc = MspSetMisc(*misc_data)

    serializable_data = misc.as_serializable()

    assert isinstance(serializable_data, tuple)
    assert len(serializable_data) == 12
    assert serializable_data == expected_serializable

@pytest.mark.parametrize("data, expected_values", [
    (
        (1000, 5, 0b1010, 3, 7),
        (1000, 5, 2, 3, 7)
    ),
    (
        (2000, 10, 0b1100, 4, 8),
        (2000, 10, 2, 4, 8)
    ),
    (
        (1500, 8, 0b1110, 5, 6),
        (1500, 8, 3, 5, 6)
    )
])
def test_msp_status_parse(data, expected_values):
    result = MspStatus.parse(data)

    assert isinstance(result, MspStatus)
    assert result.cycle_time == expected_values[0]
    assert result.i2c_errors == expected_values[1]
    assert len(result.sensors) == expected_values[2]
    assert result.status_flag == expected_values[3]
    assert result.global_config == expected_values[4]

@pytest.mark.parametrize("invalid_data", [
    "invalid_data", 
    ("invalid", "data", "tuple"), 
    (1, 2, 3)
])
def test_msp_analog_parse_invalid_data(invalid_data):
    with pytest.raises(TypeError):
        MspAnalog.parse(invalid_data)

@pytest.mark.parametrize("invalid_data", [
    ("invalid", "data", "tuple"),
    ("wrong", "format"),
    (None,)
])
def test_msp_ident_parse_invalid_data(invalid_data):
    with pytest.raises(ValueError):
        MspIdent.parse(invalid_data)

@pytest.mark.parametrize("invalid_data", [
    (1, 2, 3),
    (1, 2),
    (None,)
])
def test_msp_misc_parse_invalid_data(invalid_data):
    with pytest.raises(ValueError):
        MspMisc.parse(invalid_data)

@pytest.mark.parametrize("misc_data", [
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
])
def test_msp_set_misc_as_serializable_empty(misc_data):
    misc = MspSetMisc(*misc_data)

    serializable_data = misc.as_serializable()

    assert serializable_data == misc_data

@pytest.mark.parametrize("invalid_data", [
    ("invalid", "data", "tuple")
])
def test_msp_status_parse_invalid_data(invalid_data):
    with pytest.raises(ValueError):
        MspStatus.parse(invalid_data)
