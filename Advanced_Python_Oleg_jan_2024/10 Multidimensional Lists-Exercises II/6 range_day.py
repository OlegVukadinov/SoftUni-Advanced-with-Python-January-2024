rows, cols = 5, 5

matrix = []
my_position = []
targets = 0
for row in range(5):
    data = input().split()
    matrix.append(data)
    for col in range(5):
        if matrix[row][col] == 'A':
            my_position = [row, col]
        elif matrix[row][col] == 'x':
            targets += 1

number_of_commands = int(input())
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
targets_down = []

for _ in range(number_of_commands):
    command = input().split()
    if command[0] == 'shoot':
        direction = command[1]
        r = my_position[0] + directions[direction][0]
        c = my_position[1] + directions[direction][1]
        while 0 <= r < 5 and 0 <= c < 5:
            if matrix[r][c] == 'x':
                matrix[r][c] = '.'
                targets -= 1
                targets_down.append([r, c])
                break
            r += directions[direction][0]
            c += directions[direction][1]
        if targets == 0:
            print(f"Training completed! All {len(targets_down)} targets hit.")
            break
    elif command[0] == "move":
        direction = command[1]
        steps = int(command[2])
        if direction == "up":
            r = my_position[0] - steps
            c = my_position[1]
        elif direction == "down":
            r = my_position[0] + steps
            c = my_position[1]
        elif direction == "left":
            r = my_position[0]
            c = my_position[1] - steps
        elif direction == "right":
            r = my_position[0]
            c = my_position[1] + steps
        if 0 <= r < 5 and 0 <= c < 5 and matrix[r][c] == ".":
            matrix[r][c] = "A"
            matrix[my_position[0]][my_position[1]] = '.'
            my_position = [r, c]
if targets > 0:
    print(f"Training not completed! {targets} targets left.")

for row in targets_down:
    print(row)