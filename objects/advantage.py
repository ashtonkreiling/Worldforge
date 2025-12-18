from objects.tag import Tag

class Advantage:
    def __init__(self, magnitude: int, affected_tags: list[Tag]):
        self.magnitude = magnitude
        self.affected_tags = affected_tags