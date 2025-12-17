from objects.project import Project
from objects.advantage import Advantage
from objects.tag import Tag

class Settlement:
    def __init__(
            self,
            name: str,
            description: str,
            inhabitants: dict[str:int],
            projects: list[Project],
            advantages: list[Advantage],
            tags: list[Tag]

        ):
        self.name = name
        self.description = description
        self.inhabitants = inhabitants
        self.projects = projects
        self.advantages = advantages
        self.tags = tags
