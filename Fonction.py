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



"""def getCustomGrid(i) -> tuple[list[list[int]], tuple[int, int], tuple[int, int] ] :
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
            return available_tiles"""