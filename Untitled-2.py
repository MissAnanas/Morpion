import random
import os

array = [[0, 0, 0] for _ in range(3)]
moves = [[i, j] for i in range(3) for j in range(3)]
played_moves = []
symbols = {0: " ", 1: "X", 2: "O"}

def display_board():
    os.system("cls")
    print("---------------------☺---------------------")
    for row in array:
        print(" | ".join(map(lambda cell: symbols[cell], row)))
        print("-" * 9)
    print("---------------------☺---------------------")

def check_game_result(player):
    win_conditions = [
        all(array[i][j] == player for j in range(3)) for i in range(3),  # lignes
        all(array[j][i] == player for j in range(3)) for i in range(3),  # colonnes
        all(array[i][i] == player for i in range(3)),  # diagonale 1
        all(array[i][2 - i] == player for i in range(3))  # diagonale 2
    ]

    if any(win_conditions):
        return True, f"Joueur {player} a gagné ! Félicitations!"

    if all(array[i][j] != 0 for i in range(3) for j in range(3)):
        return True, "La partie est terminée. Match nul!"

    return False, ""


def ask_coordinates(message: str) -> tuple[int, int]:
    while True:
        try:
            user_input = input(message)
            coords = user_input.replace(',', ' ').split() if ',' in user_input else user_input.split()
            if len(coords) != 2:
                raise ValueError("Veuillez entrer deux chiffres.")

            row, col = int(coords[0]), int(coords[1])
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Veuillez entrer des chiffres entre 0 et 2.")
        except ValueError as e:
            print(f"Entrée invalide : {e}")

def make_player_move(player):
    while True:
        print("Cases disponibles :", moves)
        try:
            row, col = ask_coordinates(f"Joueur {player}, choisissez la case (les deux chiffres collés) : ")
            if array[row][col] == 0:
                array[row][col] = player
                moves.remove([row, col])
                played_moves.append((row, col))
                result, message = check_game_result(player)

                display_board()
                print(message)

                if result:
                    return True
                else:
                    return False
            else:
                print("Coup invalide. Choisissez une autre case.")
        except ValueError:
            print("Entrées invalides. Veuillez saisir des chiffres entre 0 et 2.")

def play_tic_tac_toe():
    player = 1

    while True:
        display_board()
        if player == 1:
            if make_player_move(player):
                break
            player = 3 - player
        else:
            random_move = random.choice(moves)
            if random_move:
                row, col = random_move
                array[row][col] = player
                played_moves.append((row, col))
                result, message = check_game_result(player)

                display_board()
                print(message)

                if result:
                    break
                else:
                    player = 3 - player

play_tic_tac_toe()
