import random
def my_function(original):
    randomised = ''.join(random.sample(original, len(original)))
    return randomised

my_function("beer")
my_function("godofwar")
my_function("school")
print(my_function("beer"))
print(my_function("godofwar"))
print(my_function("school"))