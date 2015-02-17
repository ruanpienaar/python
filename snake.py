#!/usr/bin/env python

import unicornhat as unicorn
import time, colorsys

position = (0, 0)
prev_position = (0, 0)
full_size = False
go_down = True
go_left = True

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

    hor_pos = position[0]
    ver_pos = position[1]

    if ver_pos == 7:
        go_left = False
    elif ver_pos == 0:
        go_left = True

    if hor_pos == 7:
        go_down = False
        position = (position[0]+1, position[1])
    elif hor_pos == 0:
        go_down = True
        position = (position[0]-1, position[1])
    else:
        if go_left:
            position = (position[0], position[1]+1)
        else:
            position = (position[0], position[1]-1)

    # if ver_pos == 7:
    #     go_left = False
    #     if go_down:
    #         position = (position[0]+1, position[1]-1)
    #     else:
    #         position = (position[0]-1, position[1]-1)
    # elif ver_pos == 0:
    #     go_left = True
    #     if go_down:
    #         position = (position[0]+1, position[1]+1)
    #     else:
    #         position = (position[0]-1, position[1]+1)
    #     position = (position[0], position[1]+1)
    # else:
    #     if go_left:
    #         position = (position[0], position[1]+1)
    #     else:
    #         position = (position[0], position[1]-1)




    prev_position = position

    print position[0], position[1]
    unicorn.set_pixel(position[0], position[1], r_on, g_on, b_on)
    unicorn.show()
    time.sleep(0.5)
