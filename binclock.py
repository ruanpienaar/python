#!/usr/bin/env python

from datetime import datetime
import time
import unicornhat as unicorn
import time, colorsys

def decimal_to_binary(decimal):
    """Convert a decimal (base 10) to a binary (base 2) number."""
    def tmp():
        n = decimal
        if n == 0:
            yield 0
        while n > 0:
            yield n % 2
            n >>= 1
    return ''.join(reversed(map(str, tmp())))

def time_as_matrix():
    """Return current time represented as binary matrix."""
    decimal = map(int, datetime.now().strftime('%H%M%S'))
    binary = [decimal_to_binary(n).rjust(4, '0') for n in decimal]
    return tuple(tuple(map(int, ns)) for ns in zip(*binary))

#"""
#matrix = (
#            (0, 1, 0, 1, 0, 1),
#            (0, 1, 1, 1, 1, 1),
#            (1, 1, 1, 1, 1, 1),
#            (1, 1, 1, 1, 1, 1),
#            )
#"""
def matrix_to_hat(matrix):
    rgb_on  = colorsys.hsv_to_rgb(0.5, 0.5, 0.5)
    rgb_off = colorsys.hsv_to_rgb(0.5, 0.5, 0.1)

    r_on  = int(rgb_on[0]*255.0)
    g_on  = int(rgb_on[1]*255.0)
    b_on  = int(rgb_on[2]*255.0)

    r_off = int(rgb_off[0]*255.0)
    g_off = int(rgb_off[1]*255.0)
    b_off = int(rgb_off[2]*255.0)

    # _,_ 0,6 _,_ 0,4 _,_ 0,2 _,_ _,_
    # _,_ 1,6 1,5 1,4 1,3 1,2 _,_ _,_
    # 2,7 2,6 2,5 2,4 2,3 2,2 _,_ _,_
    # 3,7 3,6 3,5 3,4 3,3 3,2 _,_ _,_
    # _,_ _,_ _,_ _,_ _,_ _,_ _,_ _,_
    # _,_ _,_ _,_ _,_ _,_ _,_ _,_ _,_
    # _,_ _,_ _,_ _,_ _,_ _,_ _,_ _,_
    # _,_ _,_ _,_ _,_ _,_ _,_ _,_ _,_

    if matrix[0][1] == 0:
        unicorn.set_pixel(0, 6, r_off, g_off, b_off)
    elif matrix[0][1] == 1:
        unicorn.set_pixel(0, 6, r_on, g_on, b_on)

    if matrix[0][3] == 0:
        unicorn.set_pixel(0, 4, r_off, g_off, b_off)
    elif matrix[0][3] == 1:
        unicorn.set_pixel(0, 4, r_on, g_on, b_on)

    if matrix[0][5] == 0:
        unicorn.set_pixel(0, 2, r_off, g_off, b_off)
    elif matrix[0][5] == 1:
        unicorn.set_pixel(0, 2, r_on, g_on, b_on)

    # #   unicorn.set_pixel(0, 7, r, g, b)
    # unicorn.set_pixel(0, 6, r, g, b)
    # #   unicorn.set_pixel(0, 5, r, g, b)
    # unicorn.set_pixel(0, 4, r, g, b)
    # #   unicorn.set_pixel(0, 3, r, g, b)
    # unicorn.set_pixel(0, 2, r, g, b)
    # #   unicorn.set_pixel(0, 1, r, g, b)
    # #   unicorn.set_pixel(0, 0, r, g, b)

    if matrix[1][1] == 0:
        unicorn.set_pixel(1, 6, r_off, g_off, b_off)
    elif matrix[1][1] == 1:
        unicorn.set_pixel(1, 6, r_on, g_on, b_on)

    if matrix[1][2] == 0:
        unicorn.set_pixel(1, 5, r_off, g_off, b_off)
    elif matrix[1][2] == 1:
        unicorn.set_pixel(1, 5, r_on, g_on, b_on)

    if matrix[1][3] == 0:
        unicorn.set_pixel(1, 4, r_off, g_off, b_off)
    elif matrix[1][3] == 1:
        unicorn.set_pixel(1, 4, r_on, g_on, b_on)

    if matrix[1][4] == 0:
        unicorn.set_pixel(1, 3, r_off, g_off, b_off)
    elif matrix[1][4] == 1:
        unicorn.set_pixel(1, 3, r_on, g_on, b_on)

    if matrix[1][5] == 0:
        unicorn.set_pixel(1, 2, r_off, g_off, b_off)
    elif matrix[1][5] == 1:
        unicorn.set_pixel(1, 2, r_on, g_on, b_on)

    # #   unicorn.set_pixel(1, 7, r, g, b)
    # unicorn.set_pixel(1, 6, r, g, b)
    # unicorn.set_pixel(1, 5, r, g, b)
    # unicorn.set_pixel(1, 4, r, g, b)
    # unicorn.set_pixel(1, 3, r, g, b)
    # unicorn.set_pixel(1, 2, r, g, b)
    # #   unicorn.set_pixel(1, 1, r, g, b)
    # #   unicorn.set_pixel(1, 0, r, g, b)

    if matrix[2][0] == 0:
        unicorn.set_pixel(1, 7, r_off, g_off, b_off)
    elif matrix[2][0] == 1:
        unicorn.set_pixel(1, 7, r_on, g_on, b_on)

    if matrix[2][1] == 0:
        unicorn.set_pixel(1, 6, r_off, g_off, b_off)
    elif matrix[2][1] == 1:
        unicorn.set_pixel(1, 6, r_on, g_on, b_on)

    if matrix[2][2] == 0:
        unicorn.set_pixel(1, 5, r_off, g_off, b_off)
    elif matrix[2][2] == 1:
        unicorn.set_pixel(1, 5, r_on, g_on, b_on)

    if matrix[2][3] == 0:
        unicorn.set_pixel(1, 4, r_off, g_off, b_off)
    elif matrix[2][3] == 1:
        unicorn.set_pixel(1, 4, r_on, g_on, b_on)

    if matrix[2][4] == 0:
        unicorn.set_pixel(1, 3, r_off, g_off, b_off)
    elif matrix[2][4] == 1:
        unicorn.set_pixel(1, 3, r_on, g_on, b_on)

    if matrix[2][5] == 0:
        unicorn.set_pixel(1, 2, r_off, g_off, b_off)
    elif matrix[2][5] == 1:
        unicorn.set_pixel(1, 2, r_on, g_on, b_on)

    # unicorn.set_pixel(2, 7, r, g, b)
    # unicorn.set_pixel(2, 6, r, g, b)
    # unicorn.set_pixel(2, 5, r, g, b)
    # unicorn.set_pixel(2, 4, r, g, b)
    # unicorn.set_pixel(2, 3, r, g, b)
    # unicorn.set_pixel(2, 2, r, g, b)
    # unicorn.set_pixel(2, 1, r, g, b)
    # unicorn.set_pixel(2, 0, r, g, b)

    if matrix[3][0] == 0:
        unicorn.set_pixel(1, 7, r_off, g_off, b_off)
    elif matrix[3][0] == 1:
        unicorn.set_pixel(1, 7, r_on, g_on, b_on)

    if matrix[3][1] == 0:
        unicorn.set_pixel(1, 6, r_off, g_off, b_off)
    elif matrix[3][1] == 1:
        unicorn.set_pixel(1, 6, r_on, g_on, b_on)

    if matrix[3][2] == 0:
        unicorn.set_pixel(1, 5, r_off, g_off, b_off)
    elif matrix[3][2] == 1:
        unicorn.set_pixel(1, 5, r_on, g_on, b_on)

    if matrix[3][3] == 0:
        unicorn.set_pixel(1, 4, r_off, g_off, b_off)
    elif matrix[3][3] == 1:
        unicorn.set_pixel(1, 4, r_on, g_on, b_on)

    if matrix[3][4] == 0:
        unicorn.set_pixel(1, 3, r_off, g_off, b_off)
    elif matrix[3][4] == 1:
        unicorn.set_pixel(1, 3, r_on, g_on, b_on)

    if matrix[3][5] == 0:
        unicorn.set_pixel(1, 2, r_off, g_off, b_off)
    elif matrix[3][5] == 1:
        unicorn.set_pixel(1, 2, r_on, g_on, b_on)

    # unicorn.set_pixel(3, 7, r, g, b)
    # unicorn.set_pixel(3, 6, r, g, b)
    # unicorn.set_pixel(3, 5, r, g, b)
    # unicorn.set_pixel(3, 4, r, g, b)
    # unicorn.set_pixel(3, 3, r, g, b)
    # unicorn.set_pixel(3, 2, r, g, b)
    # unicorn.set_pixel(3, 1, r, g, b)
    # unicorn.set_pixel(3, 0, r, g, b)


unicorn.brightness(0.45)
while True:
    matrix = time_as_matrix()
    matrix_to_hat(matrix)
    unicorn.show()
    time.sleep(1.0)
