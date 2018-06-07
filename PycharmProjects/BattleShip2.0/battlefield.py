from graphic import draw_grid
from pygame import display, image
from buttons import ButtonReady
from const import *


class BattleField(object):
    def __init__(self, screen,  player_1, player_2):
        """
        Данный класс отвечает отрисовку игрового поля во время игры
        """
        self.screen = screen
        self.background_img = image.load("img/water-texture_(23).jpg")
        self.player = player_1
        self.enemy_player = player_2
        self.ready_button = ButtonReady(screen)

    def update(self):
        """
        Данная функция рисует игровое поле если идет игра игрок против игрока
        """
        self.screen.blit(self.background_img, (0, 0))
        draw_grid(self.screen, 0)
        draw_grid(self.screen, 1)
        for ship in self.player.ships:
            ship.draw(self.screen)
        for part in self.player.parts_enemy_ship:
            self.screen.blit(part.image, (part.rect.x, part.rect.y))
        for part in self.enemy_player.parts_enemy_ship:
            self.screen.blit(part.image, (part.rect.x-MEDIUM, part.rect.y))
        display.flip()

    def update2(self):
        """
        Данная функция рисует игровое поле если идет игра игрок против компьютера
        """
        self.screen.blit(self.background_img, (0, 0))
        draw_grid(self.screen, 0)
        draw_grid(self.screen, 1)
        for ship in self.enemy_player.ships:
            ship.draw(self.screen)
        for part in self.enemy_player.parts_enemy_ship:
            self.screen.blit(part.image, (part.rect.x, part.rect.y))
        for part in self.player.parts_enemy_ship:
            self.screen.blit(part.image, (part.rect.x-MEDIUM, part.rect.y))
        display.flip()

    def swap(self):
        """
        Данная функция меняет местами игроков в классе BattleShip
        """
        self.player, self.enemy_player = self.enemy_player, self.player

    def draw_preparation_field(self):
        """
        Данная функция рисует поле проверки готовности
        """
        self.screen.blit(self.background_img, (0, 0))
        draw_grid(self.screen, 0)
        draw_grid(self.screen, 1)
        self.ready_button.draw_button()
        display.flip()