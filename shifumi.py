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
            max_val = 10000
            size = ask_int("Entrez la taille du morpion (min 3, max 10000) : ", min_val, max_val)
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

        def check_game_result(array: list[list[int]], symbol: int, size: int, win_condition: int, last_move: tuple[int, int]) -> tuple[bool, str]:
            row, col = last_move

            # Vérifier la ligne
            line_win = True
            for i in range(size):
                if array[row][i] != symbol:
                    line_win = False
                    break
            if line_win:
                return True, f"Joueur {symbol} a gagné ! Félicitations!"

            # Vérifier la colonne
            col_win = True
            for i in range(size):
                if array[i][col] != symbol:
                    col_win = False
                    break
            if col_win:
                return True, f"Joueur {symbol} a gagné ! Félicitations."

            # Vérifier la diagonale principale
            main_diag_win = True
            for i in range(win_condition):
                if row - i < 0 or col - i < 0 or array[row - i][col - i] != symbol:
                    main_diag_win = False
                    break
            if main_diag_win:
                return True, f"Joueur {symbol} a gagné ! Félicitations."

            # Vérifier l'anti-diagonale
            anti_diag_win = True
            for i in range(win_condition):
                if row - i < 0 or col + i >= size or array[row - i][col + i] != symbol:
                    anti_diag_win = False
                    break
            if anti_diag_win:
                return True, f"Joueur {symbol} a gagné ! Félicitations."

            match_nul = True
            for i in range(size):
                for j in range(size):
                    if array[i][j] == 0:
                        match_nul = False
                        break
            if match_nul:
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
            winning_move = find_winning_move(array, moves, size, win_condition, 2, last_move)
            if winning_move:
                return winning_move

            blocking_move = find_winning_move(array, moves, size, win_condition, 1, last_move)
            if blocking_move:
                return blocking_move

            # Si aucun coup gagnant n'est trouvé, prioriser le blocage du joueur
            return blocking_move_for_player(array, moves, size, win_condition, last_move)


        def blocking_move_for_player(array, moves, size, win_condition, last_move):
            # Chercher une case où le joueur pourrait gagner et bloquer cette possibilité
            for move in moves:
                row, col = move
                if array[row][col] == 0:
                    array[row][col] = 1  # Simuler le coup du joueur
                    if find_winning_move(array, moves, size, win_condition, 1, last_move):
                        array[row][col] = 0  # Réinitialiser le coup
                        return row, col
                    array[row][col] = 0  # Réinitialiser le coup après la vérification

            # Si aucun coup gagnant du joueur n'est trouvé, jouer aléatoirement
            return get_random_move(moves)


        # Fonction pour trouver un coup gagnant
        def find_winning_move(array, moves, size, win_condition, symbol, last_move):
            for move in moves:
                row, col = move
                if array[row][col] == 0:
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
        


