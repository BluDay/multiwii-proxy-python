from wiiproxy import MultiWii

from pytest import raises
from typing import NoReturn

class TestMultiWii(object):
    """Unit-test class for the MultiWii class."""
    
    def test_create_instance_that_raises_exception(self) -> NoReturn:
        """Creates a MultiWii instance that raises a ValueError exception."""
        with raises(ValueError):
            fc = MultiWii(serial=None)
