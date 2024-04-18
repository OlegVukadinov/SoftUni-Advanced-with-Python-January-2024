from collections import deque

quantity_of_food = int(input())

orders = deque([int(x) for x in input().split()])    # [map(int, input().split())])

print(max(orders))

for current_order in orders.copy():
    if current_order <= quantity_of_food:
        orders.popleft()
        quantity_of_food -= current_order
    else:
        print(f"Orders left:", *orders)
        break
else:
    print("Orders complete")

