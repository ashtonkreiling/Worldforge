import pygame
import pygame_gui

from server.world.world_state import WorldState
from client.action_form import ActionForm

class GameUI:
    def __init__(self, manager, window_size, server_connection: WorldState):
        self.manager = manager
        self.window_width, self.window_height = window_size
        self.server_connection = server_connection

        self.active_form = None

        self.header_height = 60
        self.sidebar_width = 220

        self.turn_payload = server_connection.get_turn_payload()

        self._build_header()
        self._build_sidebar()

    def _build_header(self):
        self.header_panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(
                0, 0,
                self.window_width, self.header_height
            ),
            starting_height=1,
            manager=self.manager
        )

        self.player_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(20, 10, 400, 40),
            text=f"Turn: {self.turn_payload["name"]} Year: {self.turn_payload["year"]}",
            manager=self.manager,
            container=self.header_panel
        )

    def reset_header(self):
        self.player_label.set_text(f"Turn: {self.turn_payload["name"]} Year: {self.turn_payload["year"]}")

    def _build_sidebar(self):
        self.sidebar_panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(
                0, self.header_height,
                self.sidebar_width,
                self.window_height - self.header_height
            ),
            starting_height=1,
            manager=self.manager
        )

        self.power_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(10, 10, 200, 30),
            text=f"Power: {self.turn_payload['power']}",
            manager=self.manager,
            container=self.sidebar_panel
        )

        self.action_buttons = []

        y = 60
        for action in self.turn_payload["actions"]:
            button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(10, y, 200, 40),
                text=f"{action['name']} ({action['cost']})",
                manager=self.manager,
                container=self.sidebar_panel
            )

            # Attach metadata directly to the button
            button.action_index = action["index"]
            button.action_cost = action["cost"]

            # Optional: disable if not enough power
            if action["cost"] > self.turn_payload["power"]:
                button.disable()

            self.action_buttons.append(button)
            y += 50

    def reset_sidebar(self):
        self.power_label.set_text(f"Power: {self.turn_payload['power']}")

        self.action_buttons = []

        y = 60
        for action in self.turn_payload["actions"]:
            button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(10, y, 200, 40),
                text=f"{action['name']} ({action['cost']})",
                manager=self.manager,
                container=self.sidebar_panel
            )

            # Attach metadata directly to the button
            button.action_index = action["index"]
            button.action_cost = action["cost"]

            # Optional: disable if not enough power
            if action["cost"] > self.turn_payload["power"]:
                button.disable()

            self.action_buttons.append(button)
            y += 50


    def process_event(self, event, hex_map, world_state):
        if hex_map.selected_hex is None:
            return  # No target selected

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element in self.action_buttons:
                if self.active_form:
                    self.active_form.destroy()
                    self.active_form = None
                action = next(
                    a for a in self.turn_payload["actions"]
                    if a["index"] == event.ui_element.action_index
                )

                self.active_form = ActionForm(
                    self.manager,
                    pygame.Rect(400, 100, 300, 400),
                    action
                )

            if self.active_form:
                if event.ui_element == self.active_form.submit:
                    data = self.active_form.collect_values()

                    q, r = hex_map.selected_hex
                    world_state.apply_action(
                        deity_id=world_state.current_turn,
                        action_index=self.active_form.action["index"],
                        q=q,
                        r=r,
                        params=data
                    )

                    self.active_form.destroy()
                    self.active_form = None
                    self.refresh_ui()

                elif event.ui_element == self.active_form.cancel:
                    self.active_form.destroy()
                    self.active_form = None

                # Update UI state
                self.turn_payload = self.server_connection.get_turn_payload()
                self.reset_header()
                self.reset_sidebar()
