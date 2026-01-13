import pygame
import pygame_gui

class ActionForm:
    def __init__(self, manager, rect, action):
        self.manager = manager
        self.action = action

        self.panel = pygame_gui.elements.UIPanel(
            relative_rect=rect,
            manager=manager,
            starting_height=5
        )

        self.fields = {}
        self._build()

    def _build(self):
        padding = 10
        title_height = 30
        button_height = 45

        panel_rect = self.panel.get_relative_rect()

        #
        # ─── TITLE ─────────────────────────────────────────────────────
        #
        self.title = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(
                padding,
                padding,
                panel_rect.width - padding * 2,
                title_height
            ),
            text=self.action["name"],
            manager=self.manager,
            container=self.panel
        )

        #
        # ─── SCROLL CONTAINER ──────────────────────────────────────────
        #
        scroll_y = padding + title_height + padding
        scroll_height = panel_rect.height - scroll_y - button_height - padding

        self.scroll_container = pygame_gui.elements.UIScrollingContainer(
            relative_rect=pygame.Rect(
                padding,
                scroll_y,
                panel_rect.width - padding * 2,
                scroll_height
            ),
            manager=self.manager,
            container=self.panel
        )

        self.content_panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(
                0, 0,
                self.scroll_container.get_relative_rect().width,
                10
            ),
            manager=self.manager,
            container=self.scroll_container
        )

        #
        # ─── BUILD FIELDS ──────────────────────────────────────────────
        #
        y = 10

        for name, spec in self.action["fields"].items():
            field_type = spec["type"]

            pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect(10, y, 120, 25),
                text=name,
                manager=self.manager,
                container=self.content_panel
            )

            if field_type in ("string", "int"):
                widget = pygame_gui.elements.UITextEntryLine(
                    relative_rect=pygame.Rect(140, y, 140, 25),
                    manager=self.manager,
                    container=self.content_panel
                )

                self.fields[name] = {
                    "spec": spec,
                    "widget": widget
                }

            elif field_type == "tag":
                widget = pygame_gui.elements.UIDropDownMenu(
                    options_list=spec["options"],
                    starting_option=spec["options"][0],
                    relative_rect=pygame.Rect(140, y, 140, 25),
                    manager=self.manager,
                    container=self.content_panel
                )

                self.fields[name] = {
                    "spec": spec,
                    "widget": widget
                }

            elif field_type == "increment":
                buttons = {}

                for value, label, x in [
                    (-1, "-1", 140),
                    (0, "0", 185),
                    (1, "+1", 230),
                ]:
                    btn = pygame_gui.elements.UIButton(
                        pygame.Rect(x, y, 40, 25),
                        label,
                        self.manager,
                        self.content_panel
                    )
                    btn.increment_field = name
                    btn.increment_value = value
                    buttons[value] = btn

                self.fields[name] = {
                    "spec": spec,
                    "widget": buttons,
                    "value": 0
                }

            else:
                raise ValueError(f"Unknown field type {field_type}")

            y += 35

        #
        # ─── FINALIZE SCROLLING ─────────────────────────────────────────
        #
        content_height = y + 10

        self.content_panel.set_dimensions((
            self.content_panel.get_relative_rect().width,
            content_height
        ))

        self.scroll_container.set_scrollable_area_dimensions((
            self.content_panel.get_relative_rect().width,
            content_height
        ))

        #
        # ─── CONFIRM / CANCEL ──────────────────────────────────────────
        #
        button_y = panel_rect.height - button_height

        self.submit = pygame_gui.elements.UIButton(
            pygame.Rect(10, button_y, 120, 35),
            "Confirm",
            self.manager,
            self.panel
        )

        self.cancel = pygame_gui.elements.UIButton(
            pygame.Rect(160, button_y, 120, 35),
            "Cancel",
            self.manager,
            self.panel
        )

    def set_increment_value(self, field_name, value):
        field = self.fields[field_name]
        field["value"] = value

        for btn_value, button in field["widget"].items():
            if btn_value == value:
                button.select()
            else:
                button.unselect()

    def collect_values(self):
        values = {}

        for name, field in self.fields.items():
            spec = field["spec"]

            if spec["type"] in ("string", "int"):
                values[name] = field["widget"].get_text()

            elif spec["type"] == "tag":
                values[name] = field["widget"].selected_option

            elif spec["type"] == "increment":
                values[name] = field["value"]

        return values

    def destroy(self):
        self.panel.kill()
