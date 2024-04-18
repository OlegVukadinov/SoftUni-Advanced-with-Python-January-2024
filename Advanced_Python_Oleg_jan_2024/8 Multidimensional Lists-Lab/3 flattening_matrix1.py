number_of_rows = int(input())
matrix = []

for i in range(number_of_rows):
    curr_row = list(map(int, input().split(", ")))
    matrix.append(curr_row)

flattern = []

for row in matrix:
    for el in row:
        flattern.append(el)

print(flattern)
