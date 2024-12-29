from multiwii.data import MspPid, MspPidNames, Pid

import pytest

@pytest.mark.parametrize(
    "data, expected_values",
    [
        (
            (
                100, 200, 300,
                400, 500, 600,
                700, 800, 900,
                1000, 1100, 1200,
                1300, 1400, 1500,
                1600, 1700, 1800,
                1900, 2000, 2100,
                2200, 2300, 2400,
                2500, 2600, 2700,
                2800, 2900, 3000
            ),
            (
                100, 200, 300,
                400, 500, 600,
                700, 800, 900,
                1000, 1100, 1200,
                1300, 1400, 1500,
                1600, 1700, 1800,
                1900, 2000, 2100,
                2200, 2300, 2400,
                2500, 2600, 2700,
                2800, 2900, 3000
            )
        ),
    ]
)
def test_msp_pid_parse(data, expected_values):
    result = MspPid.parse(data)
    
    assert isinstance(result, MspPid)

    assert result.roll.p == expected_values[0]
    assert result.roll.i == expected_values[1]
    assert result.roll.d == expected_values[2]

    assert result.pitch.p == expected_values[3]
    assert result.pitch.i == expected_values[4]
    assert result.pitch.d == expected_values[5]

    assert result.yaw.p == expected_values[6]
    assert result.yaw.i == expected_values[7]
    assert result.yaw.d == expected_values[8]

@pytest.mark.parametrize(
    "data",
    [
        (100, 200, 300, 400, 500),
    ]
)
def test_msp_pid_parse_invalid_data(data):
    with pytest.raises(TypeError):
        MspPid.parse(data)

@pytest.mark.parametrize(
    "pid_values, expected_serializable",
    [
        (
            (
                100, 200, 300,
                400, 500, 600,
                700, 800, 900,
                1000, 1100, 1200,
                1300, 1400, 1500,
                1600, 1700, 1800,
                1900, 2000, 2100,
                2200, 2300, 2400,
                2500, 2600, 2700,
                2800, 2900, 3000
            ),
            (
                100, 200, 300,
                400, 500, 600,
                700, 800, 900,
                1000, 1100, 1200,
                1300, 1400, 1500,
                1600, 1700, 1800,
                1900, 2000, 2100,
                2200, 2300, 2400,
                2500, 2600, 2700,
                2800, 2900, 3000
            )
        ),
    ]
)
def test_msp_pid_as_serializable(pid_values, expected_serializable):
    pid = MspPid(
        roll=Pid(pid_values[0], pid_values[1], pid_values[2]),
        pitch=Pid(pid_values[3], pid_values[4], pid_values[5]),
        yaw=Pid(pid_values[6], pid_values[7], pid_values[8]),
        altitude_hold=Pid(pid_values[9], pid_values[10], pid_values[11]),
        position_hold=Pid(pid_values[12], pid_values[13], pid_values[14]),
        position_rate=Pid(pid_values[15], pid_values[16], pid_values[17]),
        navigation_rate=Pid(pid_values[18], pid_values[19], pid_values[20]),
        level_mode=Pid(pid_values[21], pid_values[22], pid_values[23]),
        magnetometer=Pid(pid_values[24], pid_values[25], pid_values[26]),
        velocity=Pid(pid_values[27], pid_values[28], pid_values[29])
    )

    serializable_data = pid.as_serializable()
    
    assert isinstance(serializable_data, tuple)
    assert serializable_data == expected_serializable

@pytest.mark.parametrize(
    "pid_values, expected_serializable",
    [
        (
            (
                0, 0, 0,
                0, 0, 0,
                0, 0, 0,
                0, 0, 0,
                0, 0, 0,
                0, 0, 0,
                0, 0, 0,
                0, 0, 0,
                0, 0, 0,
                0, 0, 0,
                0, 0, 0
            ),
            (0,) * 30
        ),
    ]
)
def test_msp_pid_as_serializable_empty(pid_values, expected_serializable):
    pid = MspPid(
        roll=Pid(pid_values[0], pid_values[1], pid_values[2]),
        pitch=Pid(pid_values[3], pid_values[4], pid_values[5]),
        yaw=Pid(pid_values[6], pid_values[7], pid_values[8]),
        altitude_hold=Pid(pid_values[9], pid_values[10], pid_values[11]),
        position_hold=Pid(pid_values[12], pid_values[13], pid_values[14]),
        position_rate=Pid(pid_values[15], pid_values[16], pid_values[17]),
        navigation_rate=Pid(pid_values[18], pid_values[19], pid_values[20]),
        level_mode=Pid(pid_values[21], pid_values[22], pid_values[23]),
        magnetometer=Pid(pid_values[24], pid_values[25], pid_values[26]),
        velocity=Pid(pid_values[27], pid_values[28], pid_values[29])
    )

    serializable_data = pid.as_serializable()
    
    assert serializable_data == expected_serializable

@pytest.mark.parametrize(
    "data, expected_values",
    [
        (
            (b'Roll;Pitch;Yaw;AltitudeHold;PositionHold',),
            ("Roll", "Pitch", "Yaw", "AltitudeHold", "PositionHold")
        ),
    ]
)
def test_msp_pidnames_parse(data, expected_values):
    result = MspPidNames.parse(data)
    
    assert isinstance(result, MspPidNames)
    assert result.names == expected_values

@pytest.mark.parametrize(
    "data",
    [
        (1, 2, 3),
    ]
)
def test_msp_pidnames_parse_invalid_data(data):
    with pytest.raises(TypeError):
        MspPidNames.parse(data)

@pytest.mark.parametrize(
    "data, expected_values",
    [
        (
            (),
            ()
        ),
    ]
)
def test_msp_pidnames_empty(data, expected_values):
    result = MspPidNames.parse(data)
    
    assert isinstance(result, MspPidNames)
    assert result.names == expected_values
