clothes_stack = list(map(int, input().split()))
rack_capacity = int(input())
rack_counter = 0
sum_clothes = 0
for el in (clothes_stack.copy()):
    if len(clothes_stack) > 0:
        if sum_clothes < rack_capacity:
            clothes_stack.pop()
            sum_clothes += el
        elif sum_clothes == rack_capacity:
            rack_counter += 1
            sum_clothes = 0
        elif sum_clothes > rack_capacity:
            rack_counter += 1
    else:
        print(rack_counter)