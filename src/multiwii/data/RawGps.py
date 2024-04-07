class RawGps(MultiWiiData):
    def __init__(self) -> None:
        super().__init__()

        self.fix = 0

        self.satellites = 0

        self.coordinates = (0, 0)

        self.altitude = 0

        self.speed = 0

        self.ground_course = 0

    def evaluate(self, data: tuple) -> None:
        self.fix = data[0]

        self.satellites = data[1]

        self.coordinates = data[2:4]

        self.altitude = data[4]

        self.speed = data[5]

        self.ground_course = data[6]
