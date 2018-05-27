from select_window import SelectWindow
from buttons import ButtonsSelectWin
from const import *
from graphic import draw_grid
from pygame import image, display
class Select(object):
    def __init__(self, screen):
        self.screen = screen
        self.back_img = image.load("img/water-texture_(23).jpg")
        self.ships_num = [1,2,3,4]
        self.select_win_hori = SelectWindow(self.screen, 1)
        self.select_win_vert = SelectWindow(self.screen, -1)
        self.select_win_vert.create_select_ships()
        self.select_win_hori.create_select_ships()
        self.select_win = self.select_win_vert
        self.turn_button = ButtonsSelectWin(self.screen, "TURN", 7)
        self.auto_button = ButtonsSelectWin(self.screen, "AUTO", 8)
        self.play_button = ButtonsSelectWin(self.screen, "PLAY ", 9)
    def update(self):
        self.screen.blit(self.back_img, (0, 0))
        self.screen.fill(COLOR_SELECT_WINDOW, (MEDIUM, 0, MEDIUM, SIZE_FIELD * HEIGHT))
        self.screen.blit(self.back_img, (MEDIUM + WIDTH * 3 // 2, HEIGHT * 2), (0, 0, WIDTH * 2, HEIGHT * 4))
        draw_grid(self.screen, 0)
        self.select_win.draw_select_window()
        self.select_win.print_num_not_used()
        self.turn_button.draw_button()
        self.auto_button.draw_button()
        self.play_button.draw_button()

    def turn_select_win(self, player):
        if self.select_win == self.select_win_vert:
            self.select_win = self.select_win_hori
        else:
            self.select_win = self.select_win_vert
        self.select_win.ships_num = player.ships_num
        self.update()
        for player_ship in player.ships:
            player_ship.draw(self.screen)
        display.flip()
    def automatic_placement(self, player, AI):
            player.field = [[' '] * SIZE_FIELD for i in range(SIZE_FIELD)]
            player.ships = []
            player.log = []
            AI.add_ships(player, self.screen)
            ships_num = [0, 0, 0, 0]
            self.select_win.ships_num = player.ships_num = ships_num
            self.update()
            for player_ship in player.ships:
                player_ship.draw(self.screen)
            display.flip()
            return ships_num