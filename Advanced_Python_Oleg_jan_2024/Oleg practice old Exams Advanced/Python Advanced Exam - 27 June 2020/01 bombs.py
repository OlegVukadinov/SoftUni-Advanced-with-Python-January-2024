from collections import deque

bombs_effect = deque(int(x) for x in input().split(', '))
bombs_casings = [int(x) for x in input().split(', ')]

bombs_types = {40: 'Datura Bombs', 60: 'Cherry Bombs', 120: 'Smoke Decoy Bombs'}
bombs_made = {'Cherry Bombs': 0, 'Datura Bombs': 0, 'Smoke Decoy Bombs': 0}

is_bombs_list_filled = False


while bombs_effect and bombs_casings:
    if bombs_made['Cherry Bombs'] >= 3 \
                           and bombs_made['Datura Bombs'] >= 3 \
                           and bombs_made['Smoke Decoy Bombs'] >= 3:
        is_bombs_list_filled = True
        break

    current_effect = bombs_effect.popleft()
    current_causing = bombs_casings.pop()
    sum_value = current_effect + current_causing

    if sum_value in bombs_types.keys():
        bombs_made[bombs_types[sum_value]] += 1
    else:
        bombs_casings.append(current_causing - 5)
        bombs_effect.appendleft(current_effect)

if is_bombs_list_filled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bombs_effect:
    print(f"Bomb Effects: {', '.join(str(x) for x in bombs_effect)}")
else:
    print("Bomb Effects: empty")

if bombs_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bombs_casings)}")
else:
    print("Bomb Casings: empty")

for key, value in bombs_made.items():
    print(f"{key}: {value}")