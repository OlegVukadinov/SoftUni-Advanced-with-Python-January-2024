def is_inside(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True

def calculate_cell_value(matrix, row, col, size):
    bombs_count = 0

    if is_inside(row - 1, col, size):
        if matrix[row - 1][col] == "*":
            bombs_count += 1
    if is_inside(row + 1, col, size):
        if matrix[row + 1][col] == '*':
            bombs_count += 1
    if is_inside(row, col - 1, size):
        if matrix[row][col - 1] == '*':
            bombs_count += 1
    if is_inside(row, col + 1, size):
        if matrix[row][col + 1] == '*':
            bombs_count += 1
    if is_inside(row - 1, col + 1, size):
        if matrix[row - 1][col + 1] == '*':
            bombs_count += 1
    if is_inside(row + 1, col + 1, size):
        if matrix[row + 1][col + 1] == '*':
            bombs_count += 1
    if is_inside(row - 1, col - 1, size):
        if matrix[row - 1][col - 1] == '*':
            bombs_count += 1
    if is_inside(row + 1, col - 1, size):
        if matrix[row + 1][col - 1] == '*':
            bombs_count += 1
    return bombs_count


size = int(input())
bombs = int(input())

matrix = [[0 for j in range(size)] for i in range(size)]

for bomb in range(bombs):
    bomb_pos_row, bomb_pos_col = map(lambda x: int(x), input()[1:][:-1].split(', '))
    matrix[bomb_pos_row][bomb_pos_col] = "*"

for row in range(size):
    for col in range(size):
        element = matrix[row][col]
        if element == '*':
            continue
        else:
            matrix[row][col] = calculate_cell_value(matrix, row, col, size)
for row in matrix:
    print(*row, sep=' ')