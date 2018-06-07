from const import *
import pygame
from ship import check_aoe, ship_cpy
from graphic import draw_grid
class Event(object):
    def __init__(self, screen, player):
        self.screen = screen
        self.settings = False
        self.menu = True
        self.select = False
        self.drag = False
        self.player = player
        self.ready = False
        self.game = False
        self.first_stage_attack = True
        self.second_stage_attack = False
        self.third_stage_attack = False
        self.ships_num = [1, 2, 3, 4]
        self.ship = 0

    def event_menu(self, Menu, pos, Select):
        if Menu.button_play.msg_image_rect.collidepoint(pos):
            self.select = True
            self.menu = False
            Menu.game_type = Menu.game_types[Menu.button_gt_i]
            Menu.complexity = Menu.complexity_types[Menu.button_comp_i]
            Select.update()
        elif Menu.button_set.msg_image_rect.collidepoint(pos):
            self.menu = False
            self.settings = True
            Menu.draw_settings()

    def event_settings(self, Menu, pos):
        if Menu.button_back.rect.collidepoint(pos):
            self.menu = True
            self.settings = False
            Menu.draw_menu()
        else:
            if Menu.button_next_comp.rect.collidepoint(pos):
                Menu.button_comp_i += 1
            elif Menu.button_back_comp.rect.collidepoint(pos):
                Menu.button_comp_i -= 1
            elif Menu.button_next_gt.rect.collidepoint(pos):
                Menu.button_gt_i += 1
            elif Menu.button_back_gt.rect.collidepoint(pos):
                Menu.button_gt_i -= 1
            Menu.button_comp_i %= 3
            Menu.button_gt_i %= 2
            Menu.print_game_type = Menu.font_settings.render(Menu.game_types[Menu.button_gt_i],
                                                             True, Menu.text_color, None)
            Menu.print_complexity = Menu.font_settings.render(Menu.complexity_types[Menu.button_comp_i],
                                                              True, Menu.text_color,None)
            Menu.draw_settings()

    def in_select_window(self, pos):
        if MEDIUM + 3 * WIDTH // 2 <= pos[0] <= MEDIUM + 7 * (WIDTH // 2) and HEIGHT * 2 <= pos[1] <= HEIGHT * 6:
            return True
        else:
            return False

    def drag_n_drop(self, event, ship,  Select,  pos):
        if self.drag:
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                ship.update((WIDTH // 2) * (pos[0] // (WIDTH // 2)), HEIGHT * (pos[1] // HEIGHT))
                self.drag = False
                if check_aoe(pos[0] // (WIDTH // 2), pos[1] // HEIGHT, ship.length, self.player.field, Select.select_win.vector):
                    self.player.ships.append(ship)
                    for i in range(len(ship.field)):
                        x = pos[0] // (WIDTH // 2)
                        y = pos[1] // HEIGHT
                        if Select.select_win.vector == 1:
                            self.player.field[y][x + i] = ship.field[i]
                            self.player.log.append((x + i, y))
                        else:
                            self.player.field[y + i][x] = ship.field[i]
                            self.player.log.append((x, y + i))
                else:
                    for part in ship.parts:
                        part.kill()
                    self.ships_num[4 - ship.length] += 1
            else:
                ship.update(pos[0], pos[1])
                ship.update()
            Select.update()
            for part in ship.parts:
                self.screen.blit(part.image, (part.rect.x, part.rect.y))
            for player_ship in self.player.ships:
                player_ship.draw(self.screen)
            pygame.display.flip()
        else:
            if self.ships_num[4 - ship.length]:
                self.ships_num[4 - ship.length] -= 1
                Select.select_win.ships_num = self.player.ships_num = self.ships_num
                ship.update(pos[0], pos[1])
                ship.update()
                self.drag = True

    def select_window(self, pos, Select, event,  AI, player_1, player_2, BF, Menu):
        if self.in_select_window(pos):
            for i in range(4):
                if Select.select_win.rect_ships[i].collidepoint(pos):
                    self.ship = ship_cpy(Select.select_win.ships[i], self.screen)
                    self.drag_n_drop(event, self.ship,  Select,  pos)
        elif Select.turn_button.rect.collidepoint(pos):
            Select.turn_select_win(self.player)
        elif Select.auto_button.rect.collidepoint(pos):
            self.ships_num = Select.automatic_placement(self.player, AI)
            for field in self.player.field:
                print(field)
            print()
        elif len(self.player.ships) == 10 and Select.play_button.rect.collidepoint(pos):
            if self.player == player_1:
                self.player = player_2
                if Menu.game_type == 'PvP':
                    Select.select_win.ships_num = self.ships_num = player_2.ships_num
                    Select.update()
                    pygame.display.flip()
                else:
                    self.ships_num = Select.automatic_placement(self.player, AI)
                    BF.draw_preparation_field()
                    pygame.display.flip()
                    BF.swap()
                    self.ready = False
                    self.game = True
                    self.select = False

            else:
                BF.swap()
                self.ready = False
                self.game = True
                self.select = False
    def attack(self, pos, BF):
        print(pos[1]//HEIGHT, pos[0]//(WIDTH//2)-10)
        if BF.enemy_player.field[pos[1]//HEIGHT][pos[0]//(WIDTH//2)-10] in ('S', 'X', 'E', ' ', 'O'):
            if not BF.player.attack(pos, BF.enemy_player):
                self.ready = False
                return ()
            else:
                return pos
        else:
            return ()


    def preparation(self, BF):
        BF.swap()
        BF.update()
        self.ready = True
        pygame.display.flip()


