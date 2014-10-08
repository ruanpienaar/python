#!/usr/bin/env python
int = int(raw_input("Please enter a number : "))
if int == 0:
    print "bigger than 0 please"
elif int > 0 and int < 10:
    print "little bigger please"
else:
    print "something bigger than 10, yay!"

