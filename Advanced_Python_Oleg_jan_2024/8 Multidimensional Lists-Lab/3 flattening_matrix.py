number_of_rows = int(input())
matrix = []

for row in range(number_of_rows):
    curr_row = list(map(int, input().split(", ")))
    for el in curr_row:
        matrix.append(el)

print(matrix)
