from pico2d import *

from bowman import Bowman

count =0
argo=0
gotr=0
where1 = 350
where2 = 350

bowman = None

class Arrow:

    PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 30.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __init__(self):
        global where1
        bowman = Bowman()
        self.x, self.y = 70, 350
        self.frame=0
        self.life_time = 0.0
        self.dir = 1
        self.total_frames = 0.0
        self.image = load_image('arrow.png')

    def update(self,frame_time):
        self.life_time += frame_time
        distance = Arrow.RUN_SPEED_PPS * frame_time
        self.total_frames += Arrow.FRAMES_PER_ACTION * Arrow.ACTION_PER_TIME * frame_time
        self.x += (self.dir * distance)



    def draw(self):
        global count

        self.image.draw(self.x, self.y)

    def handle_event(self, event):
        global count
        bowman=Bowman()
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            count =1
            self.x=70
            self.y=bowman.yreturn()

    def get_bb(self):
        return self.x-35 , self.y-15 , self.x+35, self.y+15

    def delt(self):
        global count,gotr,where2
        gotr=0
        count=0
        self.x=100
        self.y= where2
