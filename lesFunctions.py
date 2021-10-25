def add(getal1, getal2):
    print(getal1)
    print("+")
    print(getal2)
    print("=")
    print(getal1+getal2)
    print("")
    
add(4, 8)
add(9, 2)
add(52, 48)

def how_long_is_string(str, length):
    if len(str) > length:
        print("Yes, this string is long")
    else:
        print("No, this string isn't very long")

how_long_is_string("Hello", 8)
how_long_is_string("Hello World", 8)

print("")

import random
def roll_dice():
    rand_getal = random.randrange(1,6)
    print("text")
    return rand_getal

d1 = roll_dice()
print(d1)
d2 = roll_dice()
print(d2)

print("")

def larger_number(getal1, getal2):
    if getal1 > getal2:
        return getal1
    elif getal1 < getal2:
        return getal2
    else:
        return 0

q1 = larger_number(8, 9)
print(q1)
q2 = larger_number(10, 2)
print(q2)
q3 = larger_number(5, 5)
print(q3)
