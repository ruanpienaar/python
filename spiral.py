#!/usr/bin/env python
# 0,0 is the corner of the Unicorn HAT furthest away from the the ethernet port.
import unicornhat as UH
import numpy as np
import time

UH.brightness(0.25)

# x = y = xlo = ylo = 0
# xhi = yhi = 7
r = 255
g = 64
b = 255

def random_rgb():
  r = int( np.random.rand() * 255 )
  # time.sleep(0.01)
  g = int( np.random.rand() * 255 )
  # time.sleep(0.01)
  b = int( np.random.rand() * 255 )
  return (r,g,b)

def draw_dot( x1, y1, r1, g1, b1, str1):
  "This draws the dot and outputs some text"
  UH.set_pixel(x1,y1,r1,g1,b1)
  UH.show()
  # print (str1 + str(x1) + ' ' + str(y1))
  time.sleep(0.1)
  return

while True:
  x = y = xlo = ylo = 0
  xhi = yhi = 7
  for ring in range(4):
    y = ylo
    rgb=random_rgb()
    for x in range(xlo, xhi +1):
      draw_dot(x,y,rgb[0],rgb[1],rgb[2],'W ');
    x = xhi
    rgb=random_rgb()
    for y in range(ylo+1, yhi +1):
      draw_dot(x,y,rgb[0],rgb[1],rgb[2],'N ');
    y = yhi
    rgb=random_rgb()
    for x in range(xhi-1, xlo, -1):
      draw_dot(x,y,rgb[0],rgb[1],rgb[2],'E ');
    x = xlo
    rgb=random_rgb()
    for y in range(yhi, ylo, -1):
      draw_dot(x,y,rgb[0],rgb[1],rgb[2],'S ');
    xlo += 1
    xhi -= 1
    ylo += 1
    yhi -= 1
  time.sleep(0.1)