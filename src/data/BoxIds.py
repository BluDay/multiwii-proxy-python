class BoxIds(ValuesBase):
    def __init__(self) -> None:
        super().__init__()

    def evaluate(self, data) -> None:
        self.values = (BoxType(value) for value in data)
