rows, cols = list(map(int, input().split()))

matrix = []
equal_blocks = 0

for _ in range(rows):
    data = input().split()
    matrix.append(data)

for row in range(rows - 1):
    for col in range(cols - 1):
        symbol = matrix[row][col]

        if symbol == matrix[row + 1][col] and symbol == matrix[row][col + 1] and symbol == matrix[row + 1][col + 1]:
            equal_blocks += 1

print(equal_blocks)