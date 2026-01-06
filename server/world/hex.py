class Hex:
    def __init__(
            self,
            q: int,
            r: int,
            height: int,
            color: tuple[int, int, int],
            terrain: str,
        ):
        self.q = q
        self.r = r
        self.height = height
        self.color = color
        self.terrain = terrain
        self.resources = []
        self.creatures = []
        self.settlements = []
        self.leviathans = []
        self.artifacts = []
        self.cataclysms = []