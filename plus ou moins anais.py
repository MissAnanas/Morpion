import random
moves = int(input("Choisissez le nombre de coup: "))
min_value = int(input("Choisissez une borne minimale (min 0): "))
max_value = int(input("Choisissez une borne maximale (max 100): "))
nb_secret = random.randint(min_value, max_value)

number = input(f"Choisissez un nouveau nombre")

def ask_int(number):
    if number != int(number):
        print("Erreur, veuillez entrer un nombre entier")

ask_int(number)




def game(moves, nb_secret):
    while moves > 0 :
        number = int(input(f"Choisissez un nouveau nombre entre {min_value} et {max_value}:"))
        moves -= 1
        if number < nb_secret:
            print("Plus !")
        if number == nb_secret:
            print("Gagné!")
            break
        if number > nb_secret:
            print("Moins !")   
        if moves == 0:
            print("Plus de coup!")

game(moves, nb_secret)
    



