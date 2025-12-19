from objects.object import Object

class Resource(Object):
    def attach_to(self, parent):
        parent.resources.append(self)