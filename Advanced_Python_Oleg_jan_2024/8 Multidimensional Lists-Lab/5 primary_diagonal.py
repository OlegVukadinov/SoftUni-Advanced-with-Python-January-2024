num_of_rows = int(input())

matrix = []

for row in range(num_of_rows):
    row_data = list(map(int,input().split(' ')))
    matrix.append(row_data)
# za drugia diagonal  for i in range(len(matrix -1, -1, -1):
                        # diag_sum += matrix[i][(len(matrix) - 1) - 1

diag_sum = [matrix[i][i] for i in range(len(matrix))]
print(sum(diag_sum))


