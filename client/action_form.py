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
        y = 10

        title = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(10, y, 280, 30),
            text=self.action["name"],
            manager=self.manager,
            container=self.panel
        )
        y += 40

        for name, spec in self.action["fields"].items():
            field_type = spec["type"]

            label = pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect(10, y, 120, 25),
                text=name,
                manager=self.manager,
                container=self.panel
            )

            if field_type == "string":
                widget = pygame_gui.elements.UITextEntryLine(
                    relative_rect=pygame.Rect(140, y, 140, 25),
                    manager=self.manager,
                    container=self.panel
                )

            elif field_type == "int":
                widget = pygame_gui.elements.UITextEntryLine(
                    relative_rect=pygame.Rect(140, y, 140, 25),
                    manager=self.manager,
                    container=self.panel
                )

            elif field_type == "tag":
                widget = pygame_gui.elements.UIDropDownMenu(
                    options_list=spec["options"],
                    starting_option=spec["options"][0],
                    relative_rect=pygame.Rect(140, y, 140, 25),
                    manager=self.manager,
                    container=self.panel
                )

            elif field_type == "increment":
                widget = {
                    -1: pygame_gui.elements.UIButton(
                        pygame.Rect(140, y, 40, 25),
                        "-1", self.manager, self.panel
                    ),
                    0: pygame_gui.elements.UIButton(
                        pygame.Rect(185, y, 40, 25),
                        "0", self.manager, self.panel
                    ),
                    1: pygame_gui.elements.UIButton(
                        pygame.Rect(230, y, 40, 25),
                        "+1", self.manager, self.panel
                    ),
                }

            else:
                raise ValueError(f"Unknown field type {field_type}")

            self.fields[name] = {"spec": spec, "widget": widget}
            y += 35

        self.submit = pygame_gui.elements.UIButton(
            pygame.Rect(10, y + 10, 120, 35),
            "Confirm",
            self.manager,
            self.panel
        )

        self.cancel = pygame_gui.elements.UIButton(
            pygame.Rect(160, y + 10, 120, 35),
            "Cancel",
            self.manager,
            self.panel
        )

    def collect_values(self):
        values = {}
        for name, field in self.fields.items():
            widget = field["widget"]
            spec = field["spec"]

            if spec["type"] in ("string", "int"):
                values[name] = widget.get_text()

            elif spec["type"] == "tag":
                values[name] = widget.selected_option

            elif spec["type"] == "increment":
                values[name] = self._increment_value

        return values

    def destroy(self):
        self.panel.kill()
