from const import *
import pygame
from ship import PartShip


class Player(object):
    __kill_img = pygame.image.load("img/kill.png")
    __hit_img = pygame.image.load("img/hit.png")
    __miss_img = pygame.image.load("img/miss.png")
    def __init__(self, screen):
        self.screen = screen
        self.killed = 0
        self.log = []
        self.ships_num = [1, 2, 3, 4]
        self.ships = []
        self.parts_enemy_ship = []
        self.field = [[' '] * SIZE_FIELD for i in range(SIZE_FIELD)]
        self.field_enemy = [[' '] * SIZE_FIELD for i in range(SIZE_FIELD)]

    def attack(self, pos, enemy):
        x = pos[0]//(WIDTH//2)
        y = pos[1]//HEIGHT
        for ship in self.ships:
            for part in ship.parts:
                if part.rect.collidepoint(pos):
                    ship.field[ship.x - x + ship.y - y] = 'H'
                    part.image = self.__hit_img
                    del enemy.log[enemy.log.index((x,y))]
        if enemy.field[y][x-10] != ' ':
            flag  = True
            self.field_enemy[y][x - 10] = 'H'
            self.parts_enemy_ship.append(
            PartShip((x + 1) * (WIDTH // 2), y * HEIGHT, 'H', self.parts_enemy_ship, self.screen))
        else:
            flag = False
            self.field_enemy[y][x - 10] = 'M'
            self.parts_enemy_ship.append(
            PartShip((x + 1) * (WIDTH // 2), y * HEIGHT, 'M', self.parts_enemy_ship, self.screen))
        return flag
    def check_win(self):
        """
        Проверка на победу игрока
        :return: если игрок уничтожил необходимое количество кораблей
        """
        if self.killed == 10:
            return 1


if __name__ == '__main__':
    print('This is player model')
