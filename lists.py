my_list = [4.4, 6.7, 3.9, 9.4, 7.3, 2.8, 1.2, 5.6]
print (my_list)
def add(getal1, getal2, getal3):
    print(getal1)
    print("+")
    print(getal2)
    print("+")
    print(getal3)
    print("=")
    print(getal1+getal2+getal3)
    print("")

add(4.4, 6.7, 3.9)
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])
print(my_list[5])
print(my_list[6])
print(my_list[7])
print("")

my_list.append(93.1)
for element in my_list:
    print(element)
    print("")

var1 = my_list.pop(0) + my_list.pop(0)

print(var1)