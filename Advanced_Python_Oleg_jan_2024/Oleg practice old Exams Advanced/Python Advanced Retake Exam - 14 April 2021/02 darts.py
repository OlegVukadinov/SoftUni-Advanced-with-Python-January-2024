current_player, next_player = input().split(', ')
size = 7
matrix = []

scores = {player: {'trows': 0, 'pts': 501} for player in (current_player, next_player)}


for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

while True:

    row, col = eval(input())
    scores[current_player]['trows'] += 1
    result = 0

    if min(row, col) >= 0 and max(row, col) < 7:
        value = matrix[row][col]
        if value.isnumeric():
            result = int(value)
        elif value == 'D':
            result = 2 * (int(matrix[0][col]) + int(matrix[6][col]) + int(matrix[row][0]) + int(matrix[row][6]))
        elif value == 'T':
            result = 3 * (int(matrix[0][col]) + int(matrix[6][col]) + int(matrix[row][0]) + int(matrix[row][6]))
        elif value == 'B':
            break

    scores[current_player]['pts'] -= result
    if scores[current_player].get('pts') <= 0:
        break
    current_player, next_player = next_player, current_player


winning_trows = scores[current_player].get('trows')
print(f'{current_player} won the game with {winning_trows} throws!')