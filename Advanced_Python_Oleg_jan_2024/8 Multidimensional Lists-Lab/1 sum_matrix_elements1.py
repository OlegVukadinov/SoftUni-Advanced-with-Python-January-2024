number_of_rows, number_of_columns = map(int, input().split(', '))
matrix = []
matrix_element_sum = 0
for row in range(number_of_rows):
    row_data = list(map(int,input().split(', ')))
    matrix_element_sum += sum(row_data)
    matrix.append(row_data)

print(matrix_element_sum)
print(matrix)