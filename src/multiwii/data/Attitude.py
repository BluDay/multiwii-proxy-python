 class Attitude(MultiWiiData):
    def __init__(self) -> None:
        super().__init__()

        self.angle = (0, 0)

        self.heading = 0

    def evaluate(self, data) -> None:
        self.angle = data[0:2]

        self.heading = data[2]
