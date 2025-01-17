
import os
import time 

def pvp():
    print ("GRACZU 1")
    while True:
        try:
            n=int(input("podaj długość wymyślonego szyfru: \n"))
            break
        except ValueError:
            print("błąd, podana długość szyfru musi być liczbą całkowitą; spróbuj ponownie \n")

    while True:
        szyfr=input(f"podaj {n} cyfrowy szyfr \n")

        if(len(szyfr)==n):
            break
        else:
            print(f"błąd, upewnij się, że wpisujesz {n} cyfr")

    ile=0
    poprzednie=[]

    
    time.sleep(1)
    os.system('cls')


    while True:
        ile=ile+1
        print ("GRACZU 2")
        while True:
            odgadniecie=input(f"odgadnij szyfr o długości {n} cyfr \n")

            if(len(odgadniecie)==n):
                break
            else:
                print(f"błąd, upewnij się, że wpisujesz {n} cyfr")

        time.sleep(1)
        os.system('cls')
        
        while True:
                try:
                    potwierdzenie=int(input("przekaż klawiature drugiemu graczowi, po przekazaniu niech wpisze '1' \n"))
                    if potwierdzenie==1:
                        break
                    else:
                        print("wpisz 1 aby potwierdzic \n")
                except ValueError:
                    print("błąd, wpisz 1 aby potwierdzić \n")

        time.sleep(1)
        os.system('cls')

        print("GRACZU 1")
        print("podany przez ciebie szyfr to: ", szyfr)
        print("podane odgadnięcie przez GRACZA 2 to: ", odgadniecie)
        
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

        if(prawidlowe==n):
            print(f"GRATULACJE, GRACZ 2 odgadł szyfr w {ile} próbach")
            print("szyfr to: ", szyfr)
            break

        while True:
                try:
                    potwierdzenie=int(input("przekaż klawiature drugiemu graczowi, po przekazaniu niech wpisze '1' "))
                    if potwierdzenie==1:
                        break
                    else:
                        print("wpisz 1 aby potwierdzic ")
                except ValueError:
                    print("błąd, wpisz 1 aby potwierdzić")

        time.sleep(1)
        os.system('cls')

        poprzednie.append((odgadniecie, prawidlowe, zle))
        print("poprzednie odgadnięcia: ")
        for i, (poprzednieodgadniecie, poprzednieprawidlowe, poprzedniezle) in enumerate(poprzednie, start=1):
            print(f"próba nr {i}: {poprzednieodgadniecie}, trafienia na prawidłowym miejscu: {poprzednieprawidlowe}, trafienia prawidłowa cyfra, ale na złym miejscu: {poprzedniezle}")



    