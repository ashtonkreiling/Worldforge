from objects.object import Object

class Project(Object):
    def attach_to(self, parent):
        parent.projects.append(self)