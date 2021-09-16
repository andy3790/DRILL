from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def randering(x,y):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)

def move_forword(val,speed):
        val += speed
        delay(0.01)
        return val

def move_ractangle(x,y,speed):
    while x<780:
        randering(x,y)
        x = move_forword(x,speed)
    while y<560:
        randering(x,y)
        y = move_forword(y,speed)
    while x>20:
        randering(x,y)
        x = move_forword(x,-speed)
    while y>90:
        randering(x,y)
        y = move_forword(y,-speed)
    return x,y

def move_circle(x,y,rectS,speed):
    while x<400:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += rectS
        delay(0.01)
    degree = 0
    while degree<360 and degree>-360:
        randering(x,y)
        x = 400+235*math.cos(math.radians(degree - 90))
        y = 325+235*math.sin(math.radians(degree - 90))
        degree += speed
        delay(0.01)
    return x,y

x = 0
y = 90

while True:
    x,y = move_ractangle(x,y,10)
    x,y = move_circle(x,y,10,3)
    
close_canvas()
