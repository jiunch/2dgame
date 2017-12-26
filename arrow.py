from pico2d import *

from bowman import Bowman

bowman = None


class Arrow:

    PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 50 cm
    RUN_SPEED_KMPH = 120.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    STOP , SHOT = 0,1

    def __init__(self):
        self.state = self.STOP
        self.x, self.y = 70, 0
        self.frame=0
        self.life_time = 0.0
        self.dir = 0
        self.total_frames = 0.0
        self.image = load_image('images/arrow.png')
        self.shotsound = load_music('sound/shot.mp3')
        self.shotsound.set_volume(8)

    def startdot(self, bowman):
        self.man = bowman
        self.x = self.man.x
        self.y=self.man.y

    def update(self,frame_time):
        distance = Arrow.RUN_SPEED_PPS * frame_time
        self.total_frames += Arrow.FRAMES_PER_ACTION * Arrow.ACTION_PER_TIME * frame_time
        self.x += (self.dir * distance)
        if self.state == self.STOP :
            self.y =self.man.y

    def draw(self):
        if self.state==self.SHOT:
            self.image.draw(self.x, self.y)

    def handle_event(self, event):
        if self.state==self.STOP:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                self.state = 1
                self.dir=1
                self.shotsound.play(1)

    def get_bb(self):
        return self.x-35 , self.y-15 , self.x+35, self.y+15

    def deletearrow(self):
        self.state=self.STOP
        self.x=self.man.x
        self.dir=0



