from objects.object import Object
from objects.project import Project
from objects.advantage import Advantage
from objects.tag import Tag
from objects.artifact import Artifact
from objects.hero import Hero
from objects.faction import Faction

class Settlement(Object):
    def __init__(
            self,
            name: str,
            description: str,
            inhabitants: dict[str:int],
            projects: list[Project],
            advantages: list[Advantage],
            tags: list[Tag],
            artifacts: list[Artifact],
            heros: list[Hero],
            factions: list[Faction],
        ):
        self.inhabitants = inhabitants
        self.projects = projects
        self.advantages = advantages
        self.artifacts = artifacts
        self.heros = heros
        self.factions = factions
        super.__init__(name, description, tags)
