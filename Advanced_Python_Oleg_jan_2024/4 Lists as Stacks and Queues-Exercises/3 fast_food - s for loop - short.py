my_list = list(map(int, input().split()))
max_num = 0
for el in my_list:
    if el > max_num:
        max_num = el
print(max_num)
