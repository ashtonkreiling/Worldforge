from actions.effect import Effect

from objects.object import Object

class AddHistory(Effect):
    def __init__(self, text_template: str):
        self.text_template = text_template

    def apply(self, context):
        text = self.text_template.format(
            deity=context.actor.name,
            turn=context.turn
        )
        context.subject.add_history_entry(text)

class AddChildObject(Effect):
    def __init__(self, object: Object):
        self.object = object
        super().__init__()

    def apply(self, context):
        self.object.attach_to(context.subject)