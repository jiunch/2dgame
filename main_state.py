from pico2d import *

import game_framework
import end_state
import select_state
import win_state
from bowman import Bowman
from nomal_enemy import Nomal_enemy
from arrow import Arrow
from background import Background
from fire import Fire

name = "Main_state"

nomal_enemy = None
bowman = None
arrow = None
background = None
fire=None

skillpoint=0
enemynum=0
enemycount=0
arrownum=0

Winpoint=0
Wintennum = Winpoint // 10
Winonenum = Winpoint % 10

Life = 0
Lifetennum = Life // 10
Lifeonenum = Life % 10

number=None
skillnum=None

def create_world():
    global bowman,nomal_enemy,arrow,background,number,fire,skillnum
    bowman = Bowman()
    arrow = [Arrow() for i in range(3)]
    nomal_enemy = [Nomal_enemy() for i in range (3)]
    background = Background()
    for i in range(3):
        arrow[i].startdot(bowman)
    number = load_image('images/countnum.png')
    skillnum = load_image('images/skillpoint.png')
    fire=Fire()


    pass

def destroy_world():
    global bowman,nomal_enemy,arrow,background,number,fire,skillnum
    del(bowman)
    del(nomal_enemy)
    del(arrow)
    del(background)
    del(number)
    del(fire)
    del(skillnum)

def enter():
    global Life,Winpoint,enemycount,enemynum,arrownum,skillpoint
    game_framework.reset_time()
    Life=10-select_state.level()
    Winpoint=15+select_state.level()*10
    enemynum = 1
    enemycount = 0
    arrownum = 0
    skillpoint=0
    create_world()

def exit():
    destroy_world()

def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global arrownum,skillpoint
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(select_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if arrownum<3:
                arrownum+=1
            for i in range(arrownum):
                    arrow[i].handle_event(event)
        else:
            bowman.handle_event(event)
            if skillpoint==10:
                fire.handle_event(event)

def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def update(frame_time):
    global Life,Winpoint,Lifeonenum,Lifetennum,Winonenum,Wintennum,enemynum,enemycount,arrownum,fire,skillpoint
    bowman.update(frame_time)
    fire.update(frame_time)
    for i in range(3):
        arrow[i].update(frame_time)
    if enemycount<90:
        enemycount+=1
    enemynum = enemycount // 30
    Lifetennum = Life // 10
    Lifeonenum = Life % 10
    Wintennum = Winpoint // 10
    Winonenum = Winpoint % 10

    for j in range(3):
        for i in range(3):
            if collide(arrow[j],nomal_enemy[i]):
                arrow[j].deletearrow()
                nomal_enemy[i].deleteenemy()
                Winpoint-=1
                arrownum-=1
                nomal_enemy[i].hit()
                if skillpoint<10:
                    skillpoint+=1

    if fire.skillstate() == 1 and skillpoint > 1:
        skillpoint -= 1
        for i in range(3):
            if collide(fire, nomal_enemy[i]):
                nomal_enemy[i].deleteenemy()
                Winpoint -= 1


    for i in range(3):
        if collide(arrow[i],background) :
            arrow[i].deletearrow()
            arrownum-=1

    for i in range(3):
        if collide(bowman, nomal_enemy[i]):
            nomal_enemy[i].deleteenemy()
            Life -= 1

    for i in range(enemynum):
        nomal_enemy[i].update(frame_time)

    if Life <=0:
        game_framework.change_state(end_state)
    if Winpoint <= 0:
        game_framework.change_state(win_state)


def draw(frame_time):
    global enemynum
    clear_canvas()
    background.draw()
    number.clip_draw(Lifeonenum * 50, 0, 50, 50, 480, 640)
    number.clip_draw(Lifetennum * 50, 0, 50, 50, 440, 640)

    number.clip_draw(Winonenum * 50, 0, 50, 50, 1070, 640)
    number.clip_draw(Wintennum * 50, 0, 50, 50, 1030, 640)

    if skillpoint == 10:
        skillnum.draw(1250,50)

    bowman.draw()

    for i in range(3):
        arrow[i].draw()

    for i in range(enemynum):
        nomal_enemy[i].draw()


    fire.draw()

    pass

    update_canvas()






