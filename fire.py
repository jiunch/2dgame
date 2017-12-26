from pico2d import *

image=None

class Fire:

    TIME_PER_ACTION = 0.3
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    def __init__(self):
        self.state= 0
        self.x, self.y = 400, 100
        self.frame=0
        self.total_frames = 0.0
        self.image = load_image('images/fire.png')
        self.shotsound = load_music('sound/fire.mp3')
        self.shotsound.set_volume(16)


    def update(self,frame_time):
        self.total_frames += Fire.FRAMES_PER_ACTION * Fire.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8
        if self.frame==7:
            self.state=0

    def draw(self):
        if self.state == 1:
            self.image.clip_draw(self.frame * 150, 0, 150, 200, self.x, self.y)
            self.image.clip_draw(self.frame * 150, 0, 150, 200, self.x+100, self.y)
            self.image.clip_draw(self.frame * 150, 0, 150, 200, self.x , self.y+200)
            self.image.clip_draw(self.frame * 150, 0, 150, 200, self.x + 100, self.y+200)
            self.image.clip_draw(self.frame * 150, 0, 150, 200, self.x, self.y + 400)
            self.image.clip_draw(self.frame * 150, 0, 150, 200, self.x + 100, self.y + 400)

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            self.shotsound.play(1)
            self.state=1
            self.total_frames=0

    def get_bb(self):
        return self.x-50 , self.y-100 , self.x+150, self.y+500

    def skillstate(self):
        return self.state



