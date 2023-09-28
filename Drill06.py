from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1240, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')


def handle_events():
    global running
    global x, y
    global point_list
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
            point_list.append(x)
            point_list.append(y)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


point_list = []

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(x, y)
    for i in range (0,len(point_list),2):
        hand.draw(point_list[i],point_list[i+1])
    update_canvas()

    handle_events()

close_canvas()
