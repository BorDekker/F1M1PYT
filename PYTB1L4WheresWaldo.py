import random
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)
print(people)

count = 0
while count < len(people):
    if people[count] == "Waldo":
        print("gevonden op positie "+ str(count+1))
    count += 1