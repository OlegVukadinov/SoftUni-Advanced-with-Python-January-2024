n = int(input())

matrix = []

for _ in range(n):
    data = list(map(int, input().split(", ")))
    matrix.append(data)
primary_diagonal = []
second_diagonal = []

for row in range(n):
    primary_diagonal.append(matrix[row][row])

for row in range(n):
    second_diagonal.append(matrix[row][n - row - 1])

print(f"Primary diagonal: {', '.join(str(el) for el in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(el) for el in second_diagonal)}. Sum: {sum(second_diagonal)}")


