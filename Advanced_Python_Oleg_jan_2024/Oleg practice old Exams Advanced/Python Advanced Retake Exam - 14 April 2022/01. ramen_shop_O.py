from collections import deque

bowls_ramen = deque(map(int, input().split(", ")))
customers = deque(map(int, input().split(", ")))


while bowls_ramen and customers:
    if bowls_ramen[-1] == customers[0]:
        bowls_ramen.pop()
        customers.popleft()
    elif bowls_ramen[-1] > customers[0]:
        bowls_ramen[-1] = bowls_ramen[-1] - customers[0]
        customers.popleft()
    elif bowls_ramen[-1] < customers[0]:
        customers[0] = customers[0] - bowls_ramen[-1]
        bowls_ramen.pop()

if not customers:
    print("Great job! You served all the customers.")
    if bowls_ramen:
        print(f"Bowls of ramen left: {', '.join(map(str, bowls_ramen))}")
elif not bowls_ramen:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join(map(str, customers))}")
