from objects.object import Object

class Technology(Object):
    def attach_to(self, parent):
        parent.technologies.append(self)