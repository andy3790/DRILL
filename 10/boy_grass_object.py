from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.image = load_image('run_animation.png')
        self.frame = random.randint(0, 7+1)

    def update(self):
        self.x += random.randint(1, 5)
        self.frame = (self.frame+1)%8

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        if random.randint(1,2) == 2:
            # self.image = load_image('ball41x41.png')
            self.size = 41
        else:
            # self.image = load_image('ball21x21.png')
            self.size = 21
        self.image = load_image('ball'+str(self.size)+'x'+str(self.size)+'.png')
        self.speed = random.randint(5, 10)

    def update(self):
        self.y -= self.speed
        if self.y <= 50 + self.size/2:
            self.y = 50 + self.size/2

    def draw(self):
        self.image.draw(self.x,self.y)

def handle_events():
    global running
    global waiting
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

grass = Grass() # create
team = [Boy() for i in range(1, 11+1)]
balls = [Ball() for i in range(1, 20+1)]

running = True
# game main loop code
while running:
    handle_events()
    #game logic
    for boy in team:
        boy.update()
    for ball in balls:
        ball.update()
    #game drawing
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    update_canvas()

    delay(0.1)

# finalization code
close_canvas()