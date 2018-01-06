# List example
prime_numbers = [2, 3, 5, 7, 11, 13, 17]

# Tuple example
perfect_squares = (1, 4, 9, 16, 25, 36)

# Display length
print("# Primes = ", len(prime_numbers))
print("# Squares = ", len(perfect_squares))

# ('# Primes = ', 7)
# ('# Squares = ', 6)

# Iterate over both sequences
for p in prime_numbers:
    print("Prime: ", p)

for n in perfect_squares:
    print("Squares: ", n)

# ('Prime: ', 2)
# ('Prime: ', 3)
# ('Prime: ', 5)
# ('Prime: ', 7)
# ('Prime: ', 11)
# ('Prime: ', 13)
# ('Prime: ', 17)
# ('Squares: ', 1)
# ('Squares: ', 4)
# ('Squares: ', 9)
# ('Squares: ', 16)
# ('Squares: ', 25)
# ('Squares: ', 36)

dir(tuple)
# ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getite
# m__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '_
# _ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook_
# _', 'count', 'index']

import sys

t = (1,2,3,4)
l = [1,2,3,4]

sys.getsizeof(t)    # 80
sys.getsizeof(l)    # 120

# Tuples
# 1. Can not be changed
# 2. Immutable
# 3. Made quickly

import timeit

list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
tuple_test = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)

print("t: ",tuple_test, " l: ", list_test)
# ('t: ', 3.4194751700595085, ' l: ', 3.855936487819027)

empty_tuple = ()
t1 = ("a") # "a", str
t2 = ("a",) # ("a"), tuple

t1 == "a"
# True

t2 == "a"
# False