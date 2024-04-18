n = int(input())
stack = []

for i in range(1, n + 1):
    query = input().split()
    if len(query) == 2:
        command = int(query[0])
        number = int(query[1])
        if command == 1:
            stack.append(number)

    elif len(query) == 1:
        command = int(query[0])
        if command == 2:
            if len(stack) > 0:
                stack.pop()
        elif command == 3:
            if len(stack) > 0:
                print(max(stack))
        elif command == 4:
            if len(stack) > 0:
                print(min(stack))
stack.reverse()
print(*stack,sep=", ")
