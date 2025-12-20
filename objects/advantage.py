from objects.tag import Tag
from utils.prompt_player import prompt_player

class Advantage:
    def __init__(self, magnitude: int, description: str):
        self.magnitude = magnitude
        self.description = description
        self.ttl = self.set_ttl()
        self.affected_tags = self.add_tags()
    
    def set_ttl(self):
        return prompt_player("How long should this advantage or disadvantage last?")
    
    def add_tags(self):
        tags = [Tag(self.name.lower())]
        while True:
            tag = prompt_player(f"Add a new tag to {self.name} or type 'skip' to skip")
            if tag == "skip":
                break
            tags.append(Tag(tag))
        return tags

    def attach_to(self, parent):
        parent.advantages.append(self)