# v = 4(pi * r^3)/3

import math

def volume(r):
    """returns the volume of a sphere with radius r."""
    return (4.0/3.0) * math.pi * math.pow(r, 3)

print volume(2)

# default parameter values
def cm(feet = 0, inches = 0):
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54

    return inches_to_cm + feet_to_cm

# follow method callee are all write
print cm(2)
print cm(2, 3)
print cm(inches = 2)
print cm(feet = 3)
print cm(feet = 2, inches = 3)
print cm(inches = 2, feet = 3)

# SyntaxError: non-default argument follows default argument
def g(x = 2, y):
    pass

# argument x is a required argument
def g(x, y = 2):
    pass

print g(2)
print g(2, y = 3)