from abc import ABC, abstractmethod
from objects.tag import Tag
from objects.event import Event
from actions.action_context import ActionContext
from utils.name_to_filename import to_filename
from utils.prompt_player import prompt_player

class Object(ABC):
    def __init__(self):
        self.name = self.set_name()
        self.description = self.set_description()
        self.tags = self.add_tags()
        self.file_path = to_filename(self.name)

    @abstractmethod
    def attach_to(self, parent):
        pass

    def set_name(self):
        return prompt_player(f"What is the name of this {type(self).__name__}?")

    def set_description(self):
        return prompt_player(f"Describe {self.name}")

    def add_tags(self):
        tags = [Tag(self.name.lower())]
        while True:
            tag = prompt_player(f"Add a new tag to {self.name} or type 'skip' to skip")
            if tag == "skip":
                break
            tags.append(Tag(tag))
        return tags
    
    def add_history_entry(self, context: ActionContext):
        event = Event(context)
        self.description += f"\n{event.to_text()}"

    def to_text(self):
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        for tag in self.tags:
            tag.to_text()