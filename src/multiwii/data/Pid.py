class Pid(ValuesBase):
    def __init__(self) -> None:
        super().__init__()

    def evaluate(self, data) -> None:
        self.values = (
            data[index:index + 3] for index in range(0, len(data), 3)
        )
