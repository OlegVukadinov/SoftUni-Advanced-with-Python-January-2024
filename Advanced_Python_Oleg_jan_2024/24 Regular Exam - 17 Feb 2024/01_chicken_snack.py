from collections import deque

amount_money = deque(map(int, input().split()))
prices_foods  = deque(map(int, input().split()))

food_counter = 0
while amount_money and prices_foods:

    if amount_money[-1] == prices_foods[0]:
        food_counter += 1
        amount_money.pop()
        prices_foods.popleft()
    elif amount_money[-1] > prices_foods[0]:
        difference = amount_money[-1] - prices_foods[0]
        food_counter += 1
        amount_money.pop()
        amount_money[-1] = amount_money[-1] + difference # da se proveri
        prices_foods.popleft()
    elif amount_money[-1] < prices_foods[0]:
        amount_money.pop()
        prices_foods.popleft()

if food_counter == 0:
   print("Henry remained hungry. He will try next weekend again.")
elif food_counter == 1:
    print(f"Henry ate: {food_counter} food.")
elif food_counter >= 4:
   print(F"Gluttony of the day! Henry ate {food_counter} foods.")
else:
    print(f"Henry ate: {food_counter} foods.")

