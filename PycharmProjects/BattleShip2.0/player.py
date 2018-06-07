from const import *
import pygame
from ship import PartShip


class Player(object):
    kill_img = pygame.image.load("img/kill.png")
    hit_img = pygame.image.load("img/hit.png")
    miss_img = pygame.image.load("img/miss.png")
    name_parts = ('S','X','E', 'O')
    def __init__(self, screen, name):
        """
        Класс игрока
        """
        self.screen = screen
        self.name = name
        self.killed = 0
        self.log = []
        self.ships_num = [1, 2, 3, 4]
        self.ships = []
        self.parts_enemy_ship = []
        self.field = [[' '] * SIZE_FIELD for i in range(SIZE_FIELD)]
        self.field_enemy = [[' '] * SIZE_FIELD for i in range(SIZE_FIELD)]

    def attack(self, pos, enemy):
        """
        Данная функция атакует по переданным координатам
        :param pos: координаты атаки
        :param enemy: вражеский игрок
        :return: True - если игрок попал; False - если игрок промахнулся
        """
        x = pos[0]//(WIDTH//2)
        y = pos[1]//HEIGHT
        hit_ship = None
        for ship in enemy.ships:
            for part in ship.parts:
                if part.rect.collidepoint((pos[0]-MEDIUM, pos[1])):
                    ship.num_deck -= 1
                    part.image = part.hit_img
                    del enemy.log[enemy.log.index((x-10,y))]
                    hit_ship = ship

        if enemy.field[y][x-10] in self.name_parts:
            flag  = True
            self.field_enemy[y][x - 10] = 'H'
            enemy.field[y][x-10] = 'H'
            self.parts_enemy_ship.append(
            PartShip((x+1)*(WIDTH//2), y*HEIGHT, 'H', self.parts_enemy_ship, self.screen))
            if hit_ship.num_deck == 0:
                self.killed += 1
                for part in hit_ship.parts:
                    part.image = part.kill_img
                    for part_hited in self.parts_enemy_ship:
                        if part_hited.x == part.x + MEDIUM and part_hited.y == part.y:
                            part_hited.image = self.kill_img
        else:
            flag = False
            self.field_enemy[y][x - 10] = 'M'
            enemy.field[y][x - 10] = 'M'
            self.parts_enemy_ship.append(
            PartShip((x+1)*(WIDTH//2), y*HEIGHT, 'M', self.parts_enemy_ship, self.screen))

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
