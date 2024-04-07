class MultiWiiData(object):
    """
    Represents the base class for MultiWii data types.
    """

    def __init__(self) -> None:
        """
        Initializes an instance with default raw data values and keys.
        """
        self._keys = (key for key in self.__dict__ if key[0] == '_')

        self._raw_values = ()

    @property
    def raw_values(self) -> tuple:
        """
        Gets an immutable list of raw values.
        """
        return self._raw_values
    
    def evaluate(self, data: tuple) -> None:
        """
        Overridable method that processes raw data values and updates corresponding members.

        Parameters:
            data (tuple): An immutable list of raw data values.
        """
        for (index, key) in enumerate(self._keys):
            setattr(self, key, data[index])

    def update_values(self, data: tuple) -> None:
        """
        Updates raw values, evaluates values and updates targeted members.

        Parameters:
            data (tuple): An immutable list of raw data values.
        """
        if data is None: return

        self._raw_values = data

        self.evaluate(data)
