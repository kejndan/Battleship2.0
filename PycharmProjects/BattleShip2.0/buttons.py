from pygame import font, Rect
from const import *


class ButtonTurn(object):
    def __init__(self, screen):
        self.screen = screen

        self.width, self.height = 10, 10
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = font.SysFont(None, 39)

        self.msg_image = self.font.render("TURN", True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.rect = Rect(MEDIUM + 4*(WIDTH // 2),
                         HEIGHT * 7,
                         self.msg_image_rect.width,
                         self.msg_image_rect.height)
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)