"""
Test suite generated using ChatGPT-4o mini.

This suite contains various tests for the _MspCommand class to ensure 
correct functionality. It covers different edge cases, invalid inputs, 
and verifies the expected behavior of properties, methods, and attributes 
for a range of MSP command codes and data formats.
"""

from multiwii import _MspCommand
from struct   import error as StructError

import pytest

def test_valid_code_and_format():
    """
    Test valid code and format string.
    
    This test checks the behavior when a valid MSP command code and a 
    valid data format string are provided. It ensures that the command 
    code, data field count, data size, and the variable size flag are set 
    correctly.
    """
    command = _MspCommand(150, 'B:1:?')

    assert command.code == 150
    assert command.data_field_count == 1
    assert command.data_size == 1
    assert command.has_variable_size is True

@pytest.mark.parametrize("invalid_code", [99, 251])
def test_invalid_code(invalid_code):
    """
    Test invalid code (outside valid range).
    
    This test verifies that a ValueError is raised when an invalid command 
    code (outside the range 100-250) is passed to the constructor.
    """
    with pytest.raises(ValueError):
        _MspCommand(invalid_code, 'B:1:?')

def test_invalid_format_string():
    """
    Test invalid format string.
    
    This test checks that a ValueError is raised when an invalid format 
    string is provided, such as a missing ':?' part, and a StructError is 
    raised when the format string contains an invalid struct type.
    """
    with pytest.raises(ValueError):
        _MspCommand(150, 'B:1')

    with pytest.raises(StructError):
        _MspCommand(150, 'X:1:?')

@pytest.mark.parametrize("code", [100, 250])
def test_edge_case_code(code):
    """
    Test the edge case with exactly 100 and 250 codes.
    
    This test checks that the constructor accepts the boundary values of 
    the command code (100 and 250) and correctly sets the properties.
    """
    command = _MspCommand(code, 'B:1:?')

    assert command.code == code

def test_empty_data_format():
    """
    Test empty data format (None).
    
    This test verifies that when no data format is provided, the command 
    initializes correctly with default values for data field count, data 
    size, and payload format.
    """
    command = _MspCommand(150)

    assert command.data_field_count == 0
    assert command.data_size == 0
    assert command.payload_struct_format is None

def test_code_property():
    """
    Test the `code` property.
    
    This test ensures that the `code` property returns the correct MSP 
    command code.
    """
    command = _MspCommand(150, 'B:1:?')

    assert command.code == 150

def test_data_field_count_property():
    """
    Test the `data_field_count` property.
    
    This test verifies that the `data_field_count` property returns the 
    correct number of fields as specified in the data format.
    """
    command = _MspCommand(150, 'B:2:?')

    assert command.data_field_count == 2

def test_data_size_property():
    """
    Test the `data_size` property.
    
    This test ensures that the `data_size` property returns the correct 
    size for the provided data structure format.
    """
    command = _MspCommand(150, 'B:1:?')

    assert command.data_size == 1

def test_data_struct_format_property():
    """
    Test the `data_struct_format` property.
    
    This test verifies that the `data_struct_format` property returns 
    the correct format string used for packing and unpacking the payload.
    """
    command = _MspCommand(150, 'B:1:?')

    assert command.data_struct_format == 'B'

def test_has_variable_size_property():
    """
    Test the `has_variable_size` property.
    
    This test checks that the `has_variable_size` property is set correctly 
    based on the presence of the '?' flag in the data format.
    """
    fixed_size_command    = _MspCommand(150, 'B:1:')
    variable_size_command = _MspCommand(150, 'B:1:?')

    assert fixed_size_command.has_variable_size is False
    assert variable_size_command.has_variable_size is True

def test_is_set_command_property():
    """
    Test the `is_set_command` property.
    
    This test verifies that the `is_set_command` property correctly identifies 
    if the MSP command is a "set" command (with code >= 200).
    """
    set_command = _MspCommand(200, 'B:1:?')
    get_command = _MspCommand(150, 'B:1:?')

    assert set_command.is_set_command is True
    assert get_command.is_set_command is False

