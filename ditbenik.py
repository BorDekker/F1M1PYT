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
    elif inputText == "B":
        print("Nee, schattige dieren. Ik heb een lieve hond genaamd Rover. Het juiste andwoord was C")
    if inputText == "C":
        print("JAAAAA, ik heb een lieve en schattige hond genaamd Rover. Hij is 2 jaar oud en het is een golden retriever")
    print("De dag is voorbij en je gaat naar huis, ga je lopen naar het station of via de tram?")
    print("A. Je gaat lopen")
    print("B. Je gaat met de tram")
    inputText = input()
    if inputText == "A":
        print("Je gaat lopen naar het station, en je weet de route ernaar toe")
        print("Na 20 minuten lopen kom je bij het station. Je gaat naar spoor 7, neem je een Intercity of een Sprinter?")
        print("A. Intercity")
        print("B. Sprinter")
        inputText = input()
        if inputText == "A":
            print("Je wacht 10 minuten en neemt de Intercity die je naar Haarlem gaat brengen")
            print("Na 9 minuten ben je op het station Haarlem en ga je naar je fiets")
            print("Je pakt je fiets en fietst naar huis. Onderweg kom je een vriend tegen, hij vraagt jouw wat")
            print("Wil je afspreken")
            print("A. Ja is goed, ik vraag eerst aan mijn ouders of het kan")
            print("B. Sorry, maar ik heb veel huiswerk. We gaan morgen afspreken oké?")
            inputText = input()
            if inputText == "A":
                print("Je belt je moeder en vraagt of je kan afspreken. Nadat je klaar was met bellen zei je dat je t/m 22:30 kan blijven")
                print("Een paar uur later neem je afscheid en bedank je je vriend voor het avond eten en ga je naar huis")
                print("Eenmaal thuis ga je film kijken met je familie en daarna tanden poetsen en naar bed")
            elif inputText == "B":
                print("Je neemt afscheid en gaat opweg naar huis")
                print("Eenmaal thuis ga je je huiswerk maken en daarna avond eten.")
                print("Later ben je op de PlayStation gegaan en nog film gekeken met je familie")
                print("Daarna heb je je hond uitgelaten en tanden gepoetst en naar bed gegaan")

        elif inputText == "B":
            print("Je wacht 5 minuten en neemt de Sprinter naar Haarlem")
            print("Onderweg crashte de Sprinter en ben je overleden")
            print("YOU DIED")
    elif inputText == "B":
        print("Je gaat met de tram, maar je weet de weg niet.")
        print("Je probeert de weg naar de tram te vinden en kijkt op je telefoon")
        print("Je steekt over en word aangereden door een vrachtwagen")
        print("YOU DIED")



    print("Do you want to repeat?")
    inputText = input()
    print("input:", inputText)
    if inputText == "no":
        break