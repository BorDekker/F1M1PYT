import datetime

script = True
while True:
    print("Hello you, ik ben Bor Dekker.")
    print("Wie ben jij?")
    username = input("Enter username")
    print("")
    print("Hello" + username)
    print("Ik ben (g)een nieuwkomer op het Mediacollege Amsterdam")
    print("Door een aantal vragen over mij te beantwoorden leer je mij beter kennen")
    print("")
    print("Voor ik naar het MBO op het Mediacollege Amsterdam kwam, werkte ik op...")
    print("A. Het Kennemer College in Overveen, Haarlem.")
    print("B. Het Spaarne College in Overveen, Haarlem")
    print("C. Het Clusius College in Alkmaar")
    inputText = input()
    if inputText == "A":
        print("Dit is het verkeerde antwoord")
        print("Het juiste antwoord was B")
    if inputText == "B":
        print("Dit is het juiste andwoord")
        print("Mijn vorige school was het Spaarne College, 3 jaar op de Paulus Mavo en mijn laaste jaar op het Spaarne College")
        print("In mijn laaste jaar gingen 3 scholen combineren, waardoor ik mijn laatste jaar op een andere school deed")
    if inputText == "C":
        print("Dit is het verkeerde andwoord")
        print("Het juiste andwoord was B")
    print("Ik ben hoe oud...")
    print("A. 17")
    print("B. 21")
    print("C. 15")
    inputText = input()
    if inputText == "A":
        print("Dat is goed, ik ben geboren op 28 Mei 2004")
    if inputText == "B":
        print("Dat is fout, ik ben 17 jaar oud. Het goede andwoord was A")
    if inputText == "C":
        print("Dat is fout, ik ben 17 jaar oud. Het goede andwoord was A")
    print("Mijn huisdier is...")
    print("A. Een alligator")
    print("B. Een konijn")
    print("C. Een hond")
    inputText = input()
    if inputText == "A":
        print("Nee, helaas niet. Ik heb een schattige hond genaamd Rover. Dus het juiste andwoord was C")
    if inputText == "B":
        print("Nee, schattige dieren. Ik heb een lieve hond genaamd Rover. Het juiste andwoord was C")
    if inputText == "C":
        print("JAAAAA, ik heb een lieve en schattige hond genaamd Rover. Hij is 2 jaar oud en het is een golden retriever")
    print("De dag is voorbij en je gaat naar huis, ga je lopen naar het station of via de tram?")
    print("A. Je gaat lopen")




    print("Do you want to repeat?")
    inputText = input()
    print("input:", inputText)
    if inputText == "no":
        break