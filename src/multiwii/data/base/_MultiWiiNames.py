class _MultiWiiNames(ValuesBase):
    def __init__(self) -> None:
        super().__init__()

    def evaluate(self, data) -> None:
        self.values = tuple(data[0].decode().split(';')[:-1])
