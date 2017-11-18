import game_framework
import select_state
import start_state

from pico2d import *

name = "MainState"

from Nomal_enemy import Nomal_enemy
from Background import Background

nomal_enemy = None
background = None

def create_world():
    global nomal_enemy,background
    nomal_enemy = Nomal_enemy()
    backfround = Background()

    pass

def destroy_world():
    global nomal_enemy,background

    del(nomal_enemy)
    del(background)


def enter():
    open_canvas(1300,700)

    create_world()

def exit():
    destroy_world()
    close_canvas()

def pause():
    pass

def resume():
    pass

def handel_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                Nomal_enemy.handle_event(event)


def update(frame_time):
    nomal_enemy.update(frame_time)

    pass


def draw(frame_time):
    clear_canvas()
    background.draw()
    nomal_enemy.draw()

    update_canvas()
    pass