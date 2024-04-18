from collections import deque

caffeinе_mg = deque(map(int, input().split(", ")))
energy_drinks = deque(map(int, input().split(", ")))

drank_caf_counter = 0
caffeine_limit = 300

while caffeinе_mg and energy_drinks:
    result = caffeinе_mg[-1] * energy_drinks[0]

    if caffeine_limit > 300:
        caffeine_limit = 300
    if drank_caf_counter < 0:
        drank_caf_counter = 0

    if result <= caffeine_limit:
        caffeinе_mg.pop()
        energy_drinks.popleft()
        drank_caf_counter += result
        caffeine_limit -= result
    else:
        if drank_caf_counter >= 0:
            caffeinе_mg.pop()
            energy_drinks.append(energy_drinks[0])
            energy_drinks.popleft()
            drank_caf_counter -= 30
            caffeine_limit += 30

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {drank_caf_counter} mg caffeine.")