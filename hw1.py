# Name: Josh Hedger
# Evergreen Login: HedJos24
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

# Comments: The questions were phrased a bit odd, I have previous programming knowledge but do not understand what was being asked exactly.

print "Problem 1 solution follows:"
# Compute and print both roots of the quadratic equation x2-5.86 x+ 8.5408. 
AVal = 1
BVal = -5.86
CVal = 8.5408
OddVal = math.sqrt((BVal ** 2) - ((AVal * CVal) * 4))

#Not quite sure what the question is asking, hopefully you mean something like this.
print((-BVal + OddVal) / (AVal * 2))

###
### Problem 2
###

print "Problem 2 solution follows:"
from hw1_test import a,b,c,d,e,f

print(a,b,c,d,e,f)
#print(b)
#print(c)
#print(d)
#print(e)
#print(f)

###
### Problem 3
###

print "Problem 3 solution follows:"

print(str(a and b) or (not c) and not (d or e or f))



###
### Collaboration
###

# ... List your collaborators here, as a comment (on a line starting with "#").
