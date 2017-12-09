from pico2d import *

class Bowman:
    PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 40.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    image = None
    STAND,UP,DOWN = 0, 1, 2

    def __init__(self):

        self.x, self.y = 70, 350
        self.frame=0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir=0
        self.state = self.STAND
        self.image = load_image('bowman.png')
        pass

    def update(self,frame_time):

        def clamp(minimum, y, maximum):
            return max(100, min(y, 300))

        self.life_time += frame_time
        distance = Bowman.RUN_SPEED_PPS * frame_time
        self.y += (self.dir * distance)
        self.total_frames += Bowman.FRAMES_PER_ACTION * Bowman.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 120,0, 120, 110, self.x, self.y)

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_w):
            if self.state in (self.STAND, self.DOWN):
                self.state = self.UP
                self.dir = 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_s):
            if self.state in (self.STAND, self.UP):
                self.state = self.DOWN
                self.dir = -1
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_w):
            if self.state in (self.UP,):
                self.state = self.STAND
                self.dir = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_s):
            if self.state in (self.DOWN,):
                self.state = self.STAND
                self.dir = 0

