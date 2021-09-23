import datetime

script = True
while True:
    print("Hello you, ik ben Bor Dekker.")
    print("Wie ben jij?")
    username = input("Enter username")
    print("")
    print("Hello" + username)
    print("Do you want to repeat?")
    inputText = input()
    print("input:", inputText)
    if inputText == "no":
        break