import game_framework
from pico2d import *
from random import randint
from boy import PIXEL_PER_METER

import game_world

# Bird Fly Speed
# 10 pixel 30 cm
FLY_SPEED_KMPH = 45.0  # Km / Hour
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed
TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

# 비둘기 크기는 세로길이 32~37cm 정도에 양 날개의 길이 64~72cm 정도의 크기
# 이미지는 뚱뚱한 새 이므로 세로길이와 양 날개길이의 절반으로 측정
# 45cm정도가 적당하나 게임상 오브젝트가 너무 작으므로 약 60cm로 설정

# 비둘기는 평균 시속 123km로 비행하며 최대 시속 150km
# 주택가 같은 곳에서 45km로 천천히 비행
# 사람이 있는 곳이니 45km/h 로 비행하는 것으로 설정

# 뚱뚱하지만 날개가 작으므로 날개짓을 열심히 해야 날 수 있다
# 1초에 5번 날개짓을 하게 설정


class Bird:
    image = None
    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.x, self.y = randint(50, 1500), randint(150, 550)
        self.sizex, self.sizey = PIXEL_PER_METER / 2, PIXEL_PER_METER / 2
        self.dir = -1 ** randint(1,2)
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.dir * FLY_SPEED_PPS * game_framework.frame_time
        if self.x > 1600 - 25:
            self.dir *= -1
        elif self.x < 25:
            self.dir *= -1

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 100, 0, 100, 100, 0, '', self.x, self.y, self.sizex, self.sizey)
        elif self.dir == -1:
            self.image.clip_composite_draw(int(self.frame) * 100, 0, 100, 100, 0, 'h', self.x, self.y, self.sizex, self.sizey)