from abc import ABC, abstractmethod
from actions.action_context import ActionContext

class Effect(ABC):
    @abstractmethod
    def apply(self, context: ActionContext):
        pass
