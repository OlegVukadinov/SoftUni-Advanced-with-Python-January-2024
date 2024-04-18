from collections import deque

quantity_of_food = int(input())

orders = deque([int(x) for x in input().split()])    # [map(int, input().split())])

print(max(orders))

while orders:
    current_order = orders.popleft()
    if current_order <= quantity_of_food:
       quantity_of_food -= current_order
    else:
        print(f"Orders left:",current_order, *orders)
        break
else:
    print("Orders complete")

