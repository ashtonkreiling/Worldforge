from objects.resource import Resource
from objects.creature import Creature
from objects.leviathan import Leviathan
from objects.artifact import Artifact
from objects.settlement import Settlement

class Hex:
    def __init__(
            self,
            q: int,
            r: int,
            height: int,
            terrain: str,
            resources: list[Resource],
            creatures: list[Creature],
            settlements: list[Settlement],
            leviathans: list[Leviathan],
            artifacts: list[Artifact]
        ):
        self.q = q
        self.r = r
        self.height = height
        self.terrain = terrain
        self.resources = resources
        self.creatures = creatures
        self.settlements = settlements
        self.leviathans = leviathans
        self.artifacts = artifacts