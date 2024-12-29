from multiwii.data import MspRc, MspRcTuning

import pytest

@pytest.mark.parametrize(
    "data, expected_values",
    [
        (
            (1000, 2000, 1500, 1200, 1800, 1600, 1400, 1300),
            (1000, 2000, 1500, 1200, 1800, 1600, 1400, 1300),
        ),
    ]
)
def test_msp_rc_parse(data, expected_values):
    result = MspRc.parse(data)
    
    assert isinstance(result, MspRc)
    assert result.roll == expected_values[0]
    assert result.pitch == expected_values[1]
    assert result.yaw == expected_values[2]
    assert result.throttle == expected_values[3]
    assert result.aux1 == expected_values[4]
    assert result.aux2 == expected_values[5]
    assert result.aux3 == expected_values[6]
    assert result.aux4 == expected_values[7]

@pytest.mark.parametrize(
    "data",
    [
        (1000, 2000, 1500, 1200, 1800),
    ]
)
def test_msp_rc_parse_invalid_data(data):
    with pytest.raises(TypeError):
        MspRc.parse(data)

@pytest.mark.parametrize(
    "rc_values, expected_serializable",
    [
        (
            (1000, 2000, 1500, 1200, 1800, 1600, 1400, 1300),
            (1000, 2000, 1500, 1200, 1800, 1600, 1400, 1300),
        ),
    ]
)
def test_msp_rc_as_serializable(rc_values, expected_serializable):
    rc = MspRc(
        roll=rc_values[0],
        pitch=rc_values[1],
        yaw=rc_values[2],
        throttle=rc_values[3],
        aux1=rc_values[4],
        aux2=rc_values[5],
        aux3=rc_values[6],
        aux4=rc_values[7]
    )

    serializable_data = rc.as_serializable()
    
    assert isinstance(serializable_data, tuple)
    assert serializable_data == expected_serializable

@pytest.mark.parametrize(
    "rc_values, expected_serializable",
    [
        (
            (0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0),
        ),
    ]
)
def test_msp_rc_as_serializable_empty(rc_values, expected_serializable):
    rc = MspRc(
        roll=rc_values[0],
        pitch=rc_values[1],
        yaw=rc_values[2],
        throttle=rc_values[3],
        aux1=rc_values[4],
        aux2=rc_values[5],
        aux3=rc_values[6],
        aux4=rc_values[7]
    )

    serializable_data = rc.as_serializable()
    
    assert serializable_data == expected_serializable

@pytest.mark.parametrize(
    "data, expected_values",
    [
        (
            (100, 200, 300, 400, 500, 600, 700),
            [
                100, 200, 300, 400, 500, 600, 700
            ]
        ),
    ]
)
def test_msp_rc_tuning_parse(data, expected_values):
    result = MspRcTuning.parse(data)
    
    assert isinstance(result, MspRcTuning)
    assert result.rate == expected_values[0]
    assert result.expo == expected_values[1]
    assert result.roll_pitch_rate == expected_values[2]
    assert result.yaw_rate == expected_values[3]
    assert result.dynamic_throttle_pid == expected_values[4]
    assert result.throttle_mid == expected_values[5]
    assert result.throttle_expo == expected_values[6]

@pytest.mark.parametrize(
    "data",
    [
        (100, 200, 300, 400, 500),
    ]
)
def test_msp_rc_tuning_parse_invalid_data(data):
    with pytest.raises(TypeError):
        MspRcTuning.parse(data)

@pytest.mark.parametrize(
    "tuning_values, expected_serializable",
    [
        (
            (100, 200, 300, 400, 500, 600, 700),
            (100, 200, 300, 400, 500, 600, 700),
        ),
    ]
)
def test_msp_rc_tuning_as_serializable(tuning_values, expected_serializable):
    rc_tuning = MspRcTuning(
        rate=tuning_values[0],
        expo=tuning_values[1],
        roll_pitch_rate=tuning_values[2],
        yaw_rate=tuning_values[3],
        dynamic_throttle_pid=tuning_values[4],
        throttle_mid=tuning_values[5],
        throttle_expo=tuning_values[6]
    )

    serializable_data = rc_tuning.as_serializable()
    
    assert isinstance(serializable_data, tuple)
    assert serializable_data == expected_serializable

@pytest.mark.parametrize(
    "tuning_values, expected_serializable",
    [
        (
            (0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0),
        ),
    ]
)
def test_msp_rc_tuning_as_serializable_empty(tuning_values, expected_serializable):
    rc_tuning = MspRcTuning(
        rate=tuning_values[0],
        expo=tuning_values[1],
        roll_pitch_rate=tuning_values[2],
        yaw_rate=tuning_values[3],
        dynamic_throttle_pid=tuning_values[4],
        throttle_mid=tuning_values[5],
        throttle_expo=tuning_values[6]
    )

    serializable_data = rc_tuning.as_serializable()
    
    assert serializable_data == expected_serializable
