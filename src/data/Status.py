class Status(MultiWiiData):
    def __init__(self) -> None:
        super().__init__()

        self.cycle_time = 0

        self.i2c_errors = 0

        self.sensors = ()

        self.flag = 0

        self.global_conf = 0

    def evaluate(self, data) -> None:
        self.cycle_time = data[0]

        self.i2c_errors = data[1]

        self.sensors = (sensor if sensor | data[2] for sensor in Sensor)

        self.flag = data[3]

        self.global_conf = data[4]
