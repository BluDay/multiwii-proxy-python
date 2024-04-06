class RawImu(MultiWiiData):
    def __init__(self) -> None:
        super().__init__()

        self.acc = (0, 0, 0)

        self.gyro = (0, 0, 0)

        self.mag = (0, 0, 0)

    def evaluate(self, data) -> None:
        self.acc = data[0:3]

        self.gyro = data[3:6]

        self.mag = data[6:9]
