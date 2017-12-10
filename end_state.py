import game_framework
import start_state
import main_state
import select_state
from pico2d import *

name = "EndState"

image = None
bgm = None
def enter():
    global image,bgm
    image = load_image('defeat.png')
    bgm = load_music('defeat.mp3')
    bgm.set_volume(32)
    bgm.play(1)

def exit():
    global image
    del(image)
    bgm.stop()

def update(frame_time):
        pass

def draw(frame_time):
    clear_canvas()
    image.draw(650,350)
    update_canvas()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(select_state)

def draw_main_scene(frame_time):
    image.draw(650,350)

def pause():
    pass

def resume():
    pass