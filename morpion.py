import random
import os

# Création d'un tableau 2D pour représenter le morpion
array = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

# Dictionnaire pour associer les valeurs du tableau à des symboles
symbols = {0: " ", 1: "X", 2: "O"}

# Fonction pour afficher le tableau actuel du morpion
def display_board():
    os.system("cls")
    print("---------------------☺---------------------")
    for row in array:
        print(" | ".join(map(lambda cell: symbols[cell], row)))
        print("-" * 9)
    print("---------------------☺---------------------")

def check_game_result(player):
    # Vérifier si un joueur a gagné
    for row in array:
        if all(cell == player for cell in row):
            return True, f"Joueur {player} a gagné ! Félicitations!"

    for i in range(3):
        if all(row[i] == player for row in array):
            return True, f"Joueur {player} a gagné ! Félicitations!"

    if all(array[i][i] == player for i in range(3)) or all(array[i][2 - i] == player for i in range(3)):
        return True, f"Joueur {player} a gagné ! Félicitations!"

    # Vérifier s'il y a égalité
    if all(array[i][j] != 0 for i in range(3) for j in range(3)):
        return True, "La partie est terminée. Match nul!"

    return False, ""

def ask_int(message: str, min_val: int, max_val: int) -> int:
    while True:
        try:
            user_input = int(input(message))
            if min_val <= user_input <= max_val:
                return user_input
            else:
                print(f"Veuillez entrer un nombre entre {min_val} et {max_val}.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

# Liste pour stocker les coups
moves = [
    [0, 0], [0, 1], [0, 2],
    [1, 0], [1, 1], [1, 2],
    [2, 0], [2, 1], [2, 2],
]

played_moves = []  # Liste pour stocker les coups joués

def make_player_move(player):
    while True:
        try:
            # Créer une nouvelle liste de mouvements disponibles pour ce tour
            current_moves = moves.copy()
            print("Cases disponibles :", current_moves)
            row = ask_int(f"Joueur {player}, choisissez la ligne (1 à 3) : ", 1, 3)
            col = ask_int(f"Joueur {player}, choisissez la colonne (1 à 3) : ", 1, 3)

            row -= 1
            col -= 1

            array_index = [row, col]
            if array_index in current_moves:
                current_moves.remove(array_index)
                array[row][col] = player
                played_moves.append((row, col))
                result, message = check_game_result(player)

                display_board()
                print(message)

                if result:
                    return True
                else:
                    # Mettez à jour la liste globale des mouvements après chaque coup
                    moves.clear()
                    moves.extend(current_moves)
                    return False
            else:
                print("Coup invalide. Choisissez une autre case.")
        except ValueError:
            print("Entrées invalides. Veuillez saisir des nombres entiers.")



# Fonction principale pour jouer au morpion
def play_tic_tac_toe():
    player = 1

    while True:
        display_board()

        # Tour du joueur
        if player == 1:
            if make_player_move(player):
                break
            player = 3 - player  # Alterner entre les joueurs 1 et 2
        # Tour de l'IA
        else:
            move = make_random_move()
            if moves:  # Vérifie s'il y a des coups disponibles dans la liste moves
                move = random.choice(moves)  # Choix aléatoire parmi les coups disponibles
                moves.remove(move)  # Retirer le coup choisi de la liste des coups disponibles
                row, col = move
                array[row][col] = player
                played_moves.append((row, col)) 

                result, message = check_game_result(player)
                display_board()
                print(message)

                if result:
                    break
                else:
                    player = 3 - player  # Alterner entre les joueurs 1 et 2

# Fonction pour effectuer un coup aléatoire
def make_random_move():
    if moves:
        random_index = random.randint(0, len(moves) - 1)
        array_index = moves[random_index]
        moves.remove(array_index)
        return array_index
    else:
        return None

# Lancer le jeu
play_tic_tac_toe()

