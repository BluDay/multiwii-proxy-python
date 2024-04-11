from wiiproxy import MultiWii

from typing   import NoReturn
from unittest import main, TestCase

class TestMultiWii(TestCase):
    """Unit-test class for the MultiWii class."""
    
    def test_create_instance_that_raises_exception(self) -> NoReturn:
        """Haha."""
        with self.assertRaises(ValueError):
            fc = MultiWii(serial=None)

if __name__ == '__main__':
    main()
