from multiwii import _MspCommand
from struct   import error as StructError

import pytest

@pytest.mark.parametrize("code, data_format, expected_code, expected_data_field_count, expected_data_size, expected_has_variable_size", [
    (150, 'B:1:?', 150, 1, 1, True)
])
def test_valid_code_and_format(code, data_format, expected_code, expected_data_field_count, expected_data_size, expected_has_variable_size):
    command = _MspCommand(code, data_format)

    assert command.code == expected_code
    assert command.data_field_count == expected_data_field_count
    assert command.data_size == expected_data_size
    assert command.has_variable_size == expected_has_variable_size

@pytest.mark.parametrize("invalid_code", [99, 251])
def test_invalid_code(invalid_code):
    with pytest.raises(ValueError):
        _MspCommand(invalid_code, 'B:1:?')

def test_invalid_format_string():
    with pytest.raises(ValueError):
        _MspCommand(150, 'B:1')

    with pytest.raises(StructError):
        _MspCommand(150, 'X:1:?')

@pytest.mark.parametrize("code", [100, 250])
def test_edge_case_code(code):
    command = _MspCommand(code, 'B:1:?')

    assert command.code == code

@pytest.mark.parametrize("data_format, expected_data_field_count, expected_data_size", [
    (None, 0, 0)
])
def test_empty_data_format(data_format, expected_data_field_count, expected_data_size):
    command = _MspCommand(150, data_format)

    assert command.data_field_count == expected_data_field_count
    assert command.data_size == expected_data_size

@pytest.mark.parametrize("code, expected_code", [
    (150, 150)
])
def test_code_property(code, expected_code):
    command = _MspCommand(code, 'B:1:?')

    assert command.code == expected_code

@pytest.mark.parametrize("data_format, expected_data_field_count", [
    ('B:2:? ', 2)
])
def test_data_field_count_property(data_format, expected_data_field_count):
    command = _MspCommand(150, data_format)

    assert command.data_field_count == expected_data_field_count

@pytest.mark.parametrize("data_format, expected_data_size", [
    ('B:1:? ', 1)
])
def test_data_size_property(data_format, expected_data_size):
    command = _MspCommand(150, data_format)

    assert command.data_size == expected_data_size

@pytest.mark.parametrize("data_format, expected_data_struct_format", [
    ('B:1:? ', 'B')
])
def test_data_struct_format_property(data_format, expected_data_struct_format):
    command = _MspCommand(150, data_format)

    assert command.data_struct_format == expected_data_struct_format

@pytest.mark.parametrize("data_format, expected_has_variable_size", [
    ('B:1:', False),
    ('B:1:?', True)
])
def test_has_variable_size_property(data_format, expected_has_variable_size):
    command = _MspCommand(150, data_format)

    assert command.has_variable_size == expected_has_variable_size

@pytest.mark.parametrize("code, data_format, expected_is_set_command", [
    (200, 'B:1:?', True),
    (150, 'B:1:?', False)
])
def test_is_set_command_property(code, data_format, expected_is_set_command):
    command = _MspCommand(code, data_format)

    assert command.is_set_command == expected_is_set_command

@pytest.mark.parametrize("data_format, expected_payload_struct_format", [
    ('B:1:? ', '<2BB')
])
def test_payload_struct_format_property(data_format, expected_payload_struct_format):
    command = _MspCommand(150, data_format)

    assert command.payload_struct_format == expected_payload_struct_format

@pytest.mark.parametrize("code, data_format, expected_int", [
    (150, 'B:1:? ', 150)
])
def test_int_method(code, data_format, expected_int):
    command = _MspCommand(code, data_format)

    assert int(command) == expected_int

@pytest.mark.parametrize("code, data_format", [
    (150, 'B:1:?')
])
def test_repr_method(code, data_format):
    command = _MspCommand(code, data_format)

    repr_str = repr(command)

    assert '<150' in repr_str
    assert '1' in repr_str
    assert '!' in repr_str

@pytest.mark.parametrize("code, data_format", [
    (150, 'B:1:?')
])
def test_str_method(code, data_format):
    command = _MspCommand(code, data_format)

    assert str(command) == 'B'

@pytest.mark.parametrize("code", [100, 250])
def test_code_boundaries(code):
    command = _MspCommand(code, 'B:1:?')

    assert command.code == code

@pytest.mark.parametrize("invalid_code", [None, "string"])
def test_invalid_code_type(invalid_code):
    with pytest.raises(ValueError):
        _MspCommand(invalid_code, 'B:1:?')

@pytest.mark.parametrize("invalid_format", [None, 123])
def test_invalid_data_format_type(invalid_format):
    with pytest.raises(ValueError):
        _MspCommand(150, invalid_format)

@pytest.mark.parametrize("data_format, expected_data_size", [
    ('B:1:? ', 1),
    ('H:2:? ', 4)
])
def test_non_standard_formats(data_format, expected_data_size):
    command = _MspCommand(150, data_format)

    assert command.data_size == expected_data_size

@pytest.mark.parametrize("data_format", [
    'ZZ:1:?'
])
def test_invalid_struct_format(data_format):
    with pytest.raises(StructError):
        _MspCommand(150, data_format)

@pytest.mark.parametrize("data_format", [
    ('B:1:?')
])
def test_repr_with_variable_size(data_format):
    command = _MspCommand(150, data_format)

    assert "?" in repr(command)

@pytest.mark.parametrize("code, data_format, expected_is_set_command", [
    (200, 'B:1:?', True),
    (100, 'H:1:? ', False)
])
def test_command_initialization(code, data_format, expected_is_set_command):
    command = _MspCommand(code, data_format)

    assert command.is_set_command == expected_is_set_command

@pytest.mark.parametrize("data_format", [
    None
])
def test_constructor_no_format(data_format):
    command = _MspCommand(150, data_format)

    assert command.data_field_count == 0
    assert command.data_size == 0
