from objects.tag import Tag

class Advantage:
    def __init__(self, magnitude: int, description: str, ttl: int, affected_tags: list[Tag]):
        self.magnitude = magnitude
        self.description = description
        self.ttl = ttl
        self.affected_tags = affected_tags

    def attach_to(self, parent):
        parent.advantages.append(self)