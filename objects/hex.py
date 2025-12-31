class Hex:
    def __init__(
            self,
            q: int,
            r: int,
            height: int,
            terrain: str,
        ):
        self.q = q
        self.r = r
        self.height = height
        self.terrain = terrain
        self.resources = []
        self.creatures = []
        self.settlements = []
        self.leviathans = []
        self.artifacts = []