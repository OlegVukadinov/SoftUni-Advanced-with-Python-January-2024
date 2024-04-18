def movement_func(matrix_data):
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }

    my_pos = []
    jet_armor = 300
    enemy = 4

    for row in range(len(matrix_data)):
        for col in range(len(matrix_data)):
            if matrix_data[row][col] == 'J':
                my_pos = [row, col]
                matrix_data[row][col] = '-'

    while enemy:

        if jet_armor <= 0:
            print(f"Mission failed, your jetfighter was shot down! Last coordinates [{my_pos[0]}, {my_pos[1]}]!")
            break
        direction = input()
        my_pos_row = my_pos[0] + directions[direction][0]
        my_pos_col = my_pos[1] + directions[direction][1]

        if not (0 <= my_pos_row < len(matrix_data) and 0 <= my_pos_col < len(matrix_data)):
            continue
        elif matrix_data[my_pos_row][my_pos_col] == '-':
            my_pos = [my_pos_row, my_pos_col]
            continue

        if matrix_data[my_pos_row][my_pos_col] == 'E':
            jet_armor -= 100
            enemy -= 1
            my_pos = [my_pos_row, my_pos_col]
            matrix_data[my_pos_row][my_pos_col] = "-"
        elif matrix_data[my_pos_row][my_pos_col] == 'R':
            jet_armor = 300
            my_pos = [my_pos_row, my_pos_col]
            matrix_data[my_pos_row][my_pos_col] = "-"

    matrix_data[my_pos[0]][my_pos[1]] = 'J'
    if not enemy:
        print("Mission accomplished, you neutralized the aerial threat!")

    print(*[''.join(row) for row in matrix_data], sep='\n')

def matrix_func():
    size = int(input())
    curr_matrix = []
    for row in range(size):
        row_data = list(input())
        curr_matrix.append(row_data)

    return curr_matrix


matrix = matrix_func()
movement_func(matrix)
