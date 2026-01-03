import pygame
import pygame_gui

class GameUI:
    def __init__(self, manager, window_size):
        self.manager = manager
        self.window_width, self.window_height = window_size

        self.header_height = 60
        self.sidebar_width = 220

        self.current_player = "Player 1"
        self.power = 10

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
            text=f"Turn: {self.current_player}",
            manager=self.manager,
            container=self.header_panel
        )

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
            text=f"Power: {self.power}",
            manager=self.manager,
            container=self.sidebar_panel
        )

        self.raise_land_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(10, 60, 200, 40),
            text="Raise Land",
            manager=self.manager,
            container=self.sidebar_panel
        )

        self.lower_land_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(10, 110, 200, 40),
            text="Lower Land",
            manager=self.manager,
            container=self.sidebar_panel
        )

    def process_event(self, event, hex_map, world_state):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.raise_land_button:
                self._raise_selected_hex(hex_map, world_state)

            if event.ui_element == self.lower_land_button:
                self._lower_selected_hex(hex_map, world_state)

    def _raise_selected_hex(self, hex_map, world_state):
        if not hex_map.selected_hex or self.power <= 0:
            return

        q, r = hex_map.selected_hex
        world_state.apply_action(
            type("Action", (), {
                "q": q,
                "r": r,
                "delta": 1
            })()
        )

        self.power -= 1
        self.power_label.set_text(f"Power: {self.power}")

    def _lower_selected_hex(self, hex_map, world_state):
        if not hex_map.selected_hex or self.power <= 0:
            return

        q, r = hex_map.selected_hex
        world_state.apply_action(
            type("Action", (), {
                "q": q,
                "r": r,
                "delta": -1
            })()
        )

        self.power -= 1
        self.power_label.set_text(f"Power: {self.power}")