my_list = [6.7, 7.6, 8.3, 5.2, 9.1]
print(my_list)
print("")

my_list.append(92.5)
for element in my_list:
    print(element)
    print("")

var1 = my_list.pop(0) + my_list.pop(0)
print(var1)
print("")

my_list.reverse()
print(my_list)