import game_framework
import select_state
import main_state
from pico2d import *

name = "StartState"

image = None
press = None
bgm=None

def enter():
    global image,press,bgm
    open_canvas(1300,700,sync=True)
    image = load_image('start_map.png')
    press = load_image('press.png')
    bgm = load_music('background.mp3')
    bgm.set_volume(5)
    game_framework.reset_time()
    bgm.repeat_play()

def exit():
    global image,press
    del(image)
    del(press)
    close_canvas()

def update(frame_time):
        pass

def draw(frame_time):
    clear_canvas()
    image.draw(650,350)
    press.draw(650,150)
    update_canvas()


def handle_events(frame_time):
    global press
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.push_state(select_state)


def draw_main_scene(frame_time):
    image.draw(650,350)


def pause():
    pass

def resume():
    pass

def bgmstart():
    bgm.resume()

def bgmstop():
    bgm.stop()