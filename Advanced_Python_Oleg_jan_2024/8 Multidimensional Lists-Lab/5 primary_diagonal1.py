num_of_rows = int(input())

matrix = []

for row in range(num_of_rows):
    row_data = list(map(int,input().split(' ')))
    matrix.append(row_data)

diag_sum = 0
for row_index in range(num_of_rows):
    for col_index in range(num_of_rows):
        if row_index == col_index:
            diag_sum += matrix[row_index][col_index]

print(diag_sum)


