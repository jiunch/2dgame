import random

from pico2d import *

class Nomal_enemy:

    PIXEL_PER_METER = (10.0 / 0.5)           # 10 pixel 50 cm
    RUN_SPEED_KMPH = 18.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    image = None

    LEFT_RUN, ATTACK , DIE = 0, 1, 2

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0
        self.state = self.LEFT_RUN
        if Nomal_enemy.image == None:
            Nomal_enemy.image = load_image('nomal_enemy.png')

    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        distance = Nomal_enemy.RUN_SPEED_PPS * frame_time
        self.total_frames += Nomal_enemy.FRAMES_PER_ACTION * Nomal_enemy.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4
        self.x += (self.dir * distance)
        self.x = clamp(0, self.x, 800)

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

    def handle_event(self, event):
        self.state = self.LEFT_RUN





