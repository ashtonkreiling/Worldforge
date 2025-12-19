from objects.object import Object

class Artifact(Object):
    def attach_to(self, parent):
        parent.artifacts.append(self)