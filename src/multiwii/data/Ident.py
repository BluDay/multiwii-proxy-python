class Ident(MultiWiiData):
    def __init__(self) -> None:
        super().__init__()

        self.version = 0

        self.multitype = Multitype.Unidentified

        self.capabilities = ()

        self.navi_version = 0

    def evaluate(self, data: tuple) -> None:
        self.version = data[0] / 100

        self.multitype = Multitype(data[1])
        
        self.capabilities = (
            capability if capability & data[3] for capability in Capability
        )

        self.navi_version = data[3] >> 28
