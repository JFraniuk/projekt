import random

code = []
guess_count = 0
correct_place = 0
correct_number_wrong_place = 0
code_length = 6

def generate_code(code_length):
    global code
    code = []
    for i in range (0,code_length):
        code.append(random.randint(0,9))
    print(code)

def player_guess_reader(code_length):
    player_guess_str = input("Podaj próbę odgadnięcia: ")
    while len(player_guess_str) != code_length or not player_guess_str.isdigit():
        print(f"Nieprawidłowy format! Wprowadź dokładnie {code_length} cyfr.")
        player_guess_str = input("Podaj próbę odgadnięcia: ")
    player_guess = [int(x) for x in player_guess_str]
    print(player_guess)
    return player_guess


def evaluate_guess(code, player_guess):
    global correct_place
    global correct_number_wrong_place
    correct_place = 0
    correct_number_wrong_plac = 0
    
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
            

def gra():
    global guess_count
    guess_count = 0
    
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


