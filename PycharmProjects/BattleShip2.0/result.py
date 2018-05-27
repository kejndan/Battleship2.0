from const import *
import pygame
class Result:
    def __init__(self, screen):
        self.screen = screen
        self.rect_screen = self.screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = GREEN
        self.text_color = BLACK
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.rect_screen.center
         self.hit = 'HIT'
        self.kill = 'KILL'
        self.miss = 'MISS'
    def prep_img(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def printed(self, msg):
        self.screen.fill(self.button_color, self.rect)
        self.screen.fill(self.)