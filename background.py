import random

from pico2d import *

class Background:

    def __init__(self):
        self.image = load_image('background.png')
        self.x =650.0
        self.y=350.0

    def draw(self):
        self.image.draw(650, 350)

    def get_bb(self):
        return self.x+640 , self.y-350 , self.x+650, self.y+350




