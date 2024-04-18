number_of_rows, number_of_columns = map(int, input().split(', '))

matrix = []

for row in range(number_of_rows):
    row_data = list(map(int,input().split(' ')))
    matrix.append(row_data)

for col_index in range(number_of_columns):
    col_sum = 0
    for row_index in range(number_of_rows):
        col_sum += matrix[row_index][col_index]

    print(col_sum)