from collections import deque

chocolate = deque(map(int,input().split(", ")))
milk_cups = deque(map(int,input().split(", ")))

shake_counter = 0

while chocolate and milk_cups and shake_counter < 5:
    if chocolate[-1] <= 0 and milk_cups[0] <= 0:
        chocolate.pop()
        milk_cups.popleft()
        continue
    if chocolate[-1] <= 0:
        chocolate.pop()
        continue
    if milk_cups[0] <= 0:
        milk_cups.popleft()
        continue
    if chocolate[-1] == milk_cups[0]:
        chocolate.pop()
        milk_cups.popleft()
        shake_counter += 1
    else:
        milk_cups.rotate(-1)
        chocolate[-1] -= 5

if shake_counter == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if len(chocolate) > 0:
    chocolate = [str(x) for x in chocolate]
    print(f'Chocolate: {", ".join(chocolate)}')
else:
    print("Chocolate: empty")

if len(milk_cups) > 0:
    milk_cups = [str(x) for x in milk_cups]
    print(f'Milk: {", ".join(milk_cups)}')
else:
    print("Milk: empty")

