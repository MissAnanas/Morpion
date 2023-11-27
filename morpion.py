import random
import os
from Fonction import *

def create_board(size):
    return [[0 for _ in range(size)] for _ in range(size)]

def main():
    print("---------------------☺---------------------")
    print("Bienvenue sur ce jeu du Morpion !")
    
    reponse = input("Souhaitez-vous consulter les règles (Y/N) ? ")
    if reponse.upper() == "Y":
        # Affichage les règles du jeu
        print("---------------------☺---------------------")
        print("Règles :")
        print("- Le but du jeu est de vaincre l'ordinateur. - ")
        print("------> - La partie se joue sur plusieurs manches !")
        print("------> - Vous avez l'un après l'autre le choix d'une case du tableau ou vous placerez un symbole (X ou O)")
        print("------> - Pour gagner il vous faudra aligner 3 symboles consécutifs (ou plus selon votre choix) en premier (verticale, horizontale ou diagonale)")
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

    def check_game_result(array, symbol, size, win_condition):
        for row in array:
            if any(sum(1 for cell in row[i:i + win_condition] if cell == symbol) == win_condition for i in range(size - win_condition + 1)):
                return True, f"Joueur {symbol} a gagné ! Félicitations!"

        for i in range(size):
            col = [array[j][i] for j in range(size)]
            if any(sum(1 for cell in col[i:i + win_condition] if cell == symbol) == win_condition for i in range(size - win_condition + 1)):
                return True, f"Joueur {symbol} a gagné ! Félicitations!"

        if any(sum(1 for cell in array[i][i:i + win_condition] if cell == symbol) == win_condition for i in range(size - win_condition + 1)):
            return True, f"Joueur {symbol} a gagné ! Félicitations!"

        if any(sum(1 for cell in array[i][size - i - win_condition:size - i] if cell == symbol) == win_condition for i in range(size - win_condition + 1)):
            return True, f"Joueur {symbol} a gagné ! Félicitations!"

        if all(array[i][j] != 0 for i in range(size) for j in range(size)):
            return True, "La partie est terminée. Match nul!"

        return False, ""

    def ask_coordinates(message: str, size) -> tuple[int, int]:
        while True:
            try:
                user_input = input(message)
                if ',' in user_input:
                    coords = user_input.replace(',', ' ').split()
                else:
                    if len(user_input) == 2:
                        coords = [user_input[0], user_input[1]]
                    else:
                        coords = user_input.split()

                if len(coords) != 2:
                    raise ValueError("Veuillez entrer deux chiffres.")

                row = int(coords[0])
                col = int(coords[1])

                if 0 <= row <= size - 1 and 0 <= col <= size - 1:
                    return row, col
                else:
                    print(f"Veuillez entrer des chiffres entre 0 et {size - 1}.")
            except ValueError as e:
                print(f"Entrée invalide : {e}")

    def make_player_move(array, symbol, moves, played_moves, size, win_condition):
        while True:
            print("Cases disponibles :", moves)
            row, col = ask_coordinates(f"Joueur {symbol}, choisissez la case : ", size)
            if array[row][col] == 0:
                array[row][col] = symbol
                moves.remove([row, col])
                played_moves.append((row, col))
                result, message = check_game_result(array, symbol, size, win_condition)
                display_board(array, size)
                print(message)
                return result
            print("Coup invalide. Choisissez une autre case.")


    def get_random_move(moves):
        if moves:
            random_index = random.randint(0, len(moves) - 1)
            array_index = moves.pop(random_index)  
            return array_index
        else:
            return None

    def get_ai_move(array, moves, size, win_condition):
        # Recherche d'une victoire possible pour l'IA
        winning_move = find_winning_move(array, moves, size, win_condition, 2, [])
        if winning_move:
            return winning_move

        # Recherche d'une victoire possible pour le joueur pour bloquer
        blocking_move = find_winning_move(array, moves, size, win_condition, 1, [])
        if blocking_move:
            return blocking_move

        return get_random_move(moves) 



    # Fonction pour trouver un coup gagnant
    def find_winning_move(array, moves, size, win_condition, symbol, played_moves):
        for move in moves:
            row, col = move
            array[row][col] = symbol  # Simuler le coup du joueur ou de l'IA
            if check_game_result(array, symbol, size, win_condition)[0]:
                array[row][col] = 0  # Réinitialiser le coup
                played_moves.append((row, col))
                return move
            array[row][col] = 0  # Réinitialiser le coup après la vérification
        return None

    def play_tic_tac_toe():
        symbol = 1
        array = initialize_game()
        size = len(array)
        moves = [[i, j] for i in range(size) for j in range(size)]
        played_moves = []
        win_condition = ask_win_condition(size)

        while True:
            display_board(array, size)

            if symbol == 1:
                if make_player_move(array, symbol, moves, played_moves, size, win_condition):
                    break
                symbol = 3 - symbol
            else:
                ai_move = get_ai_move(array, moves, size, win_condition)
                if ai_move:
                    row, col = ai_move
                    array[row][col] = symbol
                    played_moves.append((row, col))
                    result, message = check_game_result(array, symbol, size, win_condition)
                    display_board(array, size)
                    print(message)
                    if result:
                        break
                    else:
                        symbol = 3 - symbol

    # Lancer le jeu
    play_tic_tac_toe()

    reponse = print("---------------------☺---------------------")
    reponse = input("Souhaitez-vous relancer une partie (Y/N) ?")
    if reponse.upper() != "Y":
        print("---------------------☺---------------------")
        print("Merci d'avoir joué ! A bientôt :)")
        print("---------------------☺---------------------")

main()