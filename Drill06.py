from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1240, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')


def handle_events():
    global running, idle
    global x, y
    global point_list
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
            idle = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
            point_list.append(x)
            point_list.append(y)
            idle=False
            running=True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
            idle = False


point_list = []

idle = True
running = False
char_x, char_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
x, y = 0, 0
frame = 0
hide_cursor()

while idle:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(x, y)
    character.clip_draw(frame * 100, 100 * 0, 100, 100, char_x, char_y)
    frame = (frame + 1) % 8
    delay(0.05)
    update_canvas()
    handle_events()

while running:
    x1, y1 = char_x, char_y
    x2, y2 = point_list[0], point_list[1]
    for i in range(0, 100 + 1, 3):
        handle_events()
        t = i / 100
        char_x = (1 - t) * x1 + t * x2
        char_y = (1 - t) * y1 + t * y2
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        hand.draw(x, y)
        if 0 > x2 - x1:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, char_x, char_y)
        elif 0 <= x2 - x1:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, char_x, char_y)
        frame = (frame+1) % 8
        for j in range(0, len(point_list), 2):
            hand.draw(point_list[j], point_list[j + 1])
        update_canvas()
        delay(0.05)
    del point_list[1], point_list[0]
    if len(point_list) == 0 :
        pass

close_canvas()
