import math
import pygame

class Hex:
    font = None  # assigned after pygame.init()

    def __init__(self, q, r, size, center):
        self.q = q
        self.r = r
        self.size = size
        self.center = center
        self.selected = False

    def pixel_center(self, offset=(0, 0)):
        x = self.size * math.sqrt(3) * (self.q + self.r / 2)
        y = self.size * 3/2 * self.r
        return (
            self.center[0] + x + offset[0],
            self.center[1] + y + offset[1]
        )

    def corners(self, offset=(0, 0)):
        cx, cy = self.pixel_center(offset)
        points = []
        for i in range(6):
            angle = math.pi / 3 * i + math.pi / 6
            px = cx + self.size * math.cos(angle)
            py = cy + self.size * math.sin(angle)
            points.append((px, py))
        return points

    def draw(self, surface, offset=(0, 0)):
        base_color = (80, 80, 100)
        color = tuple(min(c + 50, 255) for c in base_color) if self.selected else base_color

        pygame.draw.polygon(surface, color, self.corners(offset), 0)
        pygame.draw.polygon(surface, (30, 30, 40), self.corners(offset), 2)

        if Hex.font:
            cx, cy = self.pixel_center(offset)
            label = f"{self.q},{self.r}"
            text_surf = Hex.font.render(label, True, (220, 220, 220))
            text_rect = text_surf.get_rect(center=(cx, cy))
            surface.blit(text_surf, text_rect)

    def contains_point(self, point, offset=(0,0)):
        polygon = self.corners()
        x = point[0] - offset[0]
        y = point[1] - offset[1]
        inside = False

        n = len(polygon)
        px1, py1 = polygon[0]

        for i in range(n + 1):
            px2, py2 = polygon[i % n]

            if min(py1, py2) < y <= max(py1, py2):
                if x <= max(px1, px2):
                    if py1 != py2:
                        xinters = (y - py1) * (px2 - px1) / (py2 - py1) + px1
                    if px1 == px2 or x <= xinters:
                        inside = not inside

            px1, py1 = px2, py2

        return inside
