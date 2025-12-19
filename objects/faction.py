from objects.object import Object

class Faction(Object):
    def attach_to(self, parent):
        parent.factions.append(self)