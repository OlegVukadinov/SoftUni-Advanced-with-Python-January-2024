from collections import deque

quantity_of_food = int(input())

orders = deque([int(x) for x in input().split()])    # [map(int, input().split())])

print(max(orders))

while orders:
    order = orders.popleft()
    if order <= quantity_of_food:
        quantity_of_food -= order
    else:
        print(f"Orders left:", order, *orders)
        break
else:
    print("Orders complete")

