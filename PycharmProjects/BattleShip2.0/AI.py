from const import *
from random import randint, choice
from ship import Ship, check_aoe
class AI(object):
    def __init__(self, comp):
        self.complexity = comp
        self.size = SIZE_FIELD
        self.list_attack = []

    def add_ships(self, player, screen):
        ships = (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)
        for length in ships:
            x = 0
            y = 0
            flag = True
            while flag:
                x = randint(0,self.size-1)
                y = randint(0,self.size-1)
                vector = choice([1,-1])
                if check_aoe(x, y, length, player.field.field, vector):
                    ship = Ship(length, (x+1)*(WIDTH//2), y*HEIGHT, vector, screen)
                    player.ships.append(ship)
                    for i in range(len(ship.field)):
                        if vector == 1:
                            player.field.field[y][x + i] = ship.field[i]
                            player.log.append((x + i, y))
                        else:
                            player.field.field[y + i][x] = ship.field[i]
                            player.log.append((x, y + i))
                        flag = False

                #
                #
                #
                #
                # if not (str(ship) in player.field.list_ships):
                #     player.field.list_ships[str(ship)] = []
                # prev = player.field.check_points(player.field.field)
                # player.field.
                #
                # now = player.field.check_points(player.field.field)
                # if prev < now:
                #     flag = False
                # else:
                #     player.field.list_ships[str(ship)].pop()
                #     x_start = 0
                #     y_start = 0
                #     x_end = -1
                #     y_end = -1
