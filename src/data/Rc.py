class Rc(MultiWiiData):
    def __init__(self) -> None:
        super().__init__()

        self.roll = 0

        self.pitch = 0

        self.yaw = 0

        self.throttle = 0

        self.aux = (0, 0, 0, 0)
    
    def evaluate(self, data) -> None:
        self.roll = data[0]

        self.pitch = data[1]

        self.yaw = data[2]

        self.throttle = data[3]

        self.aux = data[4:]
