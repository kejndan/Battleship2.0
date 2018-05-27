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
        hit_ship = None
        for ship in enemy.ships:
            for part in ship.parts:
                if part.rect.collidepoint((pos[0]-MEDIUM, pos[1])):
                    ship.field[(ship.x+MEDIUM)//(WIDTH//2)-1 - x + ship.y//HEIGHT - y] = 'H'
                    part.image = self.__hit_img
                    print((x-10,y) in enemy.log)
                    del enemy.log[enemy.log.index((x-10,y))]
                    hit_ship = ship




        if enemy.field[y][x-10] != ' ':
            flag  = True
            self.field_enemy[y][x - 10] = 'H'
            self.parts_enemy_ship.append(
            PartShip((x + 1) * (WIDTH // 2), y * HEIGHT, 'H', self.parts_enemy_ship, self.screen))
            if hit_ship.field.count('H') == hit_ship.length:
                for part in hit_ship.parts:
                    hit_ship.field[(hit_ship.x+MEDIUM)//(WIDTH//2)-1 - x + hit_ship.y//HEIGHT - y] = 'K'
                    part.image = self.__kill_img
                    for part_hited in self.parts_enemy_ship:
                        if part_hited.x == part.x + MEDIUM and part_hited.y == part.y:
                            part_hited.image = self.__kill_img
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
