import game_framework
import select_state
import start_state

from pico2d import *

name = "MainState"

from Nomal_enemy import Nomal_enemy
from Background import Background
from zoom import Zoom
from bowman import Bowman
from arrow import Arrow

nomal_enemy = None
background = None
zoom = None
bowman = None
arrow = None
total = None
arto= None

count=0
vic=0
level =0
def create_world():
    global level
    global nomal_enemy,background,zoom,bowman,arrow,total,arto
    arrow = Arrow()
    bowman = Bowman()
    background = Background()
    zoom=Zoom()
    nomal_enemy = [Nomal_enemy() for i in range (3)]
    level=select_state.countreturn()

    arto=arrow
    total=nomal_enemy
    pass

def destroy_world():
    global nomal_enemy,background,zoom,bowman,arrow
    del(arrow)
    del(bowman)
    del(zoom)
    del(nomal_enemy)
    del(background)


def enter():
    open_canvas(1300,700)
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
    global arto
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
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
    global vic
    for nomal_enemy in total:
        nomal_enemy.update(frame_time)

    zoom.update(frame_time)
    bowman.update(frame_time)

    arrow.update(frame_time)

    for nomal_enemy in total:
        if collide(arrow, nomal_enemy):
            arrow.delt()
            nomal_enemy.delt()
            vic +=1
            if vic == 10:
                game_framework.change_state(victory_state)
    if collide(arrow, background):
        arrow.delt()



def draw(frame_time):
    hide_cursor()
    clear_canvas()
    background.draw()

    for nomal_enemy in total:
        nomal_enemy.draw()
    bowman.draw()
    arrow.draw()
    zoom.draw()
    pass

    update_canvas()

