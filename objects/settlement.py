from objects.object import Object
from objects.project import Project
from objects.advantage import Advantage
from objects.artifact import Artifact
from objects.hero import Hero
from objects.faction import Faction
from objects.technology import Technology

class Settlement(Object):
    def __init__(
            self,
            name: str,
            description: str,
            inhabitants: dict[str:int],
            projects: list[Project] = None,
            advantages: list[Advantage] = None,
            artifacts: list[Artifact] = None,
            heroes: list[Hero] = None,
            factions: list[Faction] = None,
            technologies: list[Technology] = None,
        ):
        self.inhabitants = inhabitants
        self.projects = projects
        self.advantages = advantages
        self.artifacts = artifacts
        self.heroes = heroes
        self.factions = factions
        self.technologies = technologies
        super().__init__(name, description)

    def to_text(self):
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print("-------Projects-------")
        if self.projects:
            for project in self.projects:
                project.to_text()
        print("-------Artifacts------")
        if self.artifacts:
            for artifact in self.artifacts:
                artifact.to_text()
        print("---------Heros--------")
        if self.heros:
            for hero in self.heros:
                hero.to_text()
        print("-------Factions-------")
        if self.factions:
            for faction in self.factions:
                faction.to_text()
        print("-----Technologies-----")
        if self.technologies:
            for technology in self.technologies:
                technology.to_text()
        for tag in self.tags:
            tag.to_text()
