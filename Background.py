from pico2d import *

class Background:

    def __init__(self):
        self.image = load_image('background.png')
        self.x =650.0
        self.y= 350.0

    def draw(self):
        self.image.draw(400, 350)




