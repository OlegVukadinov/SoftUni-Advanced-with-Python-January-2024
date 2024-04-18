n = int(input())

car_info = set()

for _ in range(n):
    direction, car_number = input().split(", ")
    if direction == "IN":
        car_info.add(car_number)
    elif direction == "OUT":
        if car_number in car_info:
            car_info.remove(car_number)

if len(car_info) == 0:
    print("Parking Lot is Empty")
elif len(car_info) > 0:
    for el in car_info:
        print(el)