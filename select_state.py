import game_framework
import start_state
import main_state

from pico2d import *

name = "PauseState"
image = None
logo_time = 0.0
count=0

def enter():
    global image
    image = load_image('number.png')


def exit():
    global image
    del(image)

def update():
    pass

def draw():
    global image
    clear_canvas()
    start_state.draw_main_scene()
    image.clip_draw(count*100,0,100,100,650,200)
    update_canvas()

def handle_events():
    global count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_state()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            if(count<8):
                count += 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            if(count>0):
                count -= 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE :
            game_framework.change_state(main_state)


    pass


def pause(): pass

def resume(): pass
