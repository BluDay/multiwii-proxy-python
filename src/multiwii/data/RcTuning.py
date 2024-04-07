 class RcTuning(MultiWiiData):
    def __init__(self) -> None:
        super().__init__()

        self.rate = 0

        self.expo = 0

        self.roll_pitch_rate = 0

        self.yaw_rate = 0

        self.dynamic_throttle_pid = 0

        self.throttle_mid = 0

        self.throttle_expo = 0
