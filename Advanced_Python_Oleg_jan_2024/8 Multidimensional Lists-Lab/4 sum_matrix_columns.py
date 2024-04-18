number_of_rows, number_of_columns = map(int, input().split(', '))

matrix = []

for row in range(number_of_rows):
    row_data = list(map(int,input().split(' ')))
    matrix.append(row_data)

rows = len(matrix)
cols = len(matrix[0])
sum_of_columns = []

for i in range(cols):
    col_sum = 0
    for j in range(rows):
        col_sum += matrix[j][i]

    sum_of_columns.append(col_sum)

print(*sum_of_columns, sep="\n")  # or for el in sum_of_columns:
                                  # print(el):