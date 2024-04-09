class _MultiWiiData(object):
    """
    Represents the base class for MultiWii data types.
    """

    def __init__(self) -> None:
        """
        Initializes an instance with default raw data values and keys.
        """
        self.__raw_values = ()

    @property
    def raw_values(self) -> tuple:
        """
        Gets an immutable list of raw values.
        """
        return self.__raw_values
    
    def update_values(self, data: tuple) -> None:
        """
        Updates raw values, evaluates values and updates targeted members.

        Parameters:
            data (tuple): An immutable list of raw data values.
        """
        if not isinstance(data, tuple):
            raise TypeError

        self._raw_values = data
