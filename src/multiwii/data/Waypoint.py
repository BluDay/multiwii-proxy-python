class Waypoint(MultiWiiData):
    def __init__(self) -> None:
        super().__init__()

        self.number = 0

        self.position = (0, 0)

        self.alt_hold = 0

        self.heading = 0

        self.time_to_stay = 0

        self.flag = 0

    def evaluate(self, data) -> None:
        self.number = data[0]

        self.position = data[1:3]

        self.alt_hold = data[3]

        self.heading = data[4]

        self.time_to_stay = data[5]

        self.flag = data[6]
