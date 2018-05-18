from const import *


class Field(object):
    def __init__(self):
        self.field = [[' ']*SIZE_FIELD for i in range(SIZE_FIELD)]
        self.list_ships = {}
