import game_framework
import select_state
import main_state
from pico2d import *

name = "StartState"

image = None


def enter():
    global image
    open_canvas(1300,700)
    image = load_image('start_map.png')

def exit():
    global image
    del(image)
    close_canvas()

def update():
        pass

def draw():
    clear_canvas()
    image.draw(650,350)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.push_state(select_state)

def draw_main_scene():
    image.draw(650,350)

def pause():
    pass

def resume():
    pass