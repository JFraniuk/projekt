
import os
import time

def pvp(nick1, nick2):
    """
    Funkcja odpowiada za grę w trybie gracz vs gracz, gdzie jeden gracz wymyśla szyfr a drugi go odgaduje.

    Funkcja pobiera nick1 i nick2 podane w main. 

    Wyświetla przebieg gry.
    Pyta gracza nick1 o rolę; 
        Wybor 1 przypisuje mu zgadującego, a nick2 odgadującego. 
        Wybor 2 przypisuje mu odgadującego, a nick2 zgadującego.
    Wprowadzenie szyfru; podanie dlugosci, a potem ciągu cyfr o określonej dlugosci.
    Zgadywaie szyfru; podanie odgadnięcia.
    Ocenienie szyfru; podanie ilosc cyfr na prawidlowym miejscu i ilość na złym miejscu, ale są w szyfrze.
    Sprawdzenie wygranej; jezeli ilosc cyfr na prawidlowym miejscu i ilosc cyfr w kodzie sie zgadza to koniec gry, jezeli nie to gra trwa dalej.
    Zapisanie poprzednich prób i wyniku do listy; wyświetlana jest przy kolejnych próbach odgadnięcia.
    Funkcja obsługuje błędy; czy wprowadzane wartości są liczbami, czy mają odpowiednią długość.

    """

    #witanie graczy i zasady gry
    print("")
    print(f"Witajcie gracze {nick1} i {nick2}, zapoznajcie się z przebiegiem gry w trybie gracz vs gracz:")
    print("")
    print("Jeden z graczy będzie odpowiedzialny za wymyślenie szyfru o dowolnej długości. istotna jest kolejność, a cyfry mogą się powtarzać.")
    print("Drugi gracz dostanie informacje z ilu cyfr składa się szyfr. następnie musi podać ciąg cyfr, który myśli że jest szyfrem.")
    print("Zaraz potem, gracz który wymyślał szyfr, podaje odgadującemu ile cyfr jest na swoich miejscach oraz ile jest w szyfrze, ale nie na swoich miejscach.")
    print("Jeżeli gracz odgadł szyfr to gra się kończy, w innym wypadku podaje kolejny ciąg cyfr.")
    print("")
    print("Zdecydujcie o rolach: ")

    #wybór ról
    while True:
        try:
            corobi=int(input(f"{nick1}, chcesz wymyślić czy odgadywać szyfr? \n Wpisz '1' jeżeli chcesz wymyślić szyfr. \n Wpisz '2' jeżeli chcesz go odgadywać.\n"))
            if corobi==1:
                wymyslacz=nick1
                odgadywacz=nick2
                print(f"{wymyslacz} wymyśli szyfr, a {odgadywacz} będzie go odgadywał.\n")
                time.sleep(3)
                os.system('cls')
                break
            elif corobi==2:
                wymyslacz=nick2
                odgadywacz=nick1
                print(f"{wymyslacz} wymyśli szyfr, a {odgadywacz} będzie go zgadywać.\n")
                time.sleep(3)
                os.system('cls')
                break
        except ValueError:
            print("Błąd, wpisz 1 lub 2 aby potwierdzić. \n")

    print("")

    #podanie ilosc cyfr do szyfru
    print (f"{wymyslacz}")
    while True:
        try:
            n=int(input("Podaj długość wymyślonego szyfru: \n"))
            break
        except ValueError:
            print("Błąd, podana długość szyfru musi być liczbą całkowitą; spróbuj ponownie. \n")

    #podanie szyfru
    while True:
        szyfr=input(f"Podaj {n} cyfrowy szyfr. \n")

        if(len(szyfr)==n):
            break
        else:
            print(f"Błąd, upewnij się, że wpisujesz {n} cyfr.")

    ile=0 #licznik prob zgadniecia
    poprzednie=[] #lista przechowujaca poprzednie proby

    
    time.sleep(1)
    os.system('cls') #czyszczenie ekranu aby odgadywacz nie widzial szyfru 

    #zgadywanie przez drugiego gracza 
    while True:
        ile=ile+1 #zwieksza liczbe prob
        print (f"{odgadywacz}")
        while True:
            odgadniecie=input(f"Odgadnij szyfr o długości {n} cyfr. \n")

            if(len(odgadniecie)==n):
                break
            else:
                print(f"Błąd, upewnij się, że wpisujesz {n} cyfr.")

        time.sleep(1)
        os.system('cls') #czyszczenie ekranu 
        
        #potwierdzenie przekazania klawiatury dla drugieog gracza 
        while True:
                try:
                    potwierdzenie=int(input(f"Przekaż klawiature dla gracza {wymyslacz}, po przekazaniu niech wpisze '1'. \n"))
                    if potwierdzenie==1:
                        break
                    else:
                        print("Wpisz 1 aby potwierdzic. \n")
                except ValueError:
                    print("Błąd, wpisz 1 aby potwierdzić. \n")

        time.sleep(1)
        os.system('cls') #czyszczenie ekranu aby odgadywacz nie widzial szyfru 

        #wymyslacz ocenia szyfr
        print(f"{wymyslacz}")
        print("Podany przez ciebie szyfr to: ", szyfr)
        print(f"Podane odgadnięcie przez {odgadywacz} to: ", odgadniecie)
        
        while True:
            try:
                prawidlowe=int(input("Podaj ilość cyfr na prawidłowych miejscach. \n"))
                break
            except ValueError:
                print("Błąd, upewnij się, że podajesz liczby.")
            
        while True:
            try:
                zle=int(input("Podaj ilość cyfr, które znajdują się w kodzie, ale są na złych miejscach. \n"))
                break
            except ValueError:
                print("Błąd, upewnij się, że podajesz liczby")
            
        
        time.sleep(1)
        os.system('cls')

        #sprawdzenie czy szyfr byl odgadniety czy nie 
        if(prawidlowe==n):
            print(f"GRATULACJE, gracz {odgadywacz} odgadł szyfr w {ile} próbach.")
            print("Szyfr to: ", szyfr)
            break
        
        #przekazanie klawiatury dla odgadywacza 
        while True:
                try:
                    potwierdzenie=int(input(f"Przekaż klawiature dla gracza {odgadywacz}, po przekazaniu niech wpisze '1'. "))
                    if potwierdzenie==1:
                        break
                    else:
                        print("Wpisz 1 aby potwierdzić.")
                except ValueError:
                    print("Błąd, wpisz 1 aby potwierdzić")

        time.sleep(1)
        os.system('cls')

        #zapisywanie poprzednich prob 
        poprzednie.append((odgadniecie, prawidlowe, zle))
        print("poprzednie odgadnięcia: ")
        for i, (poprzednieodgadniecie, poprzednieprawidlowe, poprzedniezle) in enumerate(poprzednie, start=1):
            print(f"Próba nr {i}: {poprzednieodgadniecie}, trafienia na prawidłowym miejscu: {poprzednieprawidlowe}, trafienia prawidłowa cyfra, ale na złym miejscu: {poprzedniezle}")



    