import pygame
import math

def main():
    pygame.init()

    WIDTH, HEIGHT = 800, 600
    TOOLBAR_HEIGHT = 60

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mini Paint")

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 22)

    canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT))
    canvas.fill((0, 0, 0))

    color = (0, 0, 255)
    radius = 10
    mode = "brush"

    drawing = False
    start_pos = None
    last_pos = None

    buttons = [
        ("Brush", pygame.Rect(10, 10, 80, 35)),
        ("Square", pygame.Rect(100, 10, 90, 35)),
        ("Right Tri", pygame.Rect(200, 10, 100, 35)),
        ("Eq Tri", pygame.Rect(310, 10, 80, 35)),
        ("Rhombus", pygame.Rect(400, 10, 100, 35)),
        ("Eraser", pygame.Rect(510, 10, 90, 35)),
        ("Red", pygame.Rect(610, 10, 55, 35)),
        ("Green", pygame.Rect(670, 10, 65, 35)),
        ("Blue", pygame.Rect(740, 10, 55, 35)),
    ]

    running = True

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = event.pos

                    clicked_button = False

                    for text, rect in buttons:
                        if rect.collidepoint(mouse_pos):
                            clicked_button = True

                            if text == "Brush":
                                mode = "brush"
                            elif text == "Square":
                                mode = "square"
                            elif text == "Right Tri":
                                mode = "right_triangle"
                            elif text == "Eq Tri":
                                mode = "equilateral_triangle"
                            elif text == "Rhombus":
                                mode = "rhombus"
                            elif text == "Eraser":
                                mode = "eraser"
                            elif text == "Red":
                                color = (255, 0, 0)
                            elif text == "Green":
                                color = (0, 255, 0)
                            elif text == "Blue":
                                color = (0, 0, 255)

                    if not clicked_button and mouse_pos[1] > TOOLBAR_HEIGHT:
                        drawing = True
                        start_pos = (mouse_pos[0], mouse_pos[1] - TOOLBAR_HEIGHT)
                        last_pos = start_pos

            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    mouse_pos = event.pos
                    current_pos = (mouse_pos[0], mouse_pos[1] - TOOLBAR_HEIGHT)

                    if mode == "brush":
                        pygame.draw.line(canvas, color, last_pos, current_pos, radius)
                        last_pos = current_pos

                    elif mode == "eraser":
                        pygame.draw.circle(canvas, (0, 0, 0), current_pos, radius)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    mouse_pos = event.pos
                    end_pos = (mouse_pos[0], mouse_pos[1] - TOOLBAR_HEIGHT)

                    if mode == "square":
                        draw_square(canvas, start_pos, end_pos, color)

                    elif mode == "right_triangle":
                        draw_right_triangle(canvas, start_pos, end_pos, color)

                    elif mode == "equilateral_triangle":
                        draw_equilateral_triangle(canvas, start_pos, end_pos, color)

                    elif mode == "rhombus":
                        draw_rhombus(canvas, start_pos, end_pos, color)

                    drawing = False

        screen.fill((200, 200, 200))
        screen.blit(canvas, (0, TOOLBAR_HEIGHT))

        draw_toolbar(screen, buttons, font, mode)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def draw_toolbar(screen, buttons, font, mode):
    pygame.draw.rect(screen, (230, 230, 230), (0, 0, 800, 60))

    for text, rect in buttons:
        button_color = (245, 245, 245)

        if (
            (text == "Brush" and mode == "brush") or
            (text == "Square" and mode == "square") or
            (text == "Right Tri" and mode == "right_triangle") or
            (text == "Eq Tri" and mode == "equilateral_triangle") or
            (text == "Rhombus" and mode == "rhombus") or
            (text == "Eraser" and mode == "eraser")
        ):
            button_color = (180, 180, 180)

        pygame.draw.rect(screen, button_color, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 2)

        label = font.render(text, True, (0, 0, 0))
        screen.blit(label, (rect.x + 8, rect.y + 9))


def draw_square(surface, start, end, color):
    size = max(abs(end[0] - start[0]), abs(end[1] - start[1]))

    x = start[0]
    y = start[1]

    if end[0] < start[0]:
        x -= size
    if end[1] < start[1]:
        y -= size

    pygame.draw.rect(surface, color, (x, y, size, size), 2)


def draw_right_triangle(surface, start, end, color):
    points = [
        start,
        (start[0], end[1]),
        end
    ]

    pygame.draw.polygon(surface, color, points, 2)


def draw_equilateral_triangle(surface, start, end, color):
    side = abs(end[0] - start[0])
    height = int(side * math.sqrt(3) / 2)

    x1, y1 = start
    x2 = x1 + side if end[0] >= start[0] else x1 - side
    x3 = (x1 + x2) // 2

    if end[1] >= start[1]:
        y3 = y1 + height
    else:
        y3 = y1 - height

    points = [
        (x1, y1),
        (x2, y1),
        (x3, y3)
    ]

    pygame.draw.polygon(surface, color, points, 2)


def draw_rhombus(surface, start, end, color):
    center_x = (start[0] + end[0]) // 2
    center_y = (start[1] + end[1]) // 2

    points = [
        (center_x, start[1]),
        (end[0], center_y),
        (center_x, end[1]),
        (start[0], center_y)
    ]

    pygame.draw.polygon(surface, color, points, 2)
main()