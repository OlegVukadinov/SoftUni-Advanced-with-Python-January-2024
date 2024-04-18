rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    command = input()
    if command == "END":
        break
    com = command.split()
    action = com[0]
    row = int(com[1])
    col = int(com[2])
    value = int(com[3])

    if not (0 <= row < rows and 0 <= col < rows):
        print("Invalid coordinates")
        continue
    if action == "Add":
        matrix[row][col] += value
    elif action == "Subtract":
        matrix[row][col] -= value

for row in matrix:
    print(*row, sep=' ')
