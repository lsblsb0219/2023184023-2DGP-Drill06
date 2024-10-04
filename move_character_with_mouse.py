#2023184023 이수빈

import random
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

onoff = False
hand_x, hand_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
character_x, character_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

new_character_x, new_character_y = character_x, character_y

onoff = True

while onoff:
    while not character_x == hand_x and not character_y == hand_y:
        for i in range(0, 100 + 1, 4):
            clear_canvas()
            TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
            if hand_x > new_character_x:
                character.clip_draw(frame * 100, 100 * 1, 100, 100, new_character_x, new_character_y)
            elif hand_x < new_character_x:
                character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', new_character_x, new_character_y,
                                              100, 100)
            hand.draw(hand_x, hand_y, 50, 52)

            t = i / 100
            new_character_x = (1 - t) * character_x + t * hand_x
            new_character_y = (1 - t) * character_y + t * hand_y
            frame = (frame + 1) % 8
            update_canvas()
            delay(0.05)
        character_x, character_y = new_character_x, new_character_y
    hand_x, hand_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)

close_canvas()




