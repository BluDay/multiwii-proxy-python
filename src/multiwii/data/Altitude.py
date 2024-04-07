 class Altitude(MultiWiiData):
    def __init__(self) -> None:
        super().__init__()

        self.estimation = 0

        self.pressure_variation = 0
