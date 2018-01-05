# collect string / test length

input = raw_input("Please enter a test string: ")

if len(input) < 6:
    print("Your string is too short.")
    print("Please enter a string with at lease 6 characters.")
else:
    print "input is:" + input

number = raw_input("Please enter an integer: ")

if int(number) % 2 == 0:
    print ("Your number is even.")
else:
    print ("Your number is odd.")

# Scalen Triangle: All sides have different lengths.
# Isosceles Triangle: Two sides have the same length.
# Equilateral Triangle: All sides are equal.

a = int(raw_input("The length of side a = "))
b = int(raw_input("The length of side b = "))
c = int(raw_input("The length of side c = "))

if a != b and b != c and c != a:
    print "This is a saclene triangle."
elif a == b and b == c:
    print "this is a equilateral triangle."
else:
    print "this is isosceles triangle."