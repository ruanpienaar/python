#!/usr/bin/env python
def three(v):
    return v % 3 == 0

def five(v):
    return v % 5 == 0

def fizzb(v):
    return three(v) and five(v)

for x in xrange(1,100):
    if fizzb(x):
        print "FizzBuzz"
    elif five(x):
        print "Buzz"
    elif three(x):
        print "Fizz"
    else:
        print "%d" % x

