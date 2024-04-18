def is_valid(number, size):
    return 0 <= number < size


n = int(input())

snake_pos = []
b_positions = []
food_sum = 0
directions = {'up': (-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}
matrix = []

for row in range(n):
    line = list(input())
    if 'S' in line:
        snake_pos = [row, line.index('S')]
    if 'B' in line:
        b_positions.append([row, line.index('B')])
    matrix.append(line)


if b_positions:
    first_b_pos, second_b_pos = b_positions


while True:
    direction = input()
    row_changes = directions[direction][0]
    col_changes = directions[direction][1]
    row = snake_pos[0]
    col = snake_pos[1]

    if not is_valid(row + row_changes, n) or not is_valid(col + col_changes, n):
        matrix[snake_pos[0]][snake_pos[1]] = '.'
        print('Game over!')
        print(f'Food eaten: {food_sum}')
        for row_mx in matrix:
            print(''.join(row_mx))
        break
    row += row_changes
    col += col_changes
    matrix[snake_pos[0]][snake_pos[1]] = '.'
    snake_pos[0] = row
    snake_pos[1] = col
    if matrix[snake_pos[0]][snake_pos[1]] == 'B':
        if snake_pos == first_b_pos:
            matrix[first_b_pos[0]][first_b_pos[1]] = '.'
            matrix[second_b_pos[0]][second_b_pos[1]] = 'S'
            snake_pos = second_b_pos
        else:
            matrix[second_b_pos[0]][second_b_pos[1]] = '.'
            matrix[first_b_pos[0]][first_b_pos[1]] = 'S'
            snake_pos = first_b_pos


    elif matrix[snake_pos[0]][snake_pos[1]] == '*':
        food_sum += 1
        matrix[snake_pos[0]][snake_pos[1]] = 'S'
        if food_sum >= 10:
            print('You won! You fed the snake.')
            print(f'Food eaten: {food_sum}')
            for row_mx in matrix:
                print(''.join(row_mx))
            break