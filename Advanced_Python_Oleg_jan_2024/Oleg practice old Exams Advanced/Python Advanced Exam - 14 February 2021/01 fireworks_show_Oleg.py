from collections import deque

firework_effects = deque(map(int, input().split(", ")))
explosive_power = deque(map(int, input().split(", ")))

palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0

while firework_effects and explosive_power:
    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        break
    if firework_effects[0] <= 0:
        firework_effects.popleft()
        continue
    elif explosive_power[-1] <= 0:
        explosive_power.pop()
        continue
    sum_num = firework_effects[0] + explosive_power[-1]

    if sum_num % 3 == 0 and sum_num % 5 != 0:
        palm_fireworks += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif sum_num % 5 == 0 and sum_num % 3 != 0:
        willow_fireworks += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif sum_num % 3 == 0 and sum_num % 5 == 0:
        crossette_fireworks += 1
        firework_effects.popleft()
        explosive_power.pop()
    else:
        firework_effects[0] -= 1
        firework_effects.append(firework_effects[0])
        firework_effects.popleft()

if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")

print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")