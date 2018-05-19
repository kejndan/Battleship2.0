__author__ = 'Adel'
import pygame
from pygame.sprite import Group
from select_window import SelectWindow
from ship import Ship, ship_cpy, check_aoe
from const import *
import graphic
import sys
from player import Player
from buttons import ButtonsSelectWin
from AI import AI





def update_screen(back_img, screen):
    """
    Обновляет экран
    """
    screen.blit(back_img, (0, 0))
    screen.fill(GREY, (MEDIUM, 0, MEDIUM, SIZE_FIELD * HEIGHT))
    screen.blit(background_image, (MEDIUM + WIDTH * 3 // 2, HEIGHT * 2), (0, 0, WIDTH * 2, HEIGHT * 4))
    graphic.draw_grid(screen, 0)

def full_draw_select_win(select_win):
    select_win.draw_select_window()
    select_win.print_num_not_used()
    turn_button.draw_button()
    auto_button.draw_button()
    ready_button.draw_button()

def drag_n_drop(drag, ship, ships_num, select_win, *pos):
    if drag:
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            ship.update((WIDTH // 2) * (pos[0] // (WIDTH // 2)), HEIGHT * (pos[1] // HEIGHT))
            drag = False
            if check_aoe(pos[0] // (WIDTH//2), pos[1] // HEIGHT, ship.length, player.field.field, select_win.vector):
                player.ships.append(ship)
                for i in range(len(ship.field)):
                    x = pos[0] // (WIDTH // 2)
                    y = pos[1] // HEIGHT
                    if select_win.vector == 1:
                        player.field.field[y][x + i] = ship.field[i]
                        player.log.append((x+i, y))
                    else:
                        player.field.field[y + i][x] = ship.field[i]
                        player.log.append((x, y+i))
            else:
                for part in ship.parts:
                    part.kill()
                ships_num[4 - ship.length] += 1
        else:
            ship.update(pos[0], pos[1])
            ship.update()
        update_screen(background_image, screen)
        full_draw_select_win(select_win)
        for part in ship.parts:
            screen.blit(part.image, (part.rect.x, part.rect.y))
        for player_ship in player.ships:
            player_ship.draw(screen)
        pygame.display.flip()
    else:
        if ships_num[4 - ship.length]:
            ships_num[4 - ship.length] -= 1
            select_win.ships_num = ships_num
            ship.update(pos[0], pos[1])
            ship.update()
            drag = True
    return drag
def turn_select_win(select_win):
    if select_win == select_win_vert:
        select_win = select_win_hori
    else:
        select_win = select_win_vert
    select_win.ships_num = ships_num
    update_screen(background_image, screen)
    full_draw_select_win(select_win)
    for player_ship in player.ships:
        player_ship.draw(screen)
    pygame.display.flip()
    return select_win
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((SIZE_FIELD*WIDTH, SIZE_FIELD*HEIGHT))
    player_1 = Player(screen)
    player_2 = Player(screen)
    ai = AI('easy')
    select_win_hori = SelectWindow(screen, 1)
    select_win_vert = SelectWindow(screen, -1)
    select_win_vert.create_select_ships()
    select_win_hori.create_select_ships()
    background_image = pygame.image.load("img/water-texture_(23).jpg").convert()
    turn_button = ButtonsSelectWin(screen, "TURN", 7)
    auto_button = ButtonsSelectWin(screen, "AUTO", 8)
    ready_button = ButtonsSelectWin(screen, "PLAY ", 9)
    update_screen(background_image, screen)
    full_draw_select_win(select_win_vert)
    pygame.display.flip()
    select_win = select_win_vert
    player = player_1
    drag = False
    ships_num = player_1.ships_num
    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if MEDIUM + 3 * WIDTH // 2 <= pos[0] <= MEDIUM + 7 * (WIDTH // 2) and HEIGHT * 2 <= pos[1] <= HEIGHT * 6:
                        for i in range(4):
                            if select_win.rect_ships[i].collidepoint(pos):
                                ship = ship_cpy(select_win.ships[i], screen)
                                drag = drag_n_drop(drag, ship, ships_num, select_win, pos[0], pos[1])
                    elif turn_button.rect.collidepoint(pos):
                        select_win = turn_select_win(select_win)
                    elif auto_button.rect.collidepoint(pos):
                        player.field.field = [[' ']*SIZE_FIELD for i in range(SIZE_FIELD)]
                        player.ships = []
                        player.log = []
                        ai.add_ships(player, screen)
                        ships_num = [0, 0, 0, 0]
                        select_win.ships_num = player.ships_num = ships_num
                        update_screen(background_image, screen)
                        full_draw_select_win(select_win)
                        for player_ship in player.ships:
                            player_ship.draw(screen)
                        pygame.display.flip()
                    elif len(player.ships) == 10 and ready_button.rect.collidepoint(pos):
                        player = player_2
                        select_win.ships_num = ships_num = player_2.ships_num
                        update_screen(background_image, screen)
                        full_draw_select_win(select_win)
                        pygame.display.flip()


                if drag:
                    pos = pygame.mouse.get_pos()
                    drag = drag_n_drop(drag, ship, ships_num, select_win,pos[0], pos[1])









