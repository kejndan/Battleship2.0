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







def swap(player):
    if player == player_2:
        player = player_1
        enemy_player = player_2
    else:
        player = player_2
        enemy_player = player_1
    return (player, enemy_player)

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



    Menu.draw_menu()
    pygame.display.flip()



    # background_image = pygame.image.load("img/water-texture_(23).jpg").convert()

    # ready_button = ButtonReady(screen)
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
                        ship = Event.select_window(pos, Select, event,  AI, player_1, player_2)
                if Event.drag:
                    Event.drag_n_drop(event, Event.ship,  Select, pos)









            #     if not game:
            #         if event.type == pygame.MOUSEBUTTONDOWN:
            #             pos = pygame.mouse.get_pos()

            #
            #     if game:
            #         pos = pygame.mouse.get_pos()
            #         if not ready:
            #             screen.blit(background_image, (0, 0))
            #             draw_grid(screen, 0)
            #             draw_grid(screen, 1)
            #             ready_button.draw_button()
            #             pygame.display.flip()
            #             if event.type == pygame.MOUSEBUTTONDOWN and ready_button.rect.collidepoint(pos):
            #
            #                 screen.blit(background_image, (0, 0))
            #                 draw_grid(screen, 0)
            #                 draw_grid(screen, 1)
            #                 for ship in player.ships:
            #                     ship.draw(screen)
            #                 ready = True
            #                 pygame.display.flip()
            #             player, enemy_player = swap(player)
            #         else:
            #             if event.type == pygame.MOUSEBUTTONDOWN:
            #                 if not player.attack(pos, enemy_player):
            #                     ready = False
            #                 screen.blit(background_image, (0, 0))
            #                 draw_grid(screen, 0)
            #                 draw_grid(screen, 1)
            #                 for ship in player.ships:
            #                     ship.draw(screen)
            #                 for part in player.parts_enemy_ship:
            #                     screen.blit(part.image, (part.rect.x, part.rect.y))
                pygame.display.flip()