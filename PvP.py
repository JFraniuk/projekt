
import os
import time

def pvp(nick1, nick2):
    """
    funkcja odpowiada za gre w trybie gracz vs gracz, gdzie jeden gracz wymyśla szyfr a drugi go odgaduje

    funkcja pobiera nick1 i nick2 podane w main 

    wyświetla przebieg gry
    pyta gracza nick1 o rolę; 
        wybor 1 przypisuje mu zgadującego, a nick2 odgadującego 
        wybor 2 przypisuje mu odgadującego, a nick2 zgadującego
    wprowadzenie szyfru; podanie dlugosci, a potem ciągu cyfr o określonej dlugosci
    zgadywaie szyfru; podanie odgadnięcia
    ocenienie szyfru; podanie ilosc cyfr na prawidlowym miejscu i ilość na złym miejscu, ale są w szyfrze
    sprawdzenie wygranej; jezeli ilosc cyfr na prawidlowym miejscu i ilosc cyfr w kodzie sie zgadza to koniec gry, jezeli nie to gra trwa dalej
    zapisanie poprzednich prób i wyniku do listy; wyświetlana jest przy kolejnych próbach odgadnięcia
    funkcja obsługuje błędy; czy wprowadzane wartości są liczbami, czy mają odpowiednią długość

    """

    #witanie graczy i zasady gry
    print("")
    print(f"witajcie gracze {nick1} i {nick2}, zapoznajcie się z przebiegiem gry w trybie gracz vs gracz:")
    print("")
    print("jeden z graczy będzie odpowiedzialny za wymyślenie szyfru o dowolnej długości. istotna jest kolejność, a cyfry mogą się powtarzać")
    print("drugi gracz dostanie informacje z ilu cyfr składa się szyfr. następnie musi podać ciąg cyfr, który myśli że jest szyfrem")
    print("zaraz potem, gracz który wymyślał szyfr, podaje odgadującemu ile cyfr jest na swoich miejscach oraz ile jest w szyfrze, ale nie na swoich miejscach")
    print("jeżeli gracz odgadł szyfr to gra się kończy, w innym wypadku podaje kolejny ciąg cyfr")
    print("")
    print("zdecydujcie o rolach: ")

    #wybór ról
    while True:
        try:
            corobi=int(input(f"{nick1}, chcesz wymyślić czy odgadywać szyfr? \n wpisz '1' jeżeli chcesz wymyślić szyfr \n wpisz '2' jeżeli chcesz go odgadywać\n"))
            if corobi==1:
                wymyslacz=nick1
                odgadywacz=nick2
                print(f"{wymyslacz} wymyśli szyfr, a {odgadywacz} będzie go odgadywał\n")
                break
            elif corobi==2:
                wymyslacz=nick2
                odgadywacz=nick1
                print(f"{wymyslacz} wymyśli szyfr, a {odgadywacz} będzie go zgadywać\n")
                break
        except ValueError:
            print("błąd, wpisz 1 lub 2 aby potwierdzić \n")

    print("")

    #podanie ilosc cyfr do szyfru
    print (f"{wymyslacz}")
    while True:
        try:
            n=int(input("podaj długość wymyślonego szyfru: \n"))
            break
        except ValueError:
            print("błąd, podana długość szyfru musi być liczbą całkowitą; spróbuj ponownie \n")

    #podanie szyfru
    while True:
        szyfr=input(f"podaj {n} cyfrowy szyfr \n")

        if(len(szyfr)==n):
            break
        else:
            print(f"błąd, upewnij się, że wpisujesz {n} cyfr")

    ile=0 #licznik prob zgadniecia
    poprzednie=[] #lista przechowujaca poprzednie proby

    
    time.sleep(1)
    os.system('cls') #czyszczenie ekranu aby odgadywacz nie widzial szyfru 

    #zgadywanie przez drugiego gracza 
    while True:
        ile=ile+1 #zwieksza liczbe prob
        print (f"{odgadywacz}")
        while True:
            odgadniecie=input(f"odgadnij szyfr o długości {n} cyfr \n")

            if(len(odgadniecie)==n):
                break
            else:
                print(f"błąd, upewnij się, że wpisujesz {n} cyfr")

        time.sleep(1)
        os.system('cls') #czyszczenie ekranu 
        
        #potwierdzenie przekazania klawiatury dla drugieog gracza 
        while True:
                try:
                    potwierdzenie=int(input(f"przekaż klawiature dla {wymyslacz}, po przekazaniu niech wpisze '1' \n"))
                    if potwierdzenie==1:
                        break
                    else:
                        print("wpisz 1 aby potwierdzic \n")
                except ValueError:
                    print("błąd, wpisz 1 aby potwierdzić \n")

        time.sleep(1)
        os.system('cls') #czyszczenie ekranu aby odgadywacz nie widzial szyfru 

        #wymyslacz ocenia szyfr
        print(f"{wymyslacz}")
        print("podany przez ciebie szyfr to: ", szyfr)
        print(f"podane odgadnięcie przez {odgadywacz} to: ", odgadniecie)
        
        while True:
            try:
                prawidlowe=int(input("podaj ilość cyfr na prawidłowych miejscach \n"))
                break
            except ValueError:
                print("błąd, upewnij się, że podajesz liczby")
            
        while True:
            try:
                zle=int(input("podaj ilość cyfr, które znajdują się w kodzie, ale są na złych miejscach \n"))
                break
            except ValueError:
                print("błąd, upewnij się, że podajesz liczby")
            
        
        time.sleep(1)
        os.system('cls')

        #sprawdzenie czy szyfr byl odgadniety czy nie 
        if(prawidlowe==n):
            print(f"GRATULACJE, {odgadywacz} odgadł szyfr w {ile} próbach")
            print("szyfr to: ", szyfr)
            break
        
        #przekazanie klawiatury dla odgadywacza 
        while True:
                try:
                    potwierdzenie=int(input(f"przekaż klawiature dla {odgadywacz}, po przekazaniu niech wpisze '1' "))
                    if potwierdzenie==1:
                        break
                    else:
                        print("wpisz 1 aby potwierdzic ")
                except ValueError:
                    print("błąd, wpisz 1 aby potwierdzić")

        time.sleep(1)
        os.system('cls')

        #zapisywanie poprzednich prob 
        poprzednie.append((odgadniecie, prawidlowe, zle))
        print("poprzednie odgadnięcia: ")
        for i, (poprzednieodgadniecie, poprzednieprawidlowe, poprzedniezle) in enumerate(poprzednie, start=1):
            print(f"próba nr {i}: {poprzednieodgadniecie}, trafienia na prawidłowym miejscu: {poprzednieprawidlowe}, trafienia prawidłowa cyfra, ale na złym miejscu: {poprzedniezle}")



    