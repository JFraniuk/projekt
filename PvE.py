import random

def początek_gry():
    szyfr = input("Podaj swój szyfr składający się z maksymalnie 6 cyfr: ")
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

def podpowiedzi_gracza():
    liczba_cyfr_na_poprawnym_miejscu = input("Proszę podać liczbę cyfr na poprawnym miejscu: ")
    try:
        liczba_cyfr_na_poprawnym_miejscu = int(liczba_cyfr_na_poprawnym_miejscu)
    except:
        pass
    while type(liczba_cyfr_na_poprawnym_miejscu) != int:
        print("Liczba liczb na poprawnym miejscu ma być liczbą, proszę wpisać ponownie: ")
        liczba_cyfr_na_poprawnym_miejscu = input("Proszę podać liczbę cyfr na poprawnym miejscu: ")
        try:
            liczba_cyfr_na_poprawnym_miejscu = int(liczba_cyfr_na_poprawnym_miejscu)
        except:
            pass
    liczba_cyfr_na_złym_miejscu = input("Proszę podać liczbę cyfr na złym miejscu: ")
    try:
        liczba_cyfr_na_złym_miejscu = int(liczba_cyfr_na_złym_miejscu)
    except:
        pass
    while type(liczba_cyfr_na_złym_miejscu) != int:
        print("Liczba liczb na złym miejscu ma być liczbą, proszę wpisać ponownie: ")
        liczba_cyfr_na_złym_miejscu = input("Proszę podać liczbę cyfr na złym miejscu: ")
        try:
            liczba_cyfr_na_złym_miejscu = int(liczba_cyfr_na_złym_miejscu)
        except:
            pass
    return [liczba_cyfr_na_poprawnym_miejscu, liczba_cyfr_na_złym_miejscu]

def PvE():
    szyfr_gracza = początek_gry()
    while szyfr_gracza == None:
        szyfr_gracza = początek_gry()
    def pierwsze_zgadnięcie_komputera():
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
            podpowiedzi_dla_komputera1 = podpowiedzi_gracza()
            lista_list_podpowiedzi.append(podpowiedzi_dla_komputera1)
        if liczba_kroków == 0:
            if próby_zgadnięcia[liczba_kroków] == 9:
                próby_zgadnięcia[liczba_kroków] = 0
            else:
                próby_zgadnięcia[liczba_kroków] = próby_zgadnięcia[liczba_kroków] + 1
            print(próba_zgadnięcia_szyfru())
            podpowiedzi_dla_komputera2 = podpowiedzi_gracza()
            lista_list_podpowiedzi.append(podpowiedzi_dla_komputera2)
            liczba_kroków += 1
        while True:
            if lista_list_podpowiedzi[liczba_kroków-1][0] == lista_list_podpowiedzi[liczba_kroków][0]:
                if próby_zgadnięcia[miejsce_cyfry_w_szyfsze] == 9:
                    próby_zgadnięcia[miejsce_cyfry_w_szyfsze] = 0
                else:
                    próby_zgadnięcia[miejsce_cyfry_w_szyfsze] = próby_zgadnięcia[miejsce_cyfry_w_szyfsze] + 1
                print(próba_zgadnięcia_szyfru())
                podpowiedzi_dla_komputera3 = podpowiedzi_gracza()
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
                podpowiedzi_dla_komputera4 = podpowiedzi_gracza()
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
                podpowiedzi_dla_komputera5 = podpowiedzi_gracza()
                lista_list_podpowiedzi.append(podpowiedzi_dla_komputera5)
                liczba_kroków += 1
                if lista_list_podpowiedzi[liczba_kroków][0] == len(szyfr_gracza):
                    print(f'Koniec gry komputer odgadł twój szyfr w {liczba_kroków} próbach')
                    liczba_kroków += 1
                    break
        break
    return None
