from wiiproxy.multiwii import MultiWii

from pytest import raises
from typing import NoReturn

class TestMultiWii(object):
    def test_instantiation_that_raises_a_type_error(self) -> NoReturn:
        with raises(TypeError):
            fc = MultiWii(serial=None)
