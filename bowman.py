from pico2d import *


class Bowman:

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __init__(self):

        self.x, self.y = 70, 350
        self.frame=0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.image = load_image('bowman.png')

    def update(self,frame_time):
        self.life_time += frame_time
        self.total_frames += Bowman.FRAMES_PER_ACTION * Bowman.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4


    def draw(self):
        self.image.clip_draw(self.frame * 120,0, 120, 110, self.x, self.y)

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_w):
            if self.y <650 :
                self.y += 50
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_s):
            if self.y > 50:
                self.y -= 50
