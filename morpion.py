import random
import os
from Fonction import *

while True:

    def create_board(size: int) -> list[list[int]]:
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

        def initialize_game() -> list[list[int]]:
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

        def display_board(array: list[list[int]], size: int) -> None:
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

        def make_player_move(array: list[list[int]], symbol: int, moves: list[tuple[int]], size: int, win_condition: int) -> tuple[bool, tuple[int, int]]:
            while True:
                print("Cases disponibles :", moves)
                row, col = ask_coordinates(f"Joueur {symbol}, choisissez la case : ", size)
                if array[row][col] == 0:
                    array[row][col] = symbol
                    move = [row, col]
                    if move in moves:
                        moves.remove(move)
                    result, message = check_game_result(array, symbol, size, win_condition, (row, col))
                    display_board(array, size)
                    print(message)
                    if result:
                        return True, (row, col)
                    return False, (row, col)
                print("Coup invalide. Choisissez une autre case.")


        def get_random_move(moves: list[tuple[int]]) -> [list[int], None]:
            if moves:
                random_index = random.randint(0, len(moves) - 1)
                array_index = moves.pop(random_index)
                return array_index
            else:
                return None

        def get_ai_move(array: list[list[int]], moves: list[tuple[int]], size: int, win_condition: int) -> tuple[bool, tuple[int, int]]:
            # Recherche d'une victoire possible pour l'IA
            winning_move = find_winning_move(array, moves, size, win_condition, 1)
            if winning_move:
                return True, winning_move

            # Recherche d'une victoire possible pour le joueur pour bloquer
            blocking_move = find_winning_move(array, moves, size, win_condition, 2)
            if blocking_move:
                return True, blocking_move

            return False, get_random_move(moves)

        # Fonction pour trouver un coup gagnant
        def find_winning_move(array: list[list[int]], moves: list[tuple[int]], size: int, winning_symbol_count: int, symbol: int) -> tuple[bool, tuple[int, int]]:
            for move in moves:
                row, col = move
                array[row][col] = symbol  # Simuler le coup du joueur ou de l'IA
                if check_game_result(array, symbol, size, winning_symbol_count, move)[0]:
                    array[row][col] = 0  # Réinitialiser le coup
                    return True, move
                array[row][col] = 0  # Réinitialiser le coup après la vérification

            return False, get_random_move(moves)

        def getCustomGrid(i) -> tuple[list[list[int]], tuple[int, int], tuple[int, int] ] :
            custom_grid = \
                [
                    [
                        [1, 2, 0],
                        [1, 2, 0],
                        [0, 0, 0],
                    ], \
                    [
                        [1, 0, 0],
                        [0, 1, 0],
                        [0, 0, 0],
                    ],\
                    [
                        [1, 0, 2],
                        [0, 1, 2],
                        [0, 0, 0],
                    ],\
                    [
                        [1, 1, 0],
                        [0, 1, 0],
                        [0, 2, 2],
                    ],\
                    [
                        [1, 2, 0],
                        [0, 1, 0],
                        [0, 0, 2],
                    ],                  
                ]
            expected_results_win = \
                [
                    [2, 0],
                    [2, 2],
                    [2, 2],
                    [0, 2],
                    ["Random"]
                ]
            expected_results_block = \
                [
                    [2, 1],
                    [2, 2],
                    [2, 2],
                    [2, 0],
                    ["Random"]
                ]

            return custom_grid[i], expected_results_win[i], expected_results_block[i]
        
        def testGrid(i):
            array, expected_win_move, expected_block_move = getCustomGrid(i)
            size = len(array)
            moves = get_available_tile(array)
            # best_move: tuple[int, int] = find_winning_move(array, moves, size, 3, 1 )
            is_random_block, best_move_block = get_ai_move(array, moves, size, 3)
            is_random_win, best_move = find_winning_move(array, moves, size, 3, 1)
            print("Custom Grid:")
            for row in array:
                print(row)

            if expected_win_move == best_move:
                print("Win Success")
            elif expected_block_move == best_move_block[1]:
                print("Block Success")

            if is_random_block:
                print("Random Block Success -> move :", best_move_block[1])
            else:
                print("Error happened ! Expected move :",best_move_block[1])

            if is_random_win:
                print("Random Win Success -> move :", best_move)
            else:
                print("Error happened ! Expected move :",best_move)

            
        def get_available_tile(grid) -> list[list[int]]:
            available_tiles = []
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 0:
                        available_tiles.append((i, j))
            return available_tiles

        def play_tictactoe():
            symbol: int = 1
            array = initialize_game()
            size = len(array)
            moves = [[i, j] for i in range(size) for j in range(size)]
            win_condition = ask_win_condition(size)
            last_move: tuple[int, int] = None

            while True:
                display_board(array, size)
                print(last_move)

                if symbol == 1:
                    result, last_move = make_player_move(array, symbol, moves, size, win_condition)
                    if result:
                        break
                    symbol = 3 - symbol
                else:
                    if last_move is None:
                        print("Error")

                    is_random_move, ai_move = get_ai_move(array, moves, size, win_condition)
                    if ai_move:
                        row, col = ai_move
                        array[row][col] = symbol
                        last_move = (row, col)
                        result, message = check_game_result(array, symbol, size, win_condition, last_move)
                        display_board(array, size)
                        print(message)
                        print(ai_move)
                        if result:
                            break
                        else:
                            # Vérifier si le mouvement est présent dans la liste avant de le supprimer
                            if [row, col] in moves:
                                moves.remove([row, col])
                            symbol = 3 - symbol

        play_tictactoe()


        reponse = input("Souhaitez-vous tester des coups (Y/N) ? ")
        if reponse.upper() == "Y":
            array = initialize_game()
            play_tictactoe.moves = get_available_tile(array)
            testGrid(ask_int("Quelle grille voulez-vous tester ?", 0, 4))
            

    main()

    reponse = print("---------------------☺------------------")
    reponse = input("Souhaitez-vous relancer une partie (Y/N) ?")
    if reponse.upper() != "Y":
        print("---------------------☺---------------------")
        print("Merci d'avoir joué ! A bientôt :)")
        print("---------------------☺---------------------")
        break
