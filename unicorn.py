#!/usr/bin/env python

import unicornhat as unicorn
import time, colorsys
import numpy as np

unicorn.brightness(0.45)
#bright = 0.01

h = 0.05
s = 0.05
v = 0.2

row=0
col=-1

while True:

#    bright += 0.01
#    if abs(bright) > 1.0:
#	bright = 0.01
#    unicorn.brightness(bright)  

    #h += 0.01
    #s += 0.01
    #v += 0.01

    col += 1
    if abs(col) > 7:
	h += 0.01
	s += 0.01
	row += 1
	if abs(row) > 7:
	  v += 0.01
	  row = 0
	col = 0

    if abs(h) > 1:
        h = 0.1
    elif abs(s) > 1:
        s = 0.1
    elif abs(v) > 1:
	v = 0.2

    print row, col

    rgb = colorsys.hsv_to_rgb(h, s, v)
    r = int(rgb[0]*255.0)
    g = int(rgb[1]*255.0)
    b = int(rgb[2]*255.0)

    unicorn.set_pixel(row, col, r, g, b)
    unicorn.show()
    time.sleep(0.0001)
