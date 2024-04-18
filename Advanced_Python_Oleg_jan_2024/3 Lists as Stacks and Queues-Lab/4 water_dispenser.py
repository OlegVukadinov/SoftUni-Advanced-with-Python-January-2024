from collections import deque

water_in_dispenser = int(input())

people = deque()

while True:
    command = input()
    if command == "Start":
        break
    people.append(command)

while True:
    command = input()
    if command == "End":
        break
    data = command.split()
    if len(data) == 1:
        wanted_liters = int(data[0])
        person = people.popleft()

        if water_in_dispenser >= wanted_liters:
            print(f"{person} got water")
            water_in_dispenser -= wanted_liters
        else:
            print(f"{person} must wait")

    elif len(data) == 2:
        name = data[0]
        refill_liters = int(data[1])
        water_in_dispenser += refill_liters

print(f"{water_in_dispenser} liters left")