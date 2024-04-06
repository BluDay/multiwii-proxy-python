class Misc(MultiWiiData):
    def __init__(self) -> None:
        super().__init__()

        self.power_trigger = 0

        self.throttle_idle = 0

        self.throttle_min = 0

        self.throttle_max = 0

        self.throttle_failsafe = 0

        self.plog_arm = 0

        self.plog_lifetime = 0

        self.mag_declination = 0

        self.battery_scale = 0

        self.battery_warn_1 = 0

        self.battery_warn_2 = 0

        self.battery_critical = 0
