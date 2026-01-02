from server.objects.object import Object

class Leviathan(Object):
    def attach_to(self, parent):
        parent.leviathans.append(self)