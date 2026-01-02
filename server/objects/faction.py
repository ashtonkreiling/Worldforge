from server.objects.object import Object

class Faction(Object):
    def __init__(self):
        self.inhabitants = []
        self.projects = []
        self.advantages = []
        super().__init__()

    def attach_to(self, parent):
        parent.factions.append(self)