from abc import ABC, abstractmethod
from server.objects.event import Event
from server.actions.action_context import ActionContext
from server.utils.name_to_filename import to_filename

class Object(ABC):
    def __init__(self, name, description, tags):
        self.name = name
        self.description = description
        self.tags = tags
        self.file_path = to_filename(self.name)

    @abstractmethod
    def attach_to(self, parent):
        pass
    
    def add_history_entry(self, context: ActionContext):
        event = Event(context)
        self.description += f"\n{event.to_text()}"

    def to_text(self):
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        for tag in self.tags:
            tag.to_text()