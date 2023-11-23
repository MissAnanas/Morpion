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
    #os.system("cls")
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

# Fonction pour effectuer un coup du joueur
def make_player_move(player):
    while True:
        try:
            choice = ask_int(f"Joueur {player}, choisissez un coup parmi les cases disponibles : ", 1, len(moves))

            array_index = moves[choice - 1]
            if array[array_index[0]][array_index[1]] == 0:
                moves.remove(array_index)
                row, col = array_index

                array[row][col] = player
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
    
        print("Cases disponibles :", moves)
        
        del moves[random_index]

        print("Cases disponibles :", moves)

        return array_index
    else:
        return None

# Lancer le jeu
play_tic_tac_toe()
