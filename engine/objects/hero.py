from objects.object import Object

class Hero(Object):
    def attach_to(self, parent):
        parent.heroes.append(self)