from collections import deque

expression = input().split()
numbers = deque()
 #expression = [int(x) for x in expression if x.isdigit()]
for el in expression:
    if el not in '+-*/':
        numbers.append(int(el))
    else:
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()
            if el  == '+':
                numbers.appendleft(first_num + second_num)
            elif el  == '-':
                numbers.appendleft(first_num - second_num)
            elif el == '*':
                numbers.appendleft(first_num * second_num)
            elif el == '/':
                numbers.appendleft(first_num // second_num)

print(*numbers)