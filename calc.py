print("Witaj w prostym kalkulatorze")
op = 0
while op == 0:
    print("1: Dodawanie dw�ch liczb")
    print("2: Odejmowanie dw�ch liczb")
    print("3: Mnozenie dw�ch liczb")
    print("4: Dzielenie dw�ch liczb")
    print("5: Wyj�cie z programu")
    print("Wpisyj�c od 1 do 5 i zatwierdzaj�c klawiszem enter wybierasz opcje")
    opcja = str(raw_input("Kt�r� opcje wybierasz:"))
    if opcja == "1":
        x = input("Podaj pierwsz� liczb�:")
        y = input("Podaj druga liczb�:")
        print("Wynik dodawania to: " + str(x+y))
        print
    elif opcja == "2":
        x = input("Podaj pierwsz� liczb�:")
        y = input("Podaj druga liczb�:")
        print("Wynik odejmowania to: " + str(x-y))
        print
    elif opcja == "3":
        x = input("Podaj pierwsz� liczb�:")
        y = input("Podaj druga liczb�:")
        print("Wynik mno�enia to: " + str(x*y))
        print
    elif opcja == "4":
        x = input("Podaj pierwsz� liczb�:")
        y = input("Podaj druga liczb�:")
        z = float(x) / float(y)
        print("Wynik dzielenia to: " + str(z))
        print
    elif opcja == "5":
        print("Dzi�kuje za skorzystanie z prostego kalkulatora")
        break
    else:
        print("Niepoprawny wyb�r")
        print
    
    
    
