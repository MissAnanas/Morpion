#i: int = 5


# array: list = \
 #   [
  #      [0, 0, 0],
 #       [0, 0, 0],
 #       [0, 0, 0],
  #  ]

# array = [0, 0, 0,  0, 0, 0,  0, 0, 0]

import random

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
    print("---------------------☺---------------------")
    for i, row in enumerate(array):
        print(" | ".join(map(lambda cell: symbols[cell], row)))
        print("-" * 9)
    print()
    print("---------------------☺---------------------")

# Fonction pour vérifier si un joueur a gagné
def check_winner(player):
    # Vérifier les lignes, les colonnes et les diagonales
    return any(all(cell == player for cell in row) for row in array) or \
           any(all(row[i] == player for row in array) for i in range(3)) or \
           all(array[i][i] == player for i in range(3)) or \
           all(array[i][2 - i] == player for i in range(3))

# Fonction pour effectuer un coup aléatoire
def make_random_move():
    empty_cells = [(i, j) for i in range(3) for j in range(3) if array[i][j] == 0]
    if empty_cells:
        return random.choice(empty_cells)
    else:
        return None

# Fonction pour trouver la ligne, la colonne ou la diagonale gagnante
def find_winning_line(player):
    # Vérifier les lignes
    for i, row in enumerate(array):
        if all(cell == player for cell in row):
            return [('row', i)]

    # Vérifier les colonnes
    for j in range(3):
        if all(array[i][j] == player for i in range(3)):
            return [('column', j)]

    # Vérifier la diagonale principale
    if all(array[i][i] == player for i in range(3)):
        return [('diagonal', 'main')]

    # Vérifier la diagonale inverse
    if all(array[i][2 - i] == player for i in range(3)):
        return [('diagonal', 'inverse')]

    return []

# Fonction pour marquer la ligne, la colonne ou la diagonale gagnante
def mark_winning_line(winning_line):
    if not winning_line:
        return

    line_type, line_index = winning_line[0] if len(winning_line) > 0 else None, winning_line[1] if len(winning_line) > 1 else None

    if line_type == 'row':
        for j in range(3):
            array[line_index][j] = -1
    elif line_type == 'column':
        for i in range(3):
            array[i][line_index] = -1
    elif line_type == 'diagonal':
        if line_index == 'main':
            for i in range(3):
                array[i][i] = -1
        elif line_index == 'inverse':
            for i in range(3):
                array[i][2 - i] = -1


# Fonction principale pour jouer au morpion
def play_tic_tac_toe():
    player = 1

    while True:
        display_board()

        # Tour du joueur
        if player == 1:
            try:
                row, col = map(int, input("Joueur 1, vous êtes les X, choisissez la ligne et la colonne (séparées par un espace) : ").split())

                # Vérifier si le coup est valide et effectuer le coup
                if 0 <= row < 3 and 0 <= col < 3 and array[row][col] == 0:
                    array[row][col] = player

                    # Vérifier si le joueur a gagné
                    if check_winner(player):
                        winning_line = find_winning_line(player)
                        mark_winning_line(winning_line)
                        display_board()
                        print(f"Joueur {player} a gagné ! Félicitations!")
                        break
                    # Vérifier s'il y a égalité
                    elif all(array[i][j] != 0 for i in range(3) for j in range(3)):
                        display_board()
                        print("La partie est terminée. Match nul!")
                        break
                    # Passer au tour suivant
                    else:
                        player = 3 - player  # Alterner entre les joueurs 1 et 2
                else:
                    print("Coup invalide. Choisissez une autre case.")
            except ValueError:
                print("Entrées invalides. Veuillez saisir des nombres entiers.")
        # Tour de l'IA
        else:
            move = make_random_move()
            if move:
                row, col = move
                array[row][col] = player

                # Vérifier si l'IA a gagné
                if check_winner(player):
                    winning_line = find_winning_line(player)
                    mark_winning_line(winning_line)
                    display_board()
                    print(f"Joueur {player} (IA) a gagné !")
                    break
                # Vérifier s'il y a égalité
                elif all(array[i][j] != 0 for i in range(3) for j in range(3)):
                    display_board()
                    print("La partie est terminée. Match nul!")
                    break
                # Passer au tour suivant
                else:
                    player = 3 - player  # Alterner entre les joueurs 1 et 2

# Lancer le jeu
play_tic_tac_toe()
