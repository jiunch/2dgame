import game_framework
import main_state

from pico2d import *

name = "VictoryState"
image = None

def enter():
    global image
    image = load_image('victory.png')

def exit():
    global image
    del(image)

def update(frame_time):
    pass

def draw(frame_time):
    global image
    clear_canvas()
    start_state.draw_main_scene(frame_time)
    image.clip_draw(count*100,0,100,100,650,200)
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

def countreturn():
    global count
    return count

def countnum():
    global count

    return count

def pause(): pass

def resume(): pass
