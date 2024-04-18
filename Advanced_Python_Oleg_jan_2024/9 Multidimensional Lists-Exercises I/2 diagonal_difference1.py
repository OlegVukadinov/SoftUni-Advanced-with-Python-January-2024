num = int(input())
matrix = []

for _ in range(num):
    data = list(map(int, input().split()))
    matrix.append(data)

primary_sum, secondary_sum = 0, 0

for i in range(num):
    primary_sum += matrix[i][i]
    secondary_sum += matrix[i][num - i - 1]

print(abs(primary_sum - secondary_sum))