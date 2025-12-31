from objects.object import Object

class Sentient(Object):
    def attach_to(self, parent):
        parent.sentients.append(self)