import random 
import os

# Création d'un tableau 2D pour représenter le morpion
array = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

# Liste pour stocker les coups
moves = [ 
    [0,0],  [0,1], [0,2],    
    [1,0],  [1,1], [1,2],
    [2,0],  [2,1], [2,2],
]

played_moves = []  # Liste pour stocker les coups joués

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

# Fonction pour vérifier si un joueur a gagné ou s'il y a égalité
def check_game_result(player):
    # Vérifier les lignes, colonnes et diagonales
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

# Fonction pour demander un entier à l'utilisateur dans une plage donnée
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

def ask_coordinates(message: str) -> tuple[int, int]:
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

            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Veuillez entrer des chiffres entre 0 et 2.")
        except ValueError as e:
            print(f"Entrée invalide : {e}")



# Fonction pour effectuer un coup du joueur
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
            random_move = get_random_move()
            if random_move:  # Vérifie s'il y a des coups disponibles dans la liste moves
                row, col = random_move
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
def get_random_move():
    if moves:
        random_index = random.randint(0, len(moves) - 1)
        array_index = moves[random_index]
        del moves[random_index]
        return array_index
    else:
        return None

# Lancer le jeu
play_tic_tac_toe()
