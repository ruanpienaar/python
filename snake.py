#!/usr/bin/env python

import unicornhat as unicorn
import time, colorsys

position = (0, 0)
prev_position = (0, 0)
full_size = False
going_forward = True
right_to_left = True

unicorn.brightness(0.75)

while True:

    rgb_on  = colorsys.hsv_to_rgb(0.5, 0.5, 0.5)
    rgb_off = colorsys.hsv_to_rgb(0.5, 0.5, 0.1)

    r_on  = int(rgb_on[0]*255.0)
    g_on  = int(rgb_on[1]*255.0)
    b_on  = int(rgb_on[2]*255.0)

    r_off = int(rgb_off[0]*255.0)
    g_off = int(rgb_off[1]*255.0)
    b_off = int(rgb_off[2]*255.0)

    unicorn.set_pixel(prev_position[0], prev_position[1], r_off, g_off, b_off)

    if position[0] >= 7:
        going_forward = False
    elif position[0] == 0:
        going_forward = True

    if position[1] >= 7:
        if going_forward:
            position = (position[0]+1, position[1])
        else:
            position = (position[0]-1, position[1])
        right_to_left = False
    elif position[1] == 0:
        if going_forward:
            position = (position[0]+1, position[1])
        else:
            position = (position[0]-1, position[1])
        right_to_left = True

    if right_to_left:
        position = (position[0], position[1]+1)
    else:
        position = (position[0], position[1]-1)

    prev_position = position
    unicorn.set_pixel(position[0], position[1], r_on, g_on, b_on)
    unicorn.show()
    time.sleep(0.5)
