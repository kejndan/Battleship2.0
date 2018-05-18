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
        :param field: массив в который данный корабль записывается
        :param screen: экран
        """
        self.parts = Group()
        self.x = x
        self.y = y
        self.vector = vector
        self.length = length
        self.field = []
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
        if not args: # если args пустой
            self.parts.update(*args)
        else:
            part_list = list(self.parts)
            rect = part_list[0].rect
            rect.x = args[0]
            rect.y = args[1]
            if self.vector == 1:
                for i in range(1,len(part_list)):
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
        self.rect.top = y
        self.rect.right = x
        field.append(part_ship)

    def update(self, *args):
        """
        Данная функция обновляет координаты корабля в том случае если args пустой
        """
        self.rect.x -= self.rect.width / 2
        self.rect.y -= self.rect.height / 2





