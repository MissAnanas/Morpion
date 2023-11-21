import random

def afficher_grille(grille):
    for ligne in grille:
        print("|".join(ligne))
        print("-----")

def grille_vide():
    return [[" " for _ in range(3)] for _ in range(3)]

def coup_valide(grille, ligne, colonne):
    return grille[ligne][colonne] == " "

def coup_joueur(grille):
    while True:
        try:
            ligne = int(input("Choisissez la ligne (0, 1, 2) : "))
            colonne = int(input("Choisissez la colonne (0, 1, 2) : "))
            if coup_valide(grille, ligne, colonne):
                return ligne, colonne
            else:
                print("Cette case est déjà occupée. Essayez encore.")
        except ValueError:
            print("Entrez des nombres valides.")

def coup_IA(grille):
    meilleur_score = float("-inf")
    meilleur_coup = None
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                grille[i][j] = "O"
                score = minimax(grille, False)
                grille[i][j] = " "
                if score > meilleur_score:
                    meilleur_score = score
                    meilleur_coup = (i, j)
    return meilleur_coup

def minimax(grille, est_maximiseur):
    if verifier_victoire(grille, "O"):
        return 1
    elif verifier_victoire(grille, "X"):
        return -1
    elif est_match_nul(grille):
        return 0
    
    if est_maximiseur:
        meilleur_score = float("-inf")
        for i in range(3):
            for j in range(3):
                if grille[i][j] == " ":
                    grille[i][j] = "O"
                    score = minimax(grille, False)
                    grille[i][j] = " "
                    meilleur_score = max(meilleur_score, score)
        return meilleur_score
    else:
        meilleur_score = float("inf")
        for i in range(3):
            for j in range(3):
                if grille[i][j] == " ":
                    grille[i][j] = "X"
                    score = minimax(grille, True)
                    grille[i][j] = " "
                    meilleur_score = min(meilleur_score, score)
        return meilleur_score

def verifier_victoire(grille, symbole):
    lignes = ["".join(grille[i]) for i in range(3)]
    colonnes = ["".join([grille[i][j] for i in range(3)]) for j in range(3)]
    diagonales = ["".join([grille[i][i] for i in range(3)]), "".join([grille[i][2 - i] for i in range(3)])]
    lignes_colonnes_diagonales = lignes + colonnes + diagonales
    return any([symbole * 3 in ligne for ligne in lignes_colonnes_diagonales])

def est_match_nul(grille):
    return all([case != " " for ligne in grille for case in ligne])

def jouer_morpion():
    grille = grille_vide()
    tour = 0
    joueur_actuel = "X"
    afficher_grille(grille)
    
    while True:
        if joueur_actuel == "X":
            ligne, colonne = coup_joueur(grille)
        else:
            ligne, colonne = coup_IA(grille)
        grille[ligne][colonne] = joueur_actuel
        afficher_grille(grille)
        if verifier_victoire(grille, joueur_actuel):
            print(f"Le joueur {joueur_actuel} a gagné !")
            break
        elif est_match_nul(grille):
            print("Match nul !")
            break
        
        tour += 1
        joueur_actuel = "X" if tour % 2 == 0 else "O"

jouer_morpion()
