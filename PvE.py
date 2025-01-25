import random

def początek_gry(nick):
    """
    jest to funkcja rozpoczynająca grę w trybie gracz vs komputer,
    prosi gracza o podanie szyfru, jeżeli poda błędny szyfr, będzie musiał zrobić to ponownie,
    funkcja zwróci szyfr w postaci listy, gdzie każda pozycja to jedna cyfra z szyfru
    """
    szyfr = input(f'{nick} podaj swój szyfr składający się z maksymalnie 6 cyfr: ')
    lista_szyfru = []
    for cyfra in szyfr:
        if len(szyfr) > 6:
           print("Podany szyfr jest niepoprawny, proszę podać szyfr skaładający się z maksymalnie 6 cyfr bez spacji.")
           break
        try:
            cyfra = int(cyfra)
        except:
            print("Podany szyfr jest niepoprawny, proszę podać szyfr skaładający się z maksymalnie 6 cyfr bez spacji.")
            break
        lista_szyfru.append(cyfra)
        if len(szyfr) == len(lista_szyfru):
            return lista_szyfru

def podpowiedzi_gracza(nick3):
    """
    jest to funkcja prosząca gracza o podanie liczby liczb na poprawnym miejscu oraz na złym miejscu w podanym zgadnięciu przez komputer,
    w przypadku podania wartości która nie jest liczbą, gracz zostanie o tym poinformowany oraz poproszony o ponowne wpisanie podpowiedzi,
    funkcja zwraca listę z dwoma wartościami, kolejno liczb na poprawnych miejscach oraz liczb na złych miejscach
    """
    liczba_cyfr_na_poprawnym_miejscu = input(f'{nick3} podaj liczbę cyfr na poprawnym miejscu: ')
    try:
        liczba_cyfr_na_poprawnym_miejscu = int(liczba_cyfr_na_poprawnym_miejscu)
    except:
        pass
    while type(liczba_cyfr_na_poprawnym_miejscu) != int:
        print("Liczba liczb na poprawnym miejscu ma być liczbą, proszę wpisać ponownie: ")
        liczba_cyfr_na_poprawnym_miejscu = input(f'{nick3} podaj liczbę cyfr na poprawnym miejscu: ')
        try:
            liczba_cyfr_na_poprawnym_miejscu = int(liczba_cyfr_na_poprawnym_miejscu)
        except:
            pass
    liczba_cyfr_na_złym_miejscu = input(f"{nick3} podaj liczbę cyfr na złym miejscu: ")
    try:
        liczba_cyfr_na_złym_miejscu = int(liczba_cyfr_na_złym_miejscu)
    except:
        pass
    while type(liczba_cyfr_na_złym_miejscu) != int:
        print("Liczba liczb na złym miejscu ma być liczbą, proszę wpisać ponownie: ")
        liczba_cyfr_na_złym_miejscu = input(f"{nick3} podaj liczbę cyfr na złym miejscu: ")
        try:
            liczba_cyfr_na_złym_miejscu = int(liczba_cyfr_na_złym_miejscu)
        except:
            pass
    return [liczba_cyfr_na_poprawnym_miejscu, liczba_cyfr_na_złym_miejscu]

