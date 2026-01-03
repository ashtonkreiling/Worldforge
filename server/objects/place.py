from server.world.hex import Hex

class Place:
    def __init__(self, name: str, hexes: list[Hex]):
        self.name = name
        self.hexes = hexes