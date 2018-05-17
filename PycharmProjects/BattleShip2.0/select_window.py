from const import *
import pygame
from ship import Ship
from pygame.sprite import Group

class SelectWindow:
    def __init__(self, screen, vector):
        self.ships_num = [1, 2, 3, 4]
        self.ships = []
        self.rect_ships = []
        self.screen = screen
        self.vector = vector
        self.x = MEDIUM + 3*(WIDTH//2)
        self.y = HEIGHT*2

    def draw_select_window(self):
        for ship in self.ships:
            ship.draw(self.screen)


    def create_select_ships(self):
        for i in range(3, -1, -1):
            if self.vector == 1:
                self.rect_ships.append(pygame.Rect(self.x, self.y + (3-i)*HEIGHT, (i+1)*WIDTH//2, HEIGHT))
                self.ships.append(Ship(i+1, self.x + WIDTH//2, self.y + (3-i)*HEIGHT, self.vector, 0, self.screen))
            elif self.vector == -1:
                self.rect_ships.append(pygame.Rect(self.x + (3-i)*WIDTH//2, self.y, WIDTH//2, (i+1)*HEIGHT))
                self.ships.append(Ship(i+1, self.x + (4-i)*WIDTH//2, self.y, self.vector, 0, self.screen))


    def print_num_not_used(self):
        """
        Функция отображающая количество не использованных корбалей
        """
        font = pygame.font.SysFont(None, 48)
        for i in range(4):
            ship = self.ships_num[i]
            num = str(ship)
            num_image = font.render(num, True, BLACK)
            num_rect = num_image.get_rect()
            if self.vector == 1:
                num_rect.top = HEIGHT * 2 + 5 + i * HEIGHT
                num_rect.right = MEDIUM + 100
                self.screen.blit(num_image, num_rect)
            else:
                num_rect.top = HEIGHT + 5
                num_rect.right = MEDIUM + 136 + i * WIDTH // 2
                self.screen.blit(num_image, num_rect)
