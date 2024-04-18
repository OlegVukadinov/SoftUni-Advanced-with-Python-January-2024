# def read_matrix_func()     - Ако искаме с фуункция махаме #

number_of_rows, number_of_columns = map(int, input().split(', '))
current_matrix = []

for row in range(number_of_rows):
    row_data = list(map(int,input().split(', ')))
    current_matrix.append(row_data)

# return current_matrix

# matrix = read_matrix_func()
print(current_matrix)

# print(matrix)



