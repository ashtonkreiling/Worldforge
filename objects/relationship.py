from objects.object import Object
from deities.deity import Deity

class Relationship:
    def __init__(self, description: str = "Friendship", first_entity: Object | Deity = None, second_entity: Object | Deity = None):
        self.description = description
        self.first_entity = first_entity
        self.second_entity = second_entity