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

x = long(28)
y = float(29)

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

# 3. booleans

# Only two values: True, False

type(True) # type(False)
# <type 'bool'>

a = True + 100
# 101
b = False * 100
# 0

# 4. datetime

import datetime

gvr = datetime.date(1986, 7, 11)

print gvr.year  # 1986
print gvr.month # 7
print gvr.day   # 11
print gvr.ctime()   # Fri Jul 11 00:00:00 1986

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)

print launch_date   # 2017-03-30
print launch_time   # 22:27:00
print launch_datetime   # 2017-03-30 22:27:00

print datetime.datetime.today() 
# datetime.datetime(2018, 1, 4, 21, 54, 10, 808000)

# 4.1 convert string to datetime:

# - Module: datetime
# - Class: datetime
# - Method: strptime()

moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
# 1969-07-20 00:00:00