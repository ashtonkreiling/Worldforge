from objects.object import Object

class Cataclysm(Object):
    def attach_to(self, parent):
        parent.cataclysms.append(self)