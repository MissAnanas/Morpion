import random
import os
from Fonction import *


    
while True:

    # Fonction ask_int, ask_coordinates, etc. définies dans Fonction.py
    def create_board(size):
        return [[0 for _ in range(size)] for _ in range(size)]

    def main():
        print("---------------------☺---------------------")
        print("Bienvenue sur ce jeu du Morpion !")

        reponse = input("Souhaitez-vous consulter les règles (Y/N) ? ")
        if reponse.upper() == "Y":
            # Affichage des règles du jeu
            print("---------------------☺---------------------")
            print("Règles :")
            print("- Le but du jeu est de vaincre l'ordinateur. - ")
            print("------> - La partie se joue sur plusieurs manches !")
            print("------> - Vous avez l'un après l'autre le choix d'une case du tableau où vous placerez un symbole (X ou O)")
            print("------> - Pour gagner, il vous faudra aligner 3 symboles consécutifs (ou plus selon votre choix) en premier (verticale, horizontale ou diagonale)")
            print("------> - Réfléchissez bien et n'oubliez pas de bloquer l'adversaire au besoin !")

        def initialize_game():
            print("---------------------☺---------------------")
            min_val = 3
            max_val = 100
            size = ask_int("Entrez la taille du morpion (min 3, max 100) : ", min_val, max_val)
            if size < min_val:
                print(f"La taille minimale du morpion doit être {min_val}.")
                return initialize_game()
            else:
                return create_board(size)

        def ask_win_condition(size: int) -> int:
            return ask_int(f"Combien de symboles consécutifs pour gagner ? (minimum 3) ", 3, size)

        def display_board(array, size):
            os.system("cls") if os.name == "nt" else os.system("clear")
            symbols = {0: " ", 1: "X", 2: "O"}
            print("---------------------☺---------------------")
            print("-" * (4 * size - 2))
            for row in array:
                print(" | ".join(map(lambda cell: symbols[cell], row)))
                print("-" * (4 * size - 2))
            print("---------------------☺---------------------")

        def check_game_result(array: list[list[int]], symbol, size, win_condition, last_move) -> tuple[bool, str]:
            row, col = last_move

            # Vérifier la ligne
            if col + win_condition <= size and all(array[row][i] == symbol for i in range(col, col + win_condition)):
                return True, f"Joueur {symbol} a gagné ! Félicitations!"

            # Vérifier la colonne
            if row + win_condition <= size and all(array[i][col] == symbol for i in range(row, row + win_condition)):
                return True, f"Joueur {symbol} a gagné ! Félicitations!"

            # Vérifier la diagonale principale
            if row - win_condition + 1 >= 0 and col - win_condition + 1 >= 0 and all(array[row - i][col - i] == symbol for i in range(win_condition)):
                return True, f"Joueur {symbol} a gagné ! Félicitations."

            # Vérifier l'anti-diagonale
            if row - win_condition + 1 >= 0 and col + win_condition - 1 < size and all(array[row - i][col + i] == symbol for i in range(win_condition)):
                return True, f"Joueur {symbol} a gagné ! Félicitations."

            if all(array[i][j] != 0 for i in range(size) for j in range(size)):
                return True, "La partie est terminée. Match nul!"

            return False, ""

        def make_player_move(array, symbol, moves, size, win_condition) -> tuple[bool, tuple[int, int]]:
            while True:
                print("Cases disponibles :", moves)
                row, col = ask_coordinates(f"Joueur {symbol}, choisissez la case : ", size)
                if array[row][col] == 0:
                    array[row][col] = symbol
                    moves.remove([row, col])
                    result, message = check_game_result(array, symbol, size, win_condition, (row, col))
                    display_board(array, size)
                    print(message)
                    if result:
                        return True, (row, col)
                    return False, (row, col)
                print("Coup invalide. Choisissez une autre case.")


        def get_random_move(moves):
            if moves:
                random_index = random.randint(0, len(moves) - 1)
                array_index = moves.pop(random_index)
                return array_index
            else:
                return None

        def get_ai_move(array, moves, size, win_condition, last_move):
            # Recherche d'une victoire possible pour l'IA
            winning_move = find_winning_move(array, moves, size, win_condition, 2, last_move)
            if winning_move:
                return winning_move

            # Recherche d'une victoire possible pour le joueur pour bloquer
            blocking_move = find_winning_move(array, moves, size, win_condition, 1, last_move)
            if blocking_move:
                return blocking_move

            return get_random_move(moves)

        # Fonction pour trouver un coup gagnant
        def find_winning_move(array, moves, size, win_condition, symbol, last_move):
            for move in moves:
                row, col = move
                array[row][col] = symbol  # Simuler le coup du joueur ou de l'IA
                if check_game_result(array, symbol, size, win_condition, last_move)[0]:
                    array[row][col] = 0  # Réinitialiser le coup
                    return move
                array[row][col] = 0  # Réinitialiser le coup après la vérification

            return None

        def play_tictactoe():
            symbol = 1
            array = initialize_game()
            size = len(array)
            moves = [[i, j] for i in range(size) for j in range(size)]
            win_condition = ask_win_condition(size)
            last_move: tuple[int, int] = None

            while True:
                display_board(array, size)

                if symbol == 1:
                    result, last_move = make_player_move(array, symbol, moves, size, win_condition)
                    if result:
                        break
                    symbol = 3 - symbol
                else:
                    if last_move is None:
                        print("Error")

                    ai_move = get_ai_move(array, moves, size, win_condition, last_move)
                    if ai_move:
                        row, col = ai_move
                        array[row][col] = symbol
                        result, message = check_game_result(array, symbol, size, win_condition, ai_move)
                        display_board(array, size)
                        print(message)
                        if result:
                            break
                        else:
                            symbol = 3 - symbol

        play_tictactoe()
    main()
    reponse = print("---------------------☺------------------")
    reponse = input("Souhaitez-vous relancer une partie (Y/N) ?")
    if reponse.upper() != "Y":
        print("---------------------☺---------------------")
        print("Merci d'avoir joué ! A bientôt :)")
        print("---------------------☺---------------------")
        break
        


