import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 10
    drawing = False
    start_pos = None
    end_pos = None

    mode = 'draw' 
    color = (0, 0, 255)

    points = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

                if event.key == pygame.K_r:
                    color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)

                # 🛠 Режимы
                elif event.key == pygame.K_1:
                    mode = 'draw'
                elif event.key == pygame.K_2:
                    mode = 'rect'
                elif event.key == pygame.K_3:
                    mode = 'circle'
                elif event.key == pygame.K_4:
                    mode = 'eraser'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    start_pos = event.pos
                    points = [event.pos] 

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    end_pos = event.pos

                    if mode == 'rect':
                        draw_rect(screen, start_pos, end_pos, color)
                    elif mode == 'circle':
                        draw_circle(screen, start_pos, end_pos, color)

                    points = [] 

            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if mode == 'draw':
                        points.append(event.pos)
                        if len(points) > 1:
                            pygame.draw.line(screen, color, points[-2], points[-1], radius)

                    elif mode == 'eraser':
                        pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)

        pygame.display.flip()
        clock.tick(60)


def draw_rect(screen, start, end, color):
    x = min(start[0], end[0])
    y = min(start[1], end[1])
    width = abs(start[0] - end[0])
    height = abs(start[1] - end[1])
    pygame.draw.rect(screen, color, (x, y, width, height), 2)


def draw_circle(screen, start, end, color):
    radius = int(((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2) ** 0.5)
    pygame.draw.circle(screen, color, start, radius, 2)


main()