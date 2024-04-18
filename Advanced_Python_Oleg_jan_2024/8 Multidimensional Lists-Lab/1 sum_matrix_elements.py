number_of_rows, number_of_columns = map(int, input().split(', '))
matrix = []

for row in range(number_of_rows):
    row_data = list(map(int,input().split(', ')))
    matrix.append(row_data)
matrix_element_sum = 0 # s komprehenshion no trqbva da mahnem dolniqt For loop
                         # matrix_element_sum = sum([sum(current_el) for current_el in matrix])

for index in range(len(matrix)):
    current_row = matrix[index]
    matrix_element_sum += sum(current_row)

print(matrix_element_sum)
print(matrix)