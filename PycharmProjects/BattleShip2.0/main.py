__author__ = 'Adel'
import pygame
from const import *
import sys
from player import Player
from AI import AI as AI_helper
from menu import Menu as Start_Menu
from event import Event as Event_in_game
from select import Select as Select_Window
from battlefield import BattleField
from graphic import draw_congratulation

if __name__ == '__main__':
    # Инициализируем объекты
    pygame.init()
    screen = pygame.display.set_mode((SIZE_FIELD*WIDTH, SIZE_FIELD*HEIGHT))
    pygame.display.set_caption('Sea Battle')
    Menu = Start_Menu(screen)
    Select = Select_Window(screen)
    player_1 = Player(screen, 'Player 1')
    player_2 = Player(screen, 'Player 2')
    Event = Event_in_game(screen, player_1)
    AI = AI_helper()
    BF = BattleField(screen, player_1, player_2)
    Menu.draw_menu()
    pygame.display.flip()
    player = player_1

    while True:
            # цикл отслеживающий события
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    sys.exit()
                if Event.menu: # если пользователь находится в меню
                    if event.type == pygame.MOUSEBUTTONUP:
                        Event.event_menu(Menu, pos, Select)
                elif Event.settings: # если пользователь находится в настройках
                    if event.type == pygame.MOUSEBUTTONUP:
                        Event.event_settings(Menu,pos)
                elif Event.select: # если пользователь находится в окне выбора
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        Event.select_window(pos, Select, event,  AI, player_1, player_2, BF, Menu)
                elif Event.game: # если пользователь находится играет
                    if Menu.game_type == 'PvP': # если включен режим игрок против игрока
                        if Event.ready: # если игрок готов
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                Event.attack(pos, BF)
                                BF.update()
                        else:
                            BF.draw_preparation_field()
                            if event.type == pygame.MOUSEBUTTONDOWN and BF.ready_button.rect.collidepoint(pos):
                                Event.preparation(BF)
                    else: # если включен режим игрок против компьютера
                        if BF.player == player_1: # если ход пользователя
                            if Event.ready: # если игрок готов
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Event.attack(pos, BF)
                                    BF.update()
                            else:
                                Event.ready = True
                                BF.swap()

                        else: # если ход компьютера
                            if Event.ready:
                                if Event.first_stage_attack: # если компьютер ещё не попал по кораблю
                                    point = Event.attack(AI.auto_attack(player_1, Menu), BF)
                                    BF.update2()
                                    if point: # если компьютер попал
                                        ship = AI.search_ship((point[0] - MEDIUM, point[1]), player_1)
                                        if ship.num_deck != 0: #проверка на уничтожение корабля
                                            Event.first_stage_attack = False
                                            Event.second_stage_attack = True
                                            Attack = AI.AOE_attack(point)
                                            old_point = point
                                elif Event.second_stage_attack: # если компютер попал по кораблю и он вычисляет положение корабля
                                    point = Event.attack(next(Attack), BF)
                                    BF.update2()
                                    if point: # если компьютер попал
                                        if ship.num_deck != 0: #проверка на уничтожение корабля
                                            vec = (old_point[0]-point[0], old_point[1] - point[1])
                                            Event.second_stage_attack = False
                                            Event.third_stage_attack = True
                                        else:
                                            Event.second_stage_attack = False
                                            Event.first_stage_attack = True


                                elif Event.third_stage_attack: # если компьютер вычислел положение корабля
                                    for part in ship.parts:
                                        if part.image != player.hit_img and part.image != player.kill_img:
                                            Event.attack((part.x+MEDIUM-(WIDTH//2), part.y), BF)
                                            BF.update2()
                                    Event.third_stage_attack = False
                                    Event.first_stage_attack = True
                            else:
                                Event.ready = True
                                BF.update2()
                                BF.swap()

                if Event.drag: # если мы перетаскиваем корабль
                    Event.drag_n_drop(event, Event.ship,  Select, pos)
                if player_1.check_win() or player_2.check_win(): # проверка на победу
                    Event.game = False
                    if player_1.check_win():
                        draw_congratulation(player_1,screen, Menu)
                    else:
                        draw_congratulation(player_2, screen, Menu)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Menu.button_restart.rect.collidepoint(pos):
                                sys.exit()
                pygame.display.flip()