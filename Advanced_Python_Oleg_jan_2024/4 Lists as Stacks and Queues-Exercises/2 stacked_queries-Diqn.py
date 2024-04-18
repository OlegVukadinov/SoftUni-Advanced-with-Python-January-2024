n = int(input())
numbers_stack = []

for _ in range(n):
    numbers_data = [int(x) for x in input().split()]
    command = numbers_data[0]

    if command == 1:
        numbers_stack.append(numbers_data[1])
    elif command == 2:
        if numbers_stack:
            numbers_stack.pop()
    elif command == 3:
        if numbers_stack:
            print(max(numbers_stack))
    elif command == 4:
        if numbers_stack:
            print(min(numbers_stack))

numbers_stack.reverse()
print(*numbers_stack, sep= ", ")