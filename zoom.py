from pico2d import *

class Zoom:

    def __init__(self):
        self.x=0
        self.y=0
        self.image = load_image('images/zoom.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self,frame_time):
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEMOTION:
                self.x, self.y = event.x, 699 - event.y

    pass




