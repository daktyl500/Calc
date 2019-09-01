print("Witaj w prostym kalkulatorze")
op = 0
while op == 0:
    print("1: Dodawanie dwóch liczb")
    print("2: Odejmowanie dwóch liczb")
    print("3: Mnozenie dwóch liczb")
    print("4: Dzielenie dwóch liczb")
    print("5: Wyjœcie z programu")
    print("Wpisyj¹c od 1 do 5 i zatwierdzaj¹c klawiszem enter wybierasz opcje")
    opcja = str(raw_input("Któr¹ opcje wybierasz:"))
    if opcja == "1":
        x = input("Podaj pierwsz¹ liczbê:")
        y = input("Podaj druga liczbê:")
        print("Wynik dodawania to: " + str(x+y))
        print
    elif opcja == "2":
        x = input("Podaj pierwsz¹ liczbê:")
        y = input("Podaj druga liczbê:")
        print("Wynik odejmowania to: " + str(x-y))
        print
    elif opcja == "3":
        x = input("Podaj pierwsz¹ liczbê:")
        y = input("Podaj druga liczbê:")
        print("Wynik mno¿enia to: " + str(x*y))
        print
    elif opcja == "4":
        x = input("Podaj pierwsz¹ liczbê:")
        y = input("Podaj druga liczbê:")
        z = float(x) / float(y)
        print("Wynik dzielenia to: " + str(z))
        print
    elif opcja == "5":
        print("Dziêkuje za skorzystanie z prostego kalkulatora")
        break
    else:
        print("Niepoprawny wybór")
        print
    
    
    
