# numbers = list(map(int, input().split(", ")))
# n = int(input())
# for _ in range(n):
#     index = int(input())
#     if 0 <= index < len(numbers) or (index <= -1 and index >= - len(numbers):
#         print(numbers[index])

text = input()

try:
    times = int(input())
    print(text*times)
except ValueError:
        print("Variable times must be an integer")
