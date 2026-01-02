from server.objects.object import Object

class Settlement(Object):
    def __init__(
            self,
            inhabitants: dict[str:int],
        ):
        self.inhabitants = inhabitants
        self.projects = []
        self.advantages = []
        self.artifacts = []
        self.heroes = []
        self.factions = []
        self.technologies = []
        self.size = 1
        super().__init__()

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
