__author__ = 'Adel'
import pygame
from pygame.sprite import Group
from select_window import SelectWindow
from ship import Ship
from const import *
import graphic
import sys
from player import Player
from buttons import ButtonTurn

def ship_cpy(ship,  screen):
    field = [[' ']*SIZE_FIELD for i in range(SIZE_FIELD)]
    return Ship(ship.length, ship.x, ship.y, ship.vector,  screen)

def check_aoe(x,y, length, field):
    x = x // (WIDTH//2)
    y = y // HEIGHT
    for i in range(-1, length+1):
        for j in range(-1, 1):
            try:
                if y+i == -1 or x+j == -1:
                    raise IndexError
                if select_win.vector == -1:
                    if x+j>10 or y+i > 10 or field[y+i][x+j] != ' ':
                        return False
                elif select_win.vector == 1:
                    if x + i > 10 or y + j > 10 or field[y+j][x+i] != ' ':
                        return False
            except IndexError:
                pass
    return True


def update_screen(back_img, screen):
    screen.blit(back_img, (0, 0))
    screen.fill(GREY, (MEDIUM, 0, MEDIUM, SIZE_FIELD * HEIGHT))
    screen.blit(background_image, (MEDIUM + WIDTH * 3 // 2, HEIGHT * 2), (0, 0, WIDTH * 2, HEIGHT * 4))
    graphic.draw_grid(screen, 0)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((SIZE_FIELD*WIDTH, SIZE_FIELD*HEIGHT))
    player_1 = Player(screen)
    player_2 = Player(screen)
    select_win_hori = SelectWindow(screen, 1)
    select_win_vert = SelectWindow(screen, -1)
    select_win_vert.create_select_ships()
    select_win_hori.create_select_ships()
    background_image = pygame.image.load("img/water-texture_(23).jpg").convert()
    turn_button = ButtonTurn(screen)
    update_screen(background_image, screen)
    select_win_vert.draw_select_window()
    select_win_vert.print_num_not_used()
    turn_button.draw_button()
    pygame.display.flip()
    select_win = select_win_vert
    drag = False
    ships_num = player_1.ships_num
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(player_1.field.field)
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if MEDIUM + 3 * WIDTH // 2 <= pos[0] <= MEDIUM + 7 * (WIDTH // 2) and HEIGHT * 2 <= pos[1] <= HEIGHT * 6:
                    for i in range(4):
                        if select_win.rect_ships[i].collidepoint(pos):
                            ship = ship_cpy(select_win.ships[i], screen)
                            if ships_num[4 - ship.length]:
                                ships_num[4 - ship.length] -= 1
                                select_win.ships_num = ships_num
                                ship.update(pos[0], pos[1])
                                ship.update()
                                drag = True
                elif turn_button.rect.collidepoint(pos):
                    if select_win == select_win_vert:
                        select_win = select_win_hori
                    else:
                        select_win = select_win_vert
                    select_win.ships_num = ships_num
                    update_screen(background_image, screen)
                    select_win.draw_select_window()
                    select_win.print_num_not_used()
                    turn_button.draw_button()
                    for player_ship in player_1.ships:
                        player_ship.draw(screen)
                    pygame.display.flip()
            if drag:
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    ship.update((WIDTH//2)*(pos[0]//(WIDTH//2)), HEIGHT*(pos[1]//HEIGHT))
                    drag = False
                    if check_aoe(pos[0], pos[1], ship.length, player_1.field.field):
                        player_1.ships.append(ship)
                        for i in range(len(ship.field)):
                            if select_win.vector == 1:
                                player_1.field.field[pos[1]//HEIGHT][pos[0]//(WIDTH//2) + i] = ship.field[i]
                            else:
                                player_1.field.field[pos[1]//HEIGHT + i][pos[0]//(WIDTH//2)] = ship.field[i]
                    else:
                        for part in ship.parts:
                            part.kill()
                        ships_num[4 - ship.length] +=1
                else:
                    ship.update(pos[0], pos[1])
                    ship.update()
                update_screen(background_image, screen)
                select_win.draw_select_window()
                turn_button.draw_button()
                select_win.print_num_not_used()
                for part in ship.parts:
                    screen.blit(part.image, (part.rect.x, part.rect.y))
                for player_ship in player_1.ships:
                    player_ship.draw(screen)
                pygame.display.flip()








