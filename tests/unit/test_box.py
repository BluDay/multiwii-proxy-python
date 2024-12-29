from multiwii.config import MultiWiiBoxState
from multiwii.data   import MspBox, MspBoxIds, MspBoxItem, MspBoxNames

import pytest

@pytest.mark.parametrize("value, expected_aux1, expected_aux2, expected_aux3, expected_aux4", [
    (
        0b101010101,
        MultiWiiBoxState.Low,
        MultiWiiBoxState.Mid,
        MultiWiiBoxState.High,
        MultiWiiBoxState.Empty
    ),
])
def test_msp_box_item_parse_valid(value, expected_aux1, expected_aux2, expected_aux3, expected_aux4):
    result = MspBoxItem.parse(value)
    
    assert isinstance(result, MspBoxItem)

    assert result.aux1 == expected_aux1
    assert result.aux2 == expected_aux2
    assert result.aux3 == expected_aux3
    assert result.aux4 == expected_aux4

@pytest.mark.parametrize("item, expected_value", [
    (
        MspBoxItem(
            aux1=MultiWiiBoxState.Low,
            aux2=MultiWiiBoxState.Mid,
            aux3=MultiWiiBoxState.High,
            aux4=MultiWiiBoxState.Empty,
        )
        0b101010101
    ),
])
def test_msp_box_item_compile(item, expected_value):
    assert item.compile() == expected_value

@pytest.mark.parametrize("data", [((0b101010101, 0b110101010))])
def test_msp_box_parse(data):
    result = MspBox.parse(data)
    
    assert isinstance(result, MspBox)
    assert len(result.items) == 2
    assert all(isinstance(item, MspBoxItem) for item in result.items)

@pytest.mark.parametrize("item1, item2", [
    (
        MspBoxItem(
            aux1=MultiWiiBoxState.Low,
            aux2=MultiWiiBoxState.Mid,
            aux3=MultiWiiBoxState.High,
            aux4=MultiWiiBoxState.Empty
        ),
        MspBoxItem(
            aux1=MultiWiiBoxState.High,
            aux2=MultiWiiBoxState.Low,
            aux3=MultiWiiBoxState.Mid,
            aux4=MultiWiiBoxState.Empty
        )
    ),
])
def test_msp_box_as_serializable(item1, item2):
    box = MspBox(items=(item1, item2))
    
    serializable_data = box.as_serializable()

    assert isinstance(serializable_data, tuple)
    assert len(serializable_data) == 2
    assert all(isinstance(value, int) for value in serializable_data)

@pytest.mark.parametrize("data", [((1, 2, 3))])
def test_msp_box_ids_parse(data):
    result = MspBoxIds.parse(data)
    
    assert isinstance(result, MspBoxIds)
    assert len(result.values) == 3
    assert all(isinstance(box, MultiWiiBox) for box in result.values)

@pytest.mark.parametrize("data", [(b'Box1;Box2;Box3',)])
def test_msp_box_names_parse(data):
    result = MspBoxNames.parse(data)
    
    assert isinstance(result, MspBoxNames)
    assert len(result.names) == 3
    assert all(isinstance(name, str) for name in result.names)

@pytest.mark.parametrize("data", [()])
def test_msp_box_names_parse_empty(data):
    result = MspBoxNames.parse(data)
    
    assert isinstance(result, MspBoxNames)
    assert len(result.names) == 0

@pytest.mark.parametrize("value", [("invalid_value",)])
def test_msp_box_item_invalid_parse(value):
    with pytest.raises(ValueError):
        MspBoxItem.parse(value)

@pytest.mark.parametrize("item", [MspBox(items=())])
def test_msp_box_as_serializable_empty(item):
    assert item.as_serializable() == ()
