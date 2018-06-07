import pygame
from pygame import font, Rect
from const import *
from pygame.sprite import Sprite


class ButtonsSelectWin(object):
    def __init__(self, screen, msg, height):
        """
        Данный класс создает кнопки для Select Window
        :param msg: текст кнопки
        :param height: уровень на котором данная кнопка будет расположена
        """
        self.screen = screen
        self.width, self.height = 10, 10
        self.button_color = COLOR_SELECT_BUTTON
        self.text_color = BLACK
        self.font = font.SysFont(None, 39)
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.rect = Rect(MEDIUM + 4*(WIDTH // 2),
                         HEIGHT * height,
                         self.msg_image_rect.width+10,
                         self.msg_image_rect.height+10)
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """
        Данная функция рисует кнопки
        :return:
        """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class ButtonReady(ButtonsSelectWin):
    def __init__(self, screen):
        """
        Данный класс создает кнопку проверки готовности в игре
        Также он наследует функцию отрисовки кнопки из ButtonsSelectWin
        """
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.button_color = COLOR_MENU_BUTTON
        self.text_color = BLACK
        self.font = font.SysFont(None, 50)
        self.msg_image = self.font.render("READY", True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.rect = Rect(0, 0, self.msg_image_rect.width*1.5, self.msg_image_rect.height*1.5)
        self.rect.center = self.screen_rect.center
        self.msg_image_rect.center = self.rect.center

class ButtonMenu(ButtonsSelectWin):
    def __init__(self, screen, msg, row):
        """
        Данный класс создает кнопки для меню
        Также он наследует функцию отрисовки кнопки из ButtonsSelectWin
        :param msg: текст на кнопки
        :param row: строка на которой находится кнопка
        """
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.button_color = COLOR_MENU_BUTTON
        self.text_color = BLACK
        self.font = font.SysFont(None, 50)
        self.msg_image = self.font.render(msg, True, self.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.rect = Rect(0, 0, self.msg_image_rect.width+20, self.msg_image_rect.height+10)
        self.rect.center = self.screen_rect.center
        self.rect.top += 60*row
        self.msg_image_rect.center = self.rect.center

class ButtonsSettings(Sprite):
    def __init__(self, screen, type, row):
        """
        Данный класс создает кнопки назад-вперед в окне настроек
        Также он наследует класс Sprite
        :param type: функция кнопки
        :param row: строка на которой находится кнопка
        """
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        if type == 1:
            self.image = pygame.image.load('img/next.png')
        else:
            self.image = pygame.image.load('img/back.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.rect.x += type*150
        self.rect.top += row*60
    def draw(self):
        """
        Данная функция рисует кнопку
        """
        self.screen.blit(self.image, self.rect)


if __name__ == '__main__':
    print('This is buttons model')
