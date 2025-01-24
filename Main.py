import argparse
import PvP
import PvE
import EvP

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--tryb", help="Podaj tryb gry: PvP, PvE, EvP")
parser.add_argument("-n", "--nick1", help = "Podaj nick gracza")
parser.add_argument("-n2", "--nick2", help = "Podaj nick drugiego gracza")

args = parser.parse_args() # parsowanie argumentow podanych przez uzytkownika

trybGry = args.tryb
nick1 = args.nick1
nick2 = args.nick2

if trybGry == None:
    print("Witaj w świecie, wybierz opcję gry\n1.gracz vs gracz\n2.gracz vs komputer\n3.komputer vs gracz")
    wybor = input()

    while True:
        match wybor:
            case "1":
                trybGry = "PvP"
                break
            case "2":
                trybGry = "PvE"
                break
            case "3": 
                trybGry = "EvP"
                break
            case _:
                print("Niewlasciwy tryb gry, podaj jeszcze raz:")
                wybor = input()

print(trybGry)
if nick1 == None:
    nick1 = input("Podaj swój nick: ")

if trybGry == "PvP" and nick2 == None:
    nick2 = input("Podaj nick drugiego gracza: ")

match trybGry:
    case "PvP":
        PvP.pvp(nick1, nick2)
    case "PvE":
        PvE.PvE()
    case "EvP":
        pass #TODO
