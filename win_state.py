import game_framework
import select_state
import main_state
from pico2d import *

name = "Winstate"

image = None
bgm=None
def enter():
    global image,bgm
    image = load_image('images/victory.png')
    bgm = load_music('sound/victory.mp3')
    bgm.set_volume(8)
    bgm.repeat_play()

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