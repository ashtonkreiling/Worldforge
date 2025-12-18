from abc import ABC
from objects.tag import Tag
from utils.name_to_filename import to_filename

class Object(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.tags = self.add_tags()
        self.file_path = to_filename(name)

    def add_tags(self):
        tags = []
        while True:
            print(f"Add a new tag to {self.name} or type 'skip' to skip")
            tag = input()
            if tag == "skip":
                break
            tags.append(Tag(tag))
        return tags

    def to_text(self):
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        for tag in self.tags:
            tag.to_text()