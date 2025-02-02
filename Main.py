import argparse
import PvP
import PvE
import EvP
import os

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--tryb", help = "Podaj tryb gry: PvP, PvE, EvP")
parser.add_argument("-n1", "--nick1", help = "Podaj nick gracza")
parser.add_argument("-n2", "--nick2", help = "Podaj nick drugiego gracza, jeśli tryb gry to PvP")

args = parser.parse_args() # parsowanie argumentow podanych przez uzytkownika

trybGry = args.tryb
nick1 = args.nick1
nick2 = args.nick2

tryb_gry_zbior={"PvP","PvE","EvP"}

if trybGry not in tryb_gry_zbior:
    print("Witaj w grze w odgadywanie! \nNiewybrano, bądź wybrano niewłaściwy tryb gry.\nWybierz tryb gry:\n1. gracz vs gracz (wybierz 1 lub PvP)\n2. gracz vs komputer (wybierz 2 lub PvE)\n3. komputer vs gracz (wybierz 3 lub EvP)")
    wybor = input()

    while True:
        match wybor:
            case "1"|"PvP":
                trybGry = "PvP"
                break
            case "2"|"PvE":
                trybGry = "PvE"
                break
            case "3"|"EvP": 
                trybGry = "EvP"
                break
            case _:
                os.system('cls') #czyszczenie ekranu
                print("Podano niewłaściwy tryb gry. \nPrzanalizuj dostępne opcje i wybierz tryb gry w który masz ochotę zagrać.\n1. gracz vs gracz (wybierz 1 lub PvP)\n2. gracz vs komputer (wybierz 2 lub PvE)\n3. komputer vs gracz (wybierz 3 lub EvP)")
                wybor = input()

print(f"Wybrano tryb gry: {trybGry}")
if nick1 == None:
    nick1 = input("Podaj swój nick: ")

if trybGry == "PvP" and nick2 == None:
    nick2 = input("Podaj nick drugiego gracza: ")

match trybGry:
    case "PvP":
        PvP.pvp(nick1, nick2)
    case "PvE":
        PvE.PvE(nick1)
    case "EvP":
        EvP.gra(nick1)
        pass
