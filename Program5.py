""" Write a program to receive 5 command line arguments and print each argument separately.
Example: >> python test.py arg1 arg2 arg3 arg4 arg5
a) From the above statement your program should receive arguments and print them each of them.
b) Find the biggest of three numbers, where three numbers are passed as command line arguments."""

# !/usr/bin/python
import sys
m = 0
for c in range(1,len(sys.argv)):
    print sys.argv[c]

print max(sys.argv)
for a in range(1,len(sys.argv)):
    if int(a) > m:
        m = int(a)

print "Max:" , m

