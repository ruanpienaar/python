#!/usr/bin/env python

import unicornhat as unicorn
import time, colorsys
import numpy as np

x = 0
y = 0
prev_x = 0
prev_y = 0
sleep = 0.5
faster = True
amount = 1
count = 99
#stack

unicorn.brightness(0.25)

def uni_show(prev_x, prev_y):
    a = np.random.rand(1)
    b = np.random.rand(1)
    c = np.random.rand(1)
    rgb_on  = colorsys.hsv_to_rgb(a, b, c)
    rgb_off = colorsys.hsv_to_rgb(0.5, 0.5, 0.1)

    r_on  = int(rgb_on[0]*255.0)
    g_on  = int(rgb_on[1]*255.0)
    b_on  = int(rgb_on[2]*255.0)

    r_off = int(rgb_off[0]*255.0)
    g_off = int(rgb_off[1]*255.0)
    b_off = int(rgb_off[2]*255.0)	

    a = np.random.rand(1)
    x = int(a[0] * 7)
    b = np.random.rand(1)
    y = int(b[0] * 7)

    unicorn.set_pixel(x, y, r_on, g_on, b_on)
    unicorn.set_pixel(prev_x, prev_y, r_off, g_off, b_off)

    unicorn.show()
    return x, y

while True:

   count += 1
   if count % 10 == 0:
	amount += 1
	print amount

   for a in range(amount):
      x, y = uni_show(prev_x, prev_y)
      prev_x = x
      prev_y = y

#   if faster:
#     if sleep > 0.1:
#       sleep -= 0.1
#     else:
#       sleep += 0.1
#       faster = False
#   else:
#     if sleep < 0.5:
#       sleep += 0.1
#     else:
#       sleep -= 0.1
#       faster = True

   #print sleep
		  
   time.sleep(0.1)
