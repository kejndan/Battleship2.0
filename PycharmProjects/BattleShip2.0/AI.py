from const import *
from random import randint, choice
from ship import Ship, check_aoe


class AI(object):
    def __init__(self, comp):
        """
        Данный класс за действия компьютера
        :param comp: сложность
        """
        self.complexity = comp
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
                if check_aoe(x, y, length, player.field, vector):  # уставливаем корабль
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


if __name__ == '__main__':
    print('This is AI model')
