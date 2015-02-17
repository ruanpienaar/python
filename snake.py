#!/usr/bin/env python

# 0,0

# 0,0 0,1

# 0,0 0,1 0,2

# 0,0 0,1 0,2 0,3

# 0,0 0,1 0,2 0,3 0,4

# 0,0 0,1 0,2 0,3 0,4 0,5

# 0,1 0,2 0,3 0,4 0,5 0,6

# 0,2 0,3 0,4 0,5 0,6 0,7

# 0,3 0,4 0,5 0,6 0,7 1,7

# 0,4 0,5 0,6 0,7 1,7 1,6

# 0,5 0,6 0,7 1,7 1,6 1,5

# 0,6 0,7 1,7 1,6 1,5 1,4


position = (0, 0)
full_size = False
going_forward = True
left_to_right = True

while True:

    rgb_on  = colorsys.hsv_to_rgb(0.5, 0.5, 0.5)
    rgb_off = colorsys.hsv_to_rgb(0.5, 0.5, 0.1)

    r_on  = int(rgb_on[0]*255.0)
    g_on  = int(rgb_on[1]*255.0)
    b_on  = int(rgb_on[2]*255.0)

    r_off = int(rgb_off[0]*255.0)
    g_off = int(rgb_off[1]*255.0)
    b_off = int(rgb_off[2]*255.0)

    # Switch off previous light
    unicorn.set_pixel(position[0], position[1], r_off, g_off, b_off)

    if position[1] > 8:
        left_to_right = False
    elif position[1] == 0
        left_to_right = True

    if left_to_right:
        position = (position[0], position[1]+1)
    else:
        position = (position[0], position[1]-1)


        # if going_forward:
        #     position = (position[0]+1, position[1])
        # else:
        #     position = (position[0]-1, position[1])

        # # Turn around
        # if left_to_right:
        #     left_to_right = False
        # else:
        #     left_to_right = True

    unicorn.set_pixel(position[0], position[1], r_on, g_on, b_on)
    unicorn.show()
    time.sleep(0.001)

    # if full_size:
    #     foreach positions , enable light.
    # else
    #     if len( positions ) < 5
    #         if going_left:
    #             pos_col += 1
    #         elif going_right:
    #             pos_col -= 1
    #         positions = positions + ((pos_row, pos_col))
    #         if len( positions ) == 5
    #             full_size = True
    #         unicorn.set_pixel(0, 0, r_on, g_on, b_on)