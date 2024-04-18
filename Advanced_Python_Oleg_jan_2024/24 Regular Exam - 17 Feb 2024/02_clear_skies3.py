def nexts(cr, cc, mr, mc):
    nr = cr + mr
    nc = cc + mc
    return nr, nc

n = int(input())

my_pos = None
matrix = []
armor = 300
enemy = 4
for row in range(n):
    entry = list(input())
    matrix.append(entry)
    if "J" in entry:
        my_pos = [row, entry.index("J")]
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
while armor and enemy:
    command = input()
    cur_r, cur_c = my_pos
    move_r, move_c = directions[command]
    next_r, next_c = nexts(cur_r, cur_c, move_r, move_c)
    matrix[cur_r][cur_c] = "-"
    symbol = matrix[next_r][next_c]
    if symbol == "E":
        armor -= 100
        enemy -= 1
        matrix[next_r][next_c] = "J"
    elif symbol == "R":
        armor = 300
        matrix[next_r][next_c] = "J"
    my_pos = [next_r, next_c]
if enemy == 0:
    print("Mission accomplished, you neutralized the aerial threat!")
elif armor == 0:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{my_pos[0]}, {my_pos[1]}]!")
[print(*x, sep="") for x in matrix]
