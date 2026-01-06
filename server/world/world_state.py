from server.world.hex import Hex
from server.deities.primordial import Primordial

class WorldState:
    def __init__(self):
        self.deities = [Primordial(), Primordial("Primordial 2")]
        # Which Deity in self.deities is taking a turn
        self.current_turn = 0
        # What "year" of history it is right now
        self.current_round = 0
        # When a primordial causes a cataclysm or sends a
        # leviathan to attack a settlement, sovereigns have
        # a chance to respond before the settlement is destroyed
        # this gets cleared at the end of the round
        self.hexes_to_update = {}
        self.changed_hexes = {
           (1,1): Hex(1,1,1,(100,89,16),"plains")
        }  # (q,r) -> Hex
        self.deities[0].increment_power()

    def format_hex_to_dict(self, hex: Hex):
        return {
            "q": hex.q,
            "r": hex.r,
            "height": hex.height,
            "color": hex.color,
        }

    def get_hex(self, q, r):
        hex = self.changed_hexes.get((q, r))
        if hex is None:
            return None
        return self.format_hex_to_dict(hex)
    
    def create_or_edit_hex(self, q, r, height, color, terrain):
        if self.changed_hexes[(q,r)]:
            hex = self.changed_hexes[(q,r)]
            hex.height = height
            hex.color = color
            hex.terrain = terrain
        else:
            hex = Hex(q, r, height, color, terrain)
            self.changed_hexes[(q,r)] = hex


    def get_hexes_in_range(self, q_min, q_max, r_min, r_max):
        return [
            self.format_hex_to_dict(h) for (q,r), h in self.changed_hexes.items()
            if q_min <= q <= q_max and r_min <= r <= r_max
        ]

    def get_current_deity(self):
        return self.deities[self.current_turn]

    def get_turn_payload(self):
        deity = self.get_current_deity()
        return {
            "year": self.current_round * 100,
            "name": deity.name,
            "power": deity.power,
            "actions": [
                {
                    "index": i,
                    "name": action.name,
                    "cost": action.cost,
                    "fields": action.fields(),
                }
                for i, action in enumerate(deity.actions)
            ]
        }

    def apply_action(self, deity_id, action_index, q, r):
        deity = self.get_current_deity()

        if deity_id != self.current_turn:
            raise ValueError("Not your turn")
        
        context = {
            "year": self.current_round * 100,
            "world": self,
            "q": q,
            "r": r,
            "height": 1,
            "color": (100,89,16),
            "terrain": "plains",
        }
        
        end_turn = deity.take_action(action_index, context)

        if end_turn:
            self.increment_turn_or_round()
            self.clear_hexes_to_update()
            self.get_current_deity().increment_power()


    def end_turn_if_needed(self):
        deity = self.get_current_deity()
        if deity.power <= 0:
            self.increment_turn_or_round()
            self.clear_hexes_to_update()
            deity = self.get_current_deity()
            deity.increment_power()

    def clear_hexes_to_update(self):
        pass

    def increment_turn_or_round(self):
        if self.current_turn + 1 >= len(self.deities):
            self.current_round += 1
            self.current_turn = 0
        else:
            self.current_turn += 1