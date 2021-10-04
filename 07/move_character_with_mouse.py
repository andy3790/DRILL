from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def move_character():
    global mx, my
    global x, y
    global flip
    move_x = (mx - x) / 80
    move_y = (my - y) / 80
    x = x + move_x
    y = y + move_y
    if x < mx:
        flip = 0
    else:
        flip = 1


def handle_events():
    global running
    global mx, my
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.type == SDLK_ESCAPE:
            running = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)

# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse_image = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
mx, my = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
speed = 0
flip = 0

hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if flip == 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100, 100)
    mouse_image.draw(mx, my)
    update_canvas()

    if speed >= 20:
        frame = (frame + 1) % 8
        speed = 0
    move_character()
    speed = speed + 1

    handle_events()

close_canvas()




