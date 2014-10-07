#!/usr/bin/python
answer = raw_input("Yes or No ? [y/n]")
print "Your answer was %s" % answer

answer2 = raw_input("Type Something:")
print "character 1 was %s" % answer2[1]
print "last character was %s" % answer2[-1]
print "characters from 1 - 3 was %s" % answer2[1:3]

answer3 = raw_input("Enter a number:")
print "number was %d" % answer3