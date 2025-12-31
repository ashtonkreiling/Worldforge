from objects.tag import Tag
from utils.prompt_player import prompt_player

class Advantage:
    def __init__(self, magnitude: int, battle: bool = False):
        self.magnitude = magnitude
        self.battle = battle
        self.ttl = self.set_ttl()
        self.affected_tags = self.add_tags()
    
    def set_ttl(self):
        return prompt_player("How long should this advantage last?")
    
    def add_tags(self):
        tags = []
        if self.battle:
            tags.append(Tag("battle"))
        while True:
            tag = prompt_player(f"Add a new tag to this advantage or type 'skip' to skip")
            if tag == "skip":
                break
            tags.append(Tag(tag))
        return tags

    def attach_to(self, parent):
        parent.advantages.append(self)