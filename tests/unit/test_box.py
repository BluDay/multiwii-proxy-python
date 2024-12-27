"""
Test suite generated using ChatGPT-4o mini.

This suite contains various tests for the MspBoxItem, MspBox, MspBoxIds, and MspBoxNames 
classes to ensure correct functionality. It covers different edge cases, invalid 
inputs, and verifies the expected behavior of properties, methods, and attributes for 
parsing, compiling, and serializing MultiWii box data.
"""

from multiwii.config import (
    MultiWiiBox,
    MultiWiiBoxState
)

from multiwii.data import (
    MspBox,
    MspBoxIds,
    MspBoxItem,
    MspBoxNames
)

from multiwii.messaging import _decode_names

import pytest

def test_msp_box_item_parse_valid():
    """
    Test that MspBoxItem.parse correctly parses an integer value into a box item.
    """
    value = 0b101010101

    result = MspBoxItem.parse(value)
    
    assert isinstance(result, MspBoxItem)
    assert result.aux1 == MultiWiiBoxState.Low
    assert result.aux2 == MultiWiiBoxState.Mid
    assert result.aux3 == MultiWiiBoxState.High
    assert result.aux4 == MultiWiiBoxState.Empty

def test_msp_box_item_compile():
    """
    Test that MspBoxItem.compile correctly compiles box state values into an integer.
    """
    item = MspBoxItem(
        aux1=MultiWiiBoxState.Low,
        aux2=MultiWiiBoxState.Mid,
        aux3=MultiWiiBoxState.High,
        aux4=MultiWiiBoxState.Empty
    )
    
    compiled_value = item.compile()

    assert compiled_value == 0b101010101

def test_msp_box_parse():
    """
    Test that MspBox.parse correctly parses a tuple of data into a MspBox instance.
    """
    data = (0b101010101, 0b110101010)

    result = MspBox.parse(data)
    
    assert isinstance(result, MspBox)
    assert len(result.items) == 2
    assert all(isinstance(item, MspBoxItem) for item in result.items)

def test_msp_box_as_serializable():
    """
    Test that MspBox.as_serializable returns a tuple of integers.
    """
    item1 = MspBoxItem(
        aux1=MultiWiiBoxState.Low,
        aux2=MultiWiiBoxState.Mid,
        aux3=MultiWiiBoxState.High,
        aux4=MultiWiiBoxState.Empty
    )

    item2 = MspBoxItem(
        aux1=MultiWiiBoxState.High,
        aux2=MultiWiiBoxState.Low,
        aux3=MultiWiiBoxState.Mid,
        aux4=MultiWiiBoxState.Empty
    )

    box = MspBox(items=(item1, item2))
    
    serializable_data = box.as_serializable()

    assert isinstance(serializable_data, tuple)
    assert len(serializable_data) == 2
    assert all(isinstance(value, int) for value in serializable_data)

def test_msp_box_ids_parse():
    """
    Test that MspBoxIds.parse correctly parses a tuple of data into a MspBoxIds instance.
    """
    data = (1, 2, 3)

    result = MspBoxIds.parse(data)
    
    assert isinstance(result, MspBoxIds)
    assert len(result.values) == 3
    assert all(isinstance(box, MultiWiiBox) for box in result.values)

def test_msp_box_names_parse():
    """
    Test that MspBoxNames.parse correctly parses a tuple of data into a MspBoxNames instance.
    """
    data = ("Box1", "Box2", "Box3")

    result = MspBoxNames.parse(data)
    
    assert isinstance(result, MspBoxNames)
    assert len(result.names) == 3
    assert all(isinstance(name, str) for name in result.names)

def test_msp_box_names_parse_empty():
    """
    Test that MspBoxNames.parse handles an empty tuple correctly.
    """
    data = ()

    result = MspBoxNames.parse(data)
    
    assert isinstance(result, MspBoxNames)
    assert len(result.names) == 0

def test_msp_box_item_invalid_parse():
    """
    Test that MspBoxItem.parse raises an error when provided with an invalid value.
    """
    with pytest.raises(ValueError):
        MspBoxItem.parse("invalid_value")  # Pass a non-integer value

def test_msp_box_as_serializable_empty():
    """
    Test that MspBox.as_serializable works with an empty box.
    """
    box = MspBox(items=())

    serializable_data = box.as_serializable()
    
    assert serializable_data == ()
