class ValuesBase(MultiWiiData):
    def __init__(self) -> None:
        super().__init__()

        self._values = ()

    def evaluate(self, data) -> None:
        self._values = data

    @property
    def values(self) -> tuple:
        return self._values
