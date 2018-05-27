import pygame
from const import *
from pygame.sprite import Sprite
from buttons import ButtonMenu, ButtonsSettings

class Menu(object):
    complexity_types = ['EASY', 'MEDIUM', 'HARD']
    game_types = ['PvP', 'PvE']
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.background = pygame.image.load("img/bg_menu.png")
        self.font_title = pygame.font.SysFont("comicsansms", 96)
        self.text_color = BLACK
        self.title = self.font_title.render("Sea Battle", True, self.text_color, None)
        self.title_rect = self.title.get_rect()
        self.title_rect.center = self.screen_rect.center
        self.title_rect.top-=100
        self.button_play = ButtonMenu(self.screen, 'PLAY', 0)
        self.button_set = ButtonMenu(self.screen, 'SETTINGS', 1)
        self.button_comp_i = 0
        self.button_gt_i = 0
        self.game_type = self.game_types[self.button_gt_i]
        self.complexity = self.complexity_types[self.button_comp_i]
        self.font_settings = pygame.font.SysFont(None, 50)
        self.print_game_type = self.font_settings.render(self.game_type, True, self.text_color, None)
        self.print_complexity = self.font_settings.render(self.complexity, True, self.text_color, None)
        self.print_game_type_rect = self.print_game_type.get_rect()
        self.print_complexity_rect = self.print_complexity.get_rect()
        self.print_complexity_rect.center = self.print_game_type_rect.center = self.screen_rect.center
        self.print_complexity_rect.top += 60
        self.button_next_comp = ButtonsSettings(self.screen, 1, 1)
        self.button_back_comp = ButtonsSettings(self.screen, -1, 1)
        self.button_next_gt = ButtonsSettings(self.screen, 1, 0)
        self.button_back_gt = ButtonsSettings(self.screen, -1, 0)
        self.button_back = ButtonMenu(screen,'BACK', 2)



    def draw_menu(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.title, self.title_rect)
        self.button_play.draw_button()
        self.button_set.draw_button()
    def draw_settings(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.title, self.title_rect)
        self.screen.blit(self.print_game_type, self.print_game_type_rect)
        self.screen.blit(self.print_complexity, self.print_complexity_rect)
        self.button_next_comp.draw()
        self.button_back_comp.draw()
        self.button_next_gt.draw()
        self.button_back_gt.draw()
        self.button_back.draw_button()





