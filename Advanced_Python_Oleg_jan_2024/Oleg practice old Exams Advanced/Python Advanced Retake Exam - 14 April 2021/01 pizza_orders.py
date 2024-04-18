from collections import deque

pizza_orders = deque([int(x) for x in input().split(', ')])
employees_capacity = deque([int(x) for x in input().split(', ')])
total_pizza_count = 0

while True:

    if not employees_capacity or not pizza_orders:
        break
    current_order = pizza_orders.popleft()
    if current_order > 10 or current_order <= 0:
        continue

    capacity = employees_capacity.pop()

    if capacity >= current_order:
        total_pizza_count += current_order
    elif capacity < current_order:
        rest_orders = current_order - capacity
        pizza_orders.appendleft(rest_orders)
        total_pizza_count += capacity

if employees_capacity:
    print(f"All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza_count}")
    print(f"Employees: {', '.join(str(x) for x in employees_capacity)}")
else:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")