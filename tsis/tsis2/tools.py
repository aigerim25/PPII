import pygame
import math
from collections import deque

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def get_color(color_mode):
    if color_mode == "red":
        return (255, 0, 0)
    elif color_mode == "green":
        return (0, 180, 0)
    elif color_mode == "blue":
        return (0, 0, 255)
    return BLACK

def draw_rectangle(surface, start, end, color_mode, thickness):
    x = min(start[0], end[0])
    y = min(start[1], end[1])
    width = abs(end[0] - start[0])
    height = abs(end[1] - start[1])

    pygame.draw.rect(surface, get_color(color_mode), (x, y, width, height), thickness)

def draw_circle(surface, start, end, color_mode, thickness):
    radius = int(math.dist(start, end))
    pygame.draw.circle(surface, get_color(color_mode), start, radius, thickness)


def draw_square(surface, start, end, color_mode, thickness):
    size = max(abs(end[0] - start[0]), abs(end[1] - start[1]))

    x, y = start

    if end[0] < start[0]:
        x -= size
    if end[1] < start[1]:
        y -= size

    pygame.draw.rect(surface, get_color(color_mode), (x, y, size, size), thickness)


def draw_right_triangle(surface, start, end, color_mode, thickness):
    points = [
        start,
        (start[0], end[1]),
        end
    ]

    pygame.draw.polygon(surface, get_color(color_mode), points, thickness)


def draw_equilateral_triangle(surface, start, end, color_mode, thickness):
    side = abs(end[0] - start[0])
    height = int(side * math.sqrt(3) / 2)

    x1, y1 = start
    x2 = x1 + side if end[0] >= start[0] else x1 - side
    x3 = (x1 + x2) // 2
    y3 = y1 + height if end[1] >= start[1] else y1 - height

    points = [
        (x1, y1),
        (x2, y1),
        (x3, y3)
    ]

    pygame.draw.polygon(surface, get_color(color_mode), points, thickness)


def draw_rhombus(surface, start, end, color_mode, thickness):
    cx = (start[0] + end[0]) // 2
    cy = (start[1] + end[1]) // 2

    points = [
        (cx, start[1]),
        (end[0], cy),
        (cx, end[1]),
        (start[0], cy)
    ]

    pygame.draw.polygon(surface, get_color(color_mode), points, thickness)


def flood_fill(surface, start_pos, fill_color):
    width, height = surface.get_size()
    x, y = start_pos

    if x < 0 or x >= width or y < 0 or y >= height:
        return

    target_color = surface.get_at((x, y))
    fill_color = pygame.Color(fill_color)

    if target_color == fill_color:
        return

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        if x < 0 or x >= width or y < 0 or y >= height:
            continue

        if surface.get_at((x, y)) != target_color:
            continue

        surface.set_at((x, y), fill_color)

        queue.append((x + 1, y))
        queue.append((x - 1, y))
        queue.append((x, y + 1))
        queue.append((x, y - 1))

        if len(queue) % 1000 == 0:
            pygame.event.pump()