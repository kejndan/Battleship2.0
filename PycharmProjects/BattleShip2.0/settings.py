from menu import Menu

class Settings(Menu):
    def __init__(self, screen):
        super().__init__(screen)
        self.button_play = None
        self.button_set = None