def PvE(nick1):
    """
    jest to funkcja tworząca całą grę, wyświetla przebieg rozgrywki,
    pobiera nick gracza podany w main,
    używa również w sobie inne funkcje, które pomagają stworzyć grę,
    konkretnie ta funkcja interpretuje podpowiedzi gracza tak aby komputer odpowiednio zmieniał swoje zgadnięcie,
    jest również odporna na nieprawidłowe wartości, takie jak litery zamiast liczb czy spacje,
    kończy grę gdy komputer poprawnie odgadnie szyfr oraz podaje informację ile kroków zajęła rozgrywka
    """
    print(f"Witaj {nick1}, miło Cię gościć w trybie gracz vs komputer\n Teraz przedstawię Ci parę zasad naszej gry\n 1. Wymyślasz sobie szyfr długości maksymalnie 6 cyfr\n 2. W podpowiedziach ile cyfr jest na poprawnym miejscu, a ile na złym, proszę odpowiadać zgodnie z prawdą\n 3. Życzę miłej zabawy")
    szyfr_gracza = początek_gry(nick1)
    while szyfr_gracza == None:
        szyfr_gracza = początek_gry(nick1)
    def pierwsze_zgadnięcie_komputera():
        """
        jest to funkcja, która tworzy pierwsze losowe zgadnięcie przez komputer,
        funkcja zwraca listę w której znajdują się cyfry szyfru wygenerowanego przez komputer
        """
        try:
            zgadnięcie_w_liście = []
            liczba_cyfr_w_zgadnięciu = 0
            while liczba_cyfr_w_zgadnięciu < len(szyfr_gracza):
                liczba_cyfr_w_zgadnięciu += 1
                zgadnięcie_w_liście.append(random.randrange(0,10))
            return zgadnięcie_w_liście
        except:
            return None
    próby_zgadnięcia = pierwsze_zgadnięcie_komputera()
    def próba_zgadnięcia_szyfru():
        """
        jest to funkcja zamieniająca próby zgadnięcia szyfru z formatu listy na string, aby rzeczywiście był to szyfr
        """
        szyfr = ''
        for i in próby_zgadnięcia:
            szyfr += str(i)
        return szyfr
    lista_list_podpowiedzi = []
    liczba_kroków = 0
    while True:
        miejsce_cyfry_w_szyfsze = 0
        if liczba_kroków == 0:
            print(próba_zgadnięcia_szyfru())
            podpowiedzi_dla_komputera1 = podpowiedzi_gracza(nick1)
            lista_list_podpowiedzi.append(podpowiedzi_dla_komputera1)
        if liczba_kroków == 0:
            if próby_zgadnięcia[liczba_kroków] == 9:
                próby_zgadnięcia[liczba_kroków] = 0
            else:
                próby_zgadnięcia[liczba_kroków] = próby_zgadnięcia[liczba_kroków] + 1
            print(próba_zgadnięcia_szyfru())
            podpowiedzi_dla_komputera2 = podpowiedzi_gracza(nick1)
            lista_list_podpowiedzi.append(podpowiedzi_dla_komputera2)
            liczba_kroków += 1
        while True:
            if lista_list_podpowiedzi[liczba_kroków-1][0] == lista_list_podpowiedzi[liczba_kroków][0]:
                if próby_zgadnięcia[miejsce_cyfry_w_szyfsze] == 9:
                    próby_zgadnięcia[miejsce_cyfry_w_szyfsze] = 0
                else:
                    próby_zgadnięcia[miejsce_cyfry_w_szyfsze] = próby_zgadnięcia[miejsce_cyfry_w_szyfsze] + 1
                print(próba_zgadnięcia_szyfru())
                podpowiedzi_dla_komputera3 = podpowiedzi_gracza(nick1)
                lista_list_podpowiedzi.append(podpowiedzi_dla_komputera3)
                liczba_kroków += 1
                if lista_list_podpowiedzi[liczba_kroków][0] == len(szyfr_gracza):
                    print(f'Koniec gry komputer odgadł twój szyfr w {liczba_kroków} próbach')
                    liczba_kroków += 1
                    break
            if lista_list_podpowiedzi[liczba_kroków-1][0] < lista_list_podpowiedzi[liczba_kroków][0]:
                miejsce_cyfry_w_szyfsze += 1
                if próby_zgadnięcia[miejsce_cyfry_w_szyfsze] == 9:
                    próby_zgadnięcia[miejsce_cyfry_w_szyfsze] = 0
                else:
                    próby_zgadnięcia[miejsce_cyfry_w_szyfsze] = próby_zgadnięcia[miejsce_cyfry_w_szyfsze] + 1
                print(próba_zgadnięcia_szyfru())
                podpowiedzi_dla_komputera4 = podpowiedzi_gracza(nick1)
                lista_list_podpowiedzi.append(podpowiedzi_dla_komputera4)
                liczba_kroków += 1
                if lista_list_podpowiedzi[liczba_kroków][0] == len(szyfr_gracza):
                    print(f'Koniec gry komputer odgadł twój szyfr w {liczba_kroków} próbach')
                    liczba_kroków += 1
                    break
            if lista_list_podpowiedzi[liczba_kroków-1][0] > lista_list_podpowiedzi[liczba_kroków][0]:
                if próby_zgadnięcia[miejsce_cyfry_w_szyfsze] == 0:
                    próby_zgadnięcia[miejsce_cyfry_w_szyfsze] = 9
                else:
                    próby_zgadnięcia[miejsce_cyfry_w_szyfsze] = próby_zgadnięcia[miejsce_cyfry_w_szyfsze] - 1
                print(próba_zgadnięcia_szyfru())
                podpowiedzi_dla_komputera5 = podpowiedzi_gracza(nick1)
                lista_list_podpowiedzi.append(podpowiedzi_dla_komputera5)
                liczba_kroków += 1
                if lista_list_podpowiedzi[liczba_kroków][0] == len(szyfr_gracza):
                    print(f'Koniec gry komputer odgadł twój szyfr w {liczba_kroków} próbach')
                    liczba_kroków += 1
                    break
        break
    return None