import random

code = []
guess_count = 0
correct_place = 0
correct_number_wrong_place = 0

def generate_code(code_length):
    global code
    for i in range (0,code_length):
        code.append(random.randint(0,9))
    print(code)

def player_guess(code_length):
    print("podaj próbę odgadnięcia: ")
    for i in range (0,code_length):
        player_guess.append = int(input())

def evaluate_guess(code, player_guess):

    number_dictionary = {0: code.count(0), 1: code.count(1), 2: code.count(2), 3: code.count(3), 4: code.count(4), 5: code.count(5), 6: code.count(6), 7: code.count(7), 8: code.count(8), 9: code.count(9)}
     
    for i in range (0,code_length-1):
        if code[i]==player_guess[i]:
            correct_place = correct_place + 1
    for i in range (0,9):
        correct_number_wrong_place = correct_number_wrong_place + number_dictionary[i]
        if code[i]==player_guess[i]:
            correct_number_wrong_place = correct_number_wrong_place - 1
    
generate_code(int(input("podaj długość szyfru: ")))