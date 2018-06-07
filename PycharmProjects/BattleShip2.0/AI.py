from const import *
from random import randint, choice
from ship import Ship, check_aoe
from random import randint, choice

class AI(object):
    def __init__(self):
        """
        Данный класс за действия компьютера
        :param comp: сложность
        """
        self.size = SIZE_FIELD
        self.list_attack = []

    def add_ships(self, player, screen):
        """
        Данная функция сама расставляет корабли на поле
        """
        __ships = (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)  # длины кораблей
        for length in __ships:
            flag = True
            while flag:  # пока не уставновит корабль длины length
                # выбираем случайные координаты и тип расположения корабля
                x = randint(0, self.size-1)
                y = randint(0, self.size-1)
                vector = choice([1, -1])
                # проверяем можно ли уставить в данной точки  корабль
                if check_aoe(x, y, length, player.field, vector):
                    # уставливаем корабль
                    ship = Ship(length, (x+1)*(WIDTH//2), y*HEIGHT, vector, screen)
                    player.ships.append(ship)
                    for i in range(len(ship.field)):
                        # заносим его в field и сохраняем координты каждой точки в log
                        if vector == 1:
                            player.field[y][x + i] = ship.field[i]
                            player.log.append((x + i, y))
                        else:
                            player.field[y + i][x] = ship.field[i]
                            player.log.append((x, y + i))
                        flag = False


    def auto_attack(self, player, Menu):
        random_num = randint(1, 100)
        if (Menu.complexity == 'EASY' and random_num <= 10 or
                Menu.complexity == 'MEDIUM' and random_num <= 25 or
                Menu.complexity == 'HARD' and random_num <= 40):
            point = choice(player.log)
        else:
            y = randint(0, self.size - 1)
            x = randint(0, self.size - 1)
            point = (x, y)
        return (point[0]*(WIDTH//2)+MEDIUM, point[1]*HEIGHT)
    def AOE_attack(self, point):
        for i in [(-1,0),(1,0),(0,1),(0,-1)]:
            x = point[0] + i[0]*(WIDTH//2)
            y = point[1] + i[1]*HEIGHT
            if MEDIUM<=x<2*MEDIUM and 0<=y<HEIGHT*10:
                yield (x,y)

    def search_ship(self, pos, player):
        for ship in player.ships:
            for part in ship.parts:
                if part.rect.collidepoint(pos):
                    return ship

if __name__ == '__main__':
    print('This is AI model')
