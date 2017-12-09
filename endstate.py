import game_framework
import start_state
import main_state

from pico2d import *

name = "EndeState"
image = None

def enter():
    global image
    image = load_image('victory .png')

def exit():
    global image
    del(image)

def update(frame_time):
    pass

def draw(frame_time):
    global image
    clear_canvas()
    main_state.draw(frame_time)
    image.draw(350,650)
    update_canvas()

def handle_events(frame_time):
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
