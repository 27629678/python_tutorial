print "hello, world."

# 01. strings

# single quote
message = 'hello, world'

# double quote
message = "hello, world"

# triple quote
message = '''the following option:
1. option a;
2. option b;
'''

print message

# 02. numbers

# types of numbers: int, long, float, complex
# whole numbers: int, long

a = 28 # this is a perfect number
print type(a)
# <type 'int'>

import sys

b = sys.maxint + 1

print type(b)
# <type 'long'>

# 2.1 floats

e = 3.1415926
print type(e)
# <type 'float'>

# 2.2 complex(复数)

c = complex(1, 2)
c1 = 1+2j
print type(c)
# <type 'complex'>

print c.real, c.imag