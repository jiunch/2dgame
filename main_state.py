import random
import json
import os
import start_state

from pico2d import *

import game_framework
import select_state

name = "MainState"

bowman = None
boy = None
grass = None
font = None


class Background:
    def __init__(self):
        self.image = load_image('background.png')

    def draw(self):
        self.image.draw(650,350)

class Bowman:
    def __init__(self):
        self.x, self.y = 70, 350
        self.frame = 0
        self.image = load_image('bowman.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 4
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 120,0, 120, 110, self.x, self.y)

class Nomal_enemy:
    def __init__(self):
        self.x, self.y = 1200, 300
        self.frame = 0
        self.image = load_image('test2.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def enter():
    global nomal_enemy,background,bowman
    bowman = Bowman()
    nomal_enemy = Nomal_enemy()
    background = Background()


def exit():
    global nomal_enemy,background,bowman
    del(bowman)
    del(nomal_enemy)
    del(background)

def pause():
    pass

def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(select_state)



def update():
    nomal_enemy.update()
    bowman.update()

def draw():
    clear_canvas()
    draw_main_scene()
    update_canvas()

def draw_main_scene():
    background.draw()
    nomal_enemy.draw()
    bowman.draw()


