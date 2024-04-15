from wiiproxy import MultiWii

from pytest import raises
from typing import NoReturn

class TestMultiWii(object):
    """Unit test class for the MultiWii class."""
    
    def test_create_instance_that_raises_exception(self) -> NoReturn:
        """Creates a MultiWii instance that raises the only exception."""
        with raises(TypeError):
            fc = MultiWii(serial=None)
