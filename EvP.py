import random

code = []
guess_count = 0
correct_place = 0
correct_number_wrong_place = 0
code_length = 6

def generate_code(code_length):
    '''
    Funkcja generate_code odpowiada za początkowe generowanie kodu przez komputer, który później odgaduje gracz.
    Wywołuje ona globalną zmienną code, po czym iteracyjnie zapełnia listę o długości code_length code integerami z zakresu (0,9).
    '''
    global code
    code = []
    for i in range (0,code_length):
        code.append(random.randint(0,9))

def player_guess_reader(code_length):
    '''
    Funkcja player_guess_reader sczytuje próbę zgadnięcia kodu jako input string, player_guess_str, o długości globalnej zmiennej code_length. Najpierw sprawdza czy string ma odpowiednią długość,
    po czym sprawdza format każdego znaku w stringu, aby upewnić się, że są cyframi. Następnie iteruje przez każdy znak player_guess_str wymuszając typ int, tworząc int list player_guess.
    '''
    player_guess_str = input("Podaj próbę odgadnięcia: ")
    while len(player_guess_str) != code_length or not player_guess_str.isdigit():
        print(f"Nieprawidłowy format! Wprowadź dokładnie {code_length} cyfr.")
        player_guess_str = input("Podaj próbę odgadnięcia: ")
    player_guess = [int(x) for x in player_guess_str]
    print(player_guess)
    return player_guess

def evaluate_guess(code, player_guess):
    '''
    Funkcja evaluate_guess wylciza zmienne correct_place i correct_number_wrong_place na bazie int list code i player_guess. Zwraca liczbę cyfr w próbie zgadnięcia, które są na tym samym miejscu w liście code,
    oraz liczbę cyfr, które występują w liście code, ale nie są na poprawnym miejscu. Wywołuej globalne zmienne correct_place i correct_number_wrong_place, po czym sprawdza dla każdego indeksu (0, code_length)
    porównuje dany indeks z listy code i player_guess, jeżeli warunek jest spełniony, licznik correct_place wzrasta o 1. Następna pętla odpowiada za correct_number_wrong_place. Dla każdego indeksu w zakresie
    (0, code_length) dla listy code iteruje przez każdy indeks listy player_guess. Licznik zwiększa się o 1 wyłącznie jeśli indeksy i i j są różne.
    '''
    global correct_place
    global correct_number_wrong_place
    correct_place = 0
    correct_number_wrong_place = 0
    
    matched_code = [False] * code_length
    matched_guess = [False] * code_length
    
    for i in range (0, code_length):
        if code[i] == player_guess[i]:
            correct_place += 1
            matched_code[i] = True
            matched_guess[i] = True
        
    for i in range(0, code_length):
        if not matched_guess[i]:
            for j in range(0, code_length):
                if (
                    not matched_code[j]
                    and player_guess[i] == code[j]
                    and i != j
                ):
                    correct_number_wrong_place += 1
                    matched_code[j] = True
                    break
            

def gra(nick1):
    '''
    Funkcja gra odpowiada za przebieg gry, po princie powitania gracza i krótkiego opisu przebiegu, generuje kod, po czym wykorzystująć pętlę while True, wywołuje funkcje player_guess_reader oraz evaluate_guess
    aby przy każdej rundzie gracz mógł podać nowy kod. Pętla kończy się, jeżeli int listy code i player_guess są identyczne. Po końcu pętli podaje też liczbę prób w danej grze.
    '''
    global guess_count
    guess_count = 0
    
    print(f"Witaj {nick1}, w trybie gracz vs komputer!\nW tym trybie, komputer podaje kod, którego zgadnięcie jest zadaniem gracza.\nJako gracz twoja tura polega na wprowadzniu próby zgadnięcia,\nna co komputer odpowie liczbą odgadniętych cyfr, oraz liczbą cyfr w szyfrze, które nie są na swoim miejscu.\nPowodzenia!")
    
    generate_code(code_length)
    
    while True:
        guess_count += 1
        
        print(f"Próba {guess_count}:")
        player_guess = player_guess_reader(code_length)

        if code == player_guess:
            print(f"Gra zakończona! Liczba zgadnięć: {guess_count}")
            break 
        
        evaluate_guess(code, player_guess)
        
        print(f"Poprawne miejsca: {correct_place}, Poprawne liczby w złych miejscach: {correct_number_wrong_place}")


