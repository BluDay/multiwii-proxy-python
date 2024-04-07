 class Analog(MultiWiiData):
    def __init__(self) -> None:
        super().__init__()
        
        self.voltage = 0

        self.power_meter = 0 # Unclear

        self.rssi = 0
        
        self.amperage = 0
