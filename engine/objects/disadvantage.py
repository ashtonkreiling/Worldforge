from objects.tag import Tag
from utils.prompt_player import prompt_player

class Disadvantage:
    def __init__(self, magnitude: int):
        self.magnitude = magnitude
        self.ttl = self.set_ttl()
        self.affected_tags = self.add_tags()
    
    def set_ttl(self):
        return prompt_player("How long should this disadvantage last?")
    
    def add_tags(self):
        tags = []
        while True:
            tag = prompt_player(f"Add a new tag to this disadvantage or type 'skip' to skip")
            if tag == "skip":
                break
            tags.append(Tag(tag))
        return tags

    def attach_to(self, parent):
        parent.advantages.append(self)