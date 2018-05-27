__author__ = 'Adel'
import pygame
from select_window import SelectWindow
from ship import Ship, ship_cpy, check_aoe
from const import *
from graphic import  draw_grid
import sys
from settings import Settings
from player import Player
from buttons import ButtonsSelectWin, ButtonReady
from AI import AI
from menu import Menu
from event import Event
from select import Select
from battlefield import BattleField









if __name__ == '__main__':
    pygame.init()


    screen = pygame.display.set_mode((SIZE_FIELD*WIDTH, SIZE_FIELD*HEIGHT))
    Menu = Menu(screen)
    Settings = Settings(screen)

    Select = Select(screen)
    player_1 = Player(screen)
    player_2 = Player(screen)
    Event = Event(screen, player_1)
    AI = AI(Settings.complexity)
    BF = BattleField(screen, player_1, player_2)



    Menu.draw_menu()
    pygame.display.flip()



    # background_image = pygame.image.load("img/water-texture_(23).jpg").convert()


    # update_screen_select(background_image, screen)
    # full_draw_select_win(select_win, turn_button, auto_button, play_button)
    # pygame.display.flip()
    player = player_1
    # drag = False
    # game = False
    # ships_num = player_1.ships_num
    while True:
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    sys.exit()
                if Event.menu:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Event.event_menu(Menu, pos, Select)
                elif Event.settings:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Event.event_settings(Menu,pos)
                elif Event.select:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        Event.select_window(pos, Select, event,  AI, player_1, player_2, BF)
                elif Event.game:
                    if Event.ready:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            Event.attack(pos, BF)
                            BF.update()
                    else:
                        BF.draw_preparation_field(BF)
                        if event.type == pygame.MOUSEBUTTONDOWN and BF.ready_button.rect.collidepoint(pos):
                            Event.preparation(BF)


                if Event.drag:
                    Event.drag_n_drop(event, Event.ship,  Select, pos)









            #     if not game:
            #         if event.type == pygame.MOUSEBUTTONDOWN:
            #             pos = pygame.mouse.get_pos()

            #
            #     if game:
            #         pos = pygame.mouse.get_pos()
            #         if not ready:
            #
            #         else:
            #             if event.type == pygame.MOUSEBUTTONDOWN:

                pygame.display.flip()