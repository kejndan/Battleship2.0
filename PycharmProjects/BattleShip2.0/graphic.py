import pygame
from const import *


def draw_grid(surface, num_field):
    """
    Функция отрисовки сетки
    :param surface: экран
    :param num_field: номер полуполскости; 0 - левая; 1 - правая
    """
    # горизонтальные линии
    start = [num_field*MEDIUM, 0]
    end = [MEDIUM + num_field*MEDIUM, 0]
    for i in range(SIZE_FIELD):
        pygame.draw.line(surface, BLACK, start, end, 1)
        start[1] += HEIGHT
        end[1] += HEIGHT
    # вертикальные линии
    start = [MEDIUM/10 + num_field*MEDIUM, 0]
    end = [MEDIUM/10 + num_field*MEDIUM, SIZE_FIELD*HEIGHT]
    for i in range(10):
        pygame.draw.line(surface, BLACK, start, end, 1)
        start[0] += MEDIUM/10
        end[0] += MEDIUM/10
    # разделительная черта
    pygame.draw.line(surface, WHITE, [MEDIUM, 0], [MEDIUM, SIZE_FIELD*HEIGHT], 1)

def draw_congratulation(player, screen, menu):
    back_img = pygame.image.load("img/congr.png")
    screen_rect = screen.get_rect()
    font_title = pygame.font.SysFont(None, 45)
    title = font_title.render("Congratulations to the {} with the victory".format(player.name), True, BLACK, COLOR_MENU_BUTTON)
    title_rect = title.get_rect()
    title_rect.center = screen_rect.center
    title_rect.top-=50
    screen.blit(back_img, (0, 0))
    screen.blit(title, title_rect)
    menu.button_restart.draw_button()



# def update_screen_select(back_img, screen):
#     """
#     Обновляет экран
#     """
#
#
#
# def full_draw_select_win(select_win, turn_button, auto_button, play_button):



if __name__ == '__main__':
    print('This is graphic model')
