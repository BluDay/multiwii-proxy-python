class _MultiWiiNames(ValuesBase):
    """
    Base class for name-retrieval commands.
    """
    def __init__(self) -> None:
        """
        Is this necessary?
        """
        super().__init__()

    def update_values(self, data: tuple) -> None:
        """
        Overridden method.
        """
        self.values = tuple(data[0].decode().split(';')[:-1])
