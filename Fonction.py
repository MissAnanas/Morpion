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