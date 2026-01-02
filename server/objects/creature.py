from server.objects.object import Object

class Creature(Object):
    def attach_to(self, parent):
        parent.creatures.append(self)