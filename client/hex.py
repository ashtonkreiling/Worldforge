import math
import pygame

class Hex:
    font = None

    @staticmethod
    def pixel_center(q, r, size, center, offset=(0, 0)):
        x = size * math.sqrt(3) * (q + r / 2)
        y = size * 3/2 * r
        return (
            center[0] + x + offset[0],
            center[1] + y + offset[1]
        )

    @staticmethod
    def corners(q, r, size, center, offset=(0, 0)):
        cx, cy = Hex.pixel_center(q, r, size, center, offset)
        points = []
        for i in range(6):
            angle = math.pi / 3 * i + math.pi / 6
            px = cx + size * math.cos(angle)
            py = cy + size * math.sin(angle)
            points.append((px, py))
        return points

    @staticmethod
    def draw(surface, q, r, size, center, offset=(0,0), height=0, color=(16,89,100), selected=False):
        base_color = color
        color = tuple(min(c + 50, 255) for c in base_color) if selected else base_color

        corners = Hex.corners(q, r, size, center, offset)

        pygame.draw.polygon(surface, color, corners, 0)
        pygame.draw.polygon(surface, (30, 30, 40), corners, 2)

        if Hex.font:
            cx, cy = Hex.pixel_center(q, r, size, center, offset)
            label = f"{q},{r}-{height}"
            text_surf = Hex.font.render(label, True, (220, 220, 220))
            surface.blit(text_surf, text_surf.get_rect(center=(cx, cy)))

    @staticmethod
    def contains_point(point, q, r, size, center, offset=(0,0)):
        polygon = Hex.corners(q, r, size, center, offset)
        x, y = point
        inside = False

        px1, py1 = polygon[0]
        for i in range(len(polygon) + 1):
            px2, py2 = polygon[i % len(polygon)]
            if min(py1, py2) < y <= max(py1, py2):
                if x <= max(px1, px2):
                    if py1 != py2:
                        xinters = (y - py1) * (px2 - px1) / (py2 - py1) + px1
                    if px1 == px2 or x <= xinters:
                        inside = not inside
            px1, py1 = px2, py2

        return inside
