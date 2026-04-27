import pygame
from tools import *
from datetime import datetime

def main():
    pygame.init()

    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Mini Paint")

    clock = pygame.time.Clock()

    canvas = pygame.Surface((900, 600))
    canvas.fill(WHITE)

    color_mode = "blue"
    tool = "pencil"
    thickness = 5

    drawing = False
    start_pos = None
    last_pos = None

    text_active = False
    text_pos = None
    text_value = ""
    text_font = pygame.font.Font(None, 28)

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if text_active:
                    if event.key == pygame.K_RETURN:
                        canvas.blit(text_font.render(text_value, True, get_color(color_mode)), text_pos)
                        text_active = False
                        text_value = ""
                    elif event.key == pygame.K_ESCAPE:
                        text_active = False
                        text_value = ""      
                    elif event.key == pygame.K_BACKSPACE:
                        text_value = text_value[:-1]
                    else:
                        text_value += event.unicode
                    continue             
                keys = pygame.key.get_pressed()

                if event.key == pygame.K_s and (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]) : # для левого и правого CTRL
                    filename = f"assets/canvas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png" # сохранится всё в папку assets
                    pygame.image.save(canvas, filename)
                    print(f"Saved as {filename}")
                elif event.key == pygame.K_ESCAPE:
                    return

                
                elif event.key == pygame.K_r:
                    color_mode = "red"
                elif event.key == pygame.K_g:
                    color_mode = "green"
                elif event.key == pygame.K_b:
                    color_mode = "blue"

                
                elif event.key == pygame.K_1:
                    thickness = 2
                elif event.key == pygame.K_2:
                    thickness = 5
                elif event.key == pygame.K_3:
                    thickness = 10

                
                elif event.key == pygame.K_p:
                    tool = "pencil"
                elif event.key == pygame.K_l:
                    tool = "line"
                elif event.key == pygame.K_t:
                    tool = "rectangle"
                elif event.key == pygame.K_c:
                    tool = "circle"
                elif event.key == pygame.K_e:
                    tool = "eraser"
                elif event.key == pygame.K_s:
                    tool = "square"
                elif event.key == pygame.K_y:
                    tool = "right_triangle"
                elif event.key == pygame.K_q:
                    tool = "equilateral_triangle"
                elif event.key == pygame.K_h:
                    tool = "rhombus"
                elif event.key == pygame.K_f:
                    tool = "fill"
                elif event.key == pygame.K_a:
                    tool = "text"    

                
                elif event.key == pygame.K_x:
                    canvas.fill(WHITE)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if tool == "fill":
                        flood_fill(canvas, event.pos, get_color(color_mode))
                    elif tool == "text":
                        text_active = True
                        text_pos = event.pos
                        text_value = ""    
                    else:
                        drawing = True
                        start_pos = event.pos
                        last_pos = event.pos

            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    current_pos = event.pos

                    if tool == "pencil":
                        pygame.draw.line(canvas, get_color(color_mode), last_pos, current_pos, thickness)
                        last_pos = current_pos

                    elif tool == "eraser":
                        pygame.draw.line(canvas, WHITE, last_pos, current_pos, thickness * 2)
                        last_pos = current_pos

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    end_pos = event.pos

                    if tool == "line":
                        pygame.draw.line(canvas, get_color(color_mode), start_pos, end_pos, thickness)

                    elif tool == "rectangle":
                        draw_rectangle(canvas, start_pos, end_pos, color_mode, thickness)

                    elif tool == "circle":
                        draw_circle(canvas, start_pos, end_pos, color_mode, thickness)

                    elif tool == "square":
                        draw_square(canvas, start_pos, end_pos, color_mode, thickness)

                    elif tool == "right_triangle":
                        draw_right_triangle(canvas, start_pos, end_pos, color_mode, thickness)

                    elif tool == "equilateral_triangle":
                        draw_equilateral_triangle(canvas, start_pos, end_pos, color_mode, thickness)

                    elif tool == "rhombus":
                        draw_rhombus(canvas, start_pos, end_pos, color_mode, thickness)

                    drawing = False

        screen.blit(canvas, (0, 0))

       
        if drawing and tool not in ["pencil", "eraser", "fill"]:
            current_pos = pygame.mouse.get_pos()

            if tool == "line":
                pygame.draw.line(screen, get_color(color_mode), start_pos, current_pos, thickness)

            elif tool == "rectangle":
                draw_rectangle(screen, start_pos, current_pos, color_mode, thickness)

            elif tool == "circle":
                draw_circle(screen, start_pos, current_pos, color_mode, thickness)

            elif tool == "square":
                draw_square(screen, start_pos, current_pos, color_mode, thickness)

            elif tool == "right_triangle":
                draw_right_triangle(screen, start_pos, current_pos, color_mode, thickness)

            elif tool == "equilateral_triangle":
                draw_equilateral_triangle(screen, start_pos, current_pos, color_mode, thickness)

            elif tool == "rhombus":
                draw_rhombus(screen, start_pos, current_pos, color_mode, thickness)

        if text_active:
            preview = text_font.render(text_value + "|", True, get_color(color_mode))
            screen.blit(preview, text_pos)        

        draw_text(screen, tool, color_mode, thickness)

        pygame.display.flip()
        clock.tick(60)

def draw_text(screen, tool, color_mode, thickness):
    font = pygame.font.Font(None, 22)

    text1 = f"Tool: {tool} | Color: {color_mode} | Size: {thickness}px"
    text2 = "1:Small  2:Medium  3:Large"
    text3 = "P:Pen L:Line T:Rect C:Circle E:Erase S:Square Y:Tri Q:EqTri H:Rhombus F:Fill A:Text X:Clear "

    screen.blit(font.render(text1, True, BLACK), (10, 5))
    screen.blit(font.render(text2, True, BLACK), (10, 25))
    screen.blit(font.render(text3, True, BLACK), (10, 45))


main()