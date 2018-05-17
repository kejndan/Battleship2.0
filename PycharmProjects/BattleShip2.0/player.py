import pygame
from const import *


class Player():
    def __init__(self, screen):
        self.screen = screen
        # self.field = Field()
        # self.field_enemy = Field()
        self.killed = 0
        self.log = []
        self.ships_num = [1, 2, 3, 4]
        self.ships = []

    def check_win(self):
        """
        Проверка на победу игрока
        :return: если игрок уничтожил необходимое количество кораблей
        """
        if self.killed == 10:
            return 1



    # def alignment_ships(self):




