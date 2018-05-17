import pygame
from const import *


def draw_grid(surface, num_field):
    """
    Функция отрисовки сетки
    :param surface: экран
    :param num_field: номер полуполскости; 0 - левая; 1 - правая
    """
    # горизонтальные линии
    MEDIUM = SIZE_FIELD*WIDTH/2
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


def draw_arc_vert(surface, x, y, status):
    """
    Функция отрисовки начала и конца вертикального корабля
    :param surface: экран
    :param x, y: начало координат нужной точки
    :param status: 1 - начало корабля; 0 - конец корабля
    """
    pygame.draw.circle(surface, BLACK, (x + WIDTH//4, y + HEIGHT//2), WIDTH//4)
    pygame.draw.rect(surface, BLACK, (x, y + status*HEIGHT//2, WIDTH//2, HEIGHT//2))


def draw_arc_hori(surface, x, y, status):
    """
    Функция отрисовки начала и конца горизонтального корабля
    :param surface: экран
    :param x, y:  начало координат нужной точки
    :param status: 1 - начало корабля; 0 - конец корабля
    """
    pygame.draw.ellipse(surface, BLACK, (x, y, WIDTH//2, HEIGHT))
    pygame.draw.rect(surface, BLACK, (x + status*WIDTH//4, y, WIDTH//4, HEIGHT))


def draw_choose_field_vert(surface, x, y, group):
    """
    Функция отрисовки выбора вертикальных кораблей
    :param surface: экран
    :param x, y: начало области  выбора кораблей
    """
    # четерёхпалубный корабль
    draw_arc_vert(surface, x, y, 1)
    pygame.draw.rect(surface, BLACK, (x, y + HEIGHT, WIDTH//2, HEIGHT))
    pygame.draw.rect(surface, BLACK, (x, y + HEIGHT*2, WIDTH // 2, HEIGHT))
    draw_arc_vert(surface, x, y + HEIGHT*3, 0)
    # трёхпалубный корабль
    draw_arc_vert(surface, x + WIDTH//2, y, 1)
    pygame.draw.rect(surface, BLACK, (x + WIDTH//2, y + HEIGHT, WIDTH//2, HEIGHT))
    draw_arc_vert(surface, x + WIDTH//2, y + HEIGHT*2, 0)
    # двухпалубный корабль
    draw_arc_vert(surface, x + WIDTH, y, 1)
    draw_arc_vert(surface, x + WIDTH, y + HEIGHT, 0)
    # однопалубный корабль
    pygame.draw.circle(surface, BLACK, (x + WIDTH + WIDTH//2 + WIDTH//4, y + HEIGHT//2), WIDTH//4)


def draw_choose_field_hori(surface, x, y):
    """
    Функция отрисовки выбора горизонтальных кораблей
    :param surface: экран
    :param x, y: начало области  выбора кораблей
    """
    # четырехпалубный корабль
    draw_arc_hori(surface, x, y, 1)
    pygame.draw.rect(surface, BLACK, (x + WIDTH//2, y, WIDTH//2, HEIGHT))
    pygame.draw.rect(surface, BLACK, (x + WIDTH, y, WIDTH//2, HEIGHT))
    draw_arc_hori(surface, x + WIDTH + WIDTH//2, y, 0)
    # трехпалубный корабль
    draw_arc_hori(surface, x, y + HEIGHT, 1)
    pygame.draw.rect(surface, BLACK, (x + WIDTH//2, y + HEIGHT, WIDTH//2, HEIGHT))
    draw_arc_hori(surface, x + WIDTH, y + HEIGHT, 0)
    # двухпалубный корабль
    draw_arc_hori(surface, x, y + HEIGHT*2, 1)
    draw_arc_hori(surface, x + WIDTH//2, y + HEIGHT*2, 0)
    # однопалубный корабль
    pygame.draw.circle(surface, BLACK, (x + WIDTH//4, y + HEIGHT*3 + HEIGHT//2), WIDTH//4)