def test_payload_struct_format_property():
    """
    Test the `payload_struct_format` property.
    
    This test ensures that the `payload_struct_format` property is correctly 
    calculated and returned.
    """
    command = _MspCommand(150, 'B:1:?')

    assert command.payload_struct_format == '<2BB'

def test_int_method():
    """
    Test the `__int__` method.
    
    This test checks that the `__int__` method correctly returns the MSP 
    command code as an integer.
    """
    command = _MspCommand(150, 'B:1:?')

    assert int(command) == 150

def test_repr_method():
    """
    Test the `__repr__` method.
    
    This test verifies that the `__repr__` method generates a string that 
    correctly represents the object, including its command code and format.
    """
    command = _MspCommand(150, 'B:1:?')

    repr_str = repr(command)

    assert '<150' in repr_str
    assert '1' in repr_str
    assert '!' in repr_str

def test_str_method():
    """
    Test the `__str__` method.
    
    This test ensures that the `__str__` method returns the correct string 
    representation of the data structure format.
    """
    command = _MspCommand(150, 'B:1:?')

    assert str(command) == 'B'

def test_code_boundaries():
    """
	Test the handling of boundary code values.
    
    This test checks the behavior when the MSP command code is at its 
    boundary values (100 and 250). It verifies that the code is correctly 
    accepted and initialized.
    """
    lower_code_command = _MspCommand(100, 'B:1:?')
    upper_code_command = _MspCommand(250, 'B:1:?')

    assert lower_code_command.code == 100
    assert upper_code_command.code == 250

def test_invalid_code_type():
    """
	Test exception handling for non-integer code.
    
    This test checks that a ValueError is raised if the provided command 
    code is not an integer.
    """
    with pytest.raises(ValueError):
        _MspCommand(None, 'B:1:?')

    with pytest.raises(ValueError):
        _MspCommand("string", 'B:1:?')

def test_invalid_data_format_type():
    """
	Test invalid type for data_format.
    
    This test ensures that a ValueError is raised when the data format 
    is not a string (e.g., None or integer).
    """
    with pytest.raises(ValueError):
        _MspCommand(150, None)

    with pytest.raises(ValueError):
        _MspCommand(150, 123)

def test_non_standard_formats():
    """
	Test non-standard struct formats.
    
    This test verifies that non-standard struct formats are correctly 
    parsed and that the payload structure is formatted accordingly.
    """
    simple_command = _MspCommand(150, 'B:1:?')

    assert simple_command.data_size == 1

    complex_command = _MspCommand(150, 'H:2:?')

    assert complex_command.data_size == 4
    assert complex_command.payload_struct_format == '<2BH'

def test_invalid_struct_format():
    """
	Test invalid struct format string that causes struct.error.
    
    This test ensures that an invalid struct format (e.g., 'ZZ') raises 
    a `StructError`.
    """
    with pytest.raises(StructError):
        _MspCommand(150, 'ZZ:1:?')

def test_repr_with_variable_size():
    """
	Test `__repr__` with variable size formats.
    
    This test checks that the `__repr__` method correctly includes the 
    '?' flag when the data format has variable size.
    """
    command = _MspCommand(150, 'B:1:?')

    assert "?" in repr(command)

def test_command_initialization():
    """
	Test the command initialization with different code and format combinations.
    
    This test verifies that the constructor correctly handles different 
    MSP command codes and their associated data formats.
    """
    set_command = _MspCommand(200, 'B:1:?')

    assert set_command.is_set_command is True

    get_command = _MspCommand(100, 'H:1:?')

    assert get_command.is_set_command is False

def test_constructor_no_format():
    """
	Test the constructor with no data format.
    
    This test verifies that when no data format is provided, the object 
    is initialized with default values for data field count, data size, 
    and payload struct format.
    """
    command = _MspCommand(150)

    assert command.data_field_count == 0
    assert command.data_size == 0
