from pico2d import *

import game_framework
import endstate
import start_state

from bowman import Bowman
from nomal_enemy import Nomal_enemy
from arrow import Arrow
from background import Background
from zoom import Zoom

name = "Main_state"

nomal_enemy = None
bowman = None
arrow = None
background = None
zoom = None

arrownum=0
Life = 1

def create_world():
    global bowman,nomal_enemy,arrow,background,zoom
    bowman = Bowman()
    arrow = Arrow()
    nomal_enemy = [Nomal_enemy() for i in range (3)]
    background = Background()
    zoom = Zoom()

    arrow.startdot(bowman)
    pass

def destroy_world():
    global bowman,nomal_enemy,arrow,background,zoom

    del(bowman)
    del(nomal_enemy)
    del(arrow)
    del(background)
    del(zoom)



def enter():
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global arrownum
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif Life ==0:
            game_framework.change_state(endstate)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(start_state)
        else:
            bowman.handle_event(event)
            arrow.handle_event(event)


def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def update(frame_time):
    global Life
    bowman.update(frame_time)
    arrow.update(frame_time)
    for i in range(3):
        if collide(arrow,nomal_enemy[i]):
            arrow.deletearrow()
            nomal_enemy[i].deleteenemy()
            Life -=1
    if collide(arrow,background) :
        arrow.deletearrow()
    for i in range(3):
        nomal_enemy[i].update(frame_time)

def draw(frame_time):
    clear_canvas()
    background.draw()
    bowman.draw()
    arrow.draw()
    for i in range(3):
        nomal_enemy[i].draw()
    pass

    update_canvas()






