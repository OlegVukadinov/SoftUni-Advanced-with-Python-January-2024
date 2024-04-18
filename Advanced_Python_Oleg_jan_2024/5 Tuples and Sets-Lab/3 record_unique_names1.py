n = int(input())

my_list = []

for _ in range(n):
    name = input()
    if name not in my_list:
        my_list.append(name)

for el in my_list:
    print(el)
