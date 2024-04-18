number_of_rows = int(input())
matrix = []

for i in range(number_of_rows):
    data = [int(element) for element in input().split(", ")]
    matrix.append(data)

even_matrix = []

for row in matrix:
    sub_list = []
    for el in row:
        if el % 2 == 0:
            sub_list.append(el)
    even_matrix.append(sub_list)

print(even_matrix)
