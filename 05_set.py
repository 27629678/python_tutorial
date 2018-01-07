# unordered list

s = set()

dir(set)

# ['__and__', '__class__', '__cmp__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getat
# tribute__', '__gt__', '__hash__', '__iand__', '__init__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__le
# n__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub
# __', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy
# ', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issup
# erset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

help(set.add)

# Help on method_descriptor:

# add(...)
#     Add an element to a set.

#     This has no effect if the element is already present.

s.add(10)
s.add(False)
s.add("hello")
s.add(3.14)

len(s)
# 4

help(s.remove)

Help on method_descriptor:

# remove(...)
#     Remove an element from a set; it must be a member.

#     If the element is not a member, raise a KeyError.

s.remove(True)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   KeyError: True

help(s.discard)

# Help on method_descriptor:

# discard(...)
#     Remove an element from a set if it is a member.

#     If the element is not a member, do nothing.

s.discard(True)

len(s)
# 4

s.remove(False)

len(s)
# 3

s.discard("hello")
# 2

s.discard("world")
# no out-put

print s

# set([10, 3.14])

# literal set initializer
s1 = set([28, True, 3.1415926, False, "hello, world."])
len(s1)

# 5

# clear all elements
s1.clear()

len(s1)

# 0

# Integers 1 - 10

odds = set([1,3,5,7,9])
evens= set([2,4,6,8,10])
primes = set([2,3,5,7])
composites = set([4,6,8,9,10])

odds.union(evens)

# set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

odds.intersection(evens)

# set()

if 1 in odds :
    print True

# True

# List Comprehensions(列表推导)

# [expr for val in collection]

# [expr for val in collection if <test>]

# [expr for val in collection if <test1> and <test2>]

# [expr for val1 in collection1 and val2 in collection2]

squires = [i**2 for i in range(1, 100)]