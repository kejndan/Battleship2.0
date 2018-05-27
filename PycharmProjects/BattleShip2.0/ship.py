from const import *
from pygame.sprite import Sprite, Group
import pygame


class Ship(object):
    def __init__(self, length, x, y, vector,  screen):
        """
        Данный класс создает корабль
        :param length: длина корабля
        :param x, y: координаты начала корабля
        :param vector: 1 - горизонтальный корабль; -1 - вертикальный корабль
        :param screen: экран
        """
        self.parts = Group()
        self.x = x
        self.y = y
        self.vector = vector
        self.length = length
        self.field = []
        self.log = []
        self.num_deck = length
        for i in range(self.length):
            if self.length == 1:
                part = 'O'
            elif i == 0:
                part = 'S'
            elif i == self.length - 1:
                part = 'E'
            else:
                part = 'X'

            if vector == 1:
                self.parts.add(PartShip(x + i*WIDTH//2, y, part, self.field, screen))
            elif vector == -1:
                self.parts.add(PartShip(x, y + i*HEIGHT, part, self.field, screen))

    def draw(self, screen):
        """
        Данная функция вызывает метод для рисования для каждого Sprite из группы parts
        :param screen: экран
        """
        self.parts.draw(screen)

    def update(self, *args):
        """
        Данная функция обновляет координаты корабля
        :param args: координаты на которые переместился корабль
        """
        if not args:  # если args пустой
            self.parts.update(*args)
        else:
            part_list = list(self.parts)
            rect = part_list[0].rect
            rect.x = args[0]
            rect.y = args[1]
            if self.vector == 1:
                for i in range(1, len(part_list)):
                    part_list[i].rect.x = args[0] + i*WIDTH/2
                    part_list[i].rect.y = args[1]
            else:
                for i in range(1, len(part_list)):
                    part_list[i].rect.x = args[0]
                    part_list[i].rect.y = args[1] + i*HEIGHT


class PartShip(Sprite):

    __start_img = pygame.image.load("img/start.png")
    __end_img = pygame.image.load("img/e.png")
    __m_img = pygame.image.load("img/m.png")
    __one_p = pygame.image.load("img/one.png")
    __hit_img = pygame.image.load("img/hit.png")
    __miss_img = pygame.image.load("img/miss.png")
    def __init__(self, x, y, part_ship, field, screen):
        """
        Данный класс создает часть корабля
        :param x, y: координаты начала корабля
        :param part_ship: O - корабль однопалубный;
                          S - начало многопалубного;
                          X - середина многопалубного;
                          E - конец многопалубного;
        :param field: массив в который заносится часть корабля
        :param screen: экран
        """
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y
        if part_ship == 'O':
            self.image = self.__one_p
            self.rect = self.image.get_rect()
            self.part = (self.image, self.rect)
        elif part_ship == 'S':
            self.image = self.__start_img
            self.rect = self.image.get_rect()
            self.part = (self.image, self.rect)
        elif part_ship == 'E':
            self.image = self.__end_img
            self.rect = self.image.get_rect()
            self.part = (self.image, self.rect)
        elif part_ship == 'X':
            self.image = self.__m_img
            self.rect = self.image.get_rect()
            self.part = (self.image, self.rect)
        elif part_ship == 'H':
            self.image = self.__hit_img
            self.rect = self.image.get_rect()
        elif part_ship == 'M':
            self.image = self.__miss_img
            self.rect = self.image.get_rect()
        self.rect.top = self.y
        self.rect.right = self.x
        if part_ship != 'H' and part_ship != 'M':
            field.append(part_ship)

    def update(self, *args):
        """
        Данная функция обновляет координаты корабля в том случае если args пустой
        """
        self.rect.x -= self.rect.width / 2
        self.rect.y -= self.rect.height / 2



def ship_cpy(ship,  screen):
    """
    Данная функция создает копию объекта Ship
    :return: возращает новый объект Ship
    """
    return Ship(ship.length, ship.x, ship.y, ship.vector,  screen)


def check_aoe(x, y, length, field, vector):
    """
    Данная функция проверяет можно ли поставить корабль в этом месте
    :param x, y: координаты курсора мыши куда нужно поставить начало корабля
    :param length: длина корабля
    :param field: массив где храниться корабли
    :param vector: 1 - горизонтальный корабль; -1 - вертикальный корабль
    :return: True - можно поставить корабль; False - нельзя поставить корабль
    """
    # Проверяем стоит другой корабль в радиусе одной ячейки
    for i in range(-1, length+1):
        for j in range(-1, 2):
            try:
                if y+i == -1 or x+j == -1:
                    raise IndexError
                if vector == -1 and (x+j > 10 or y+i > 10 or field[y+i][x+j] != ' '):
                        return False
                elif vector == 1 and (x + i > 10 or y + j > 10 or field[y+j][x+i] != ' '):
                        return False
            except IndexError:
                pass
    return True

if __name__ == '__main__':
    print('This is ship model')