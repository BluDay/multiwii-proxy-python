class CompGps(MultiWiiData):
    def __init__(self) -> None:
        super().__init__()

        self.distance_to_home = 0

        self.direction_to_home = 0

        self.update = 0 # What?
