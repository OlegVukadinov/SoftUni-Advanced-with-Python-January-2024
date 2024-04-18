from collections import deque

worms = deque(map(int, input().split()))
holes = deque(map(int, input().split()))

matches_counter = 0
non_fit_counter = 0

while worms and holes:
    if worms[-1] <= 0:
        worms.pop()
    elif worms[-1] == holes[0]:
        worms.pop()
        holes.popleft()
        matches_counter += 1
    else:
        holes.popleft()
        worms[-1] -= 3
        non_fit_counter += 1

if matches_counter > 0:
    print(f"Matches: {matches_counter}")
else:
    print("There are no matches.")

if len(worms) == 0 and non_fit_counter == 0:
    print("Every worm found a suitable hole!")
elif len(worms) == 0 and non_fit_counter > 0:
    print("Worms left: none")
elif len(worms) > 0:
    print(f"Worms left: {', '.join(map(str, worms))}")

if len(holes) == 0:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(map(str, holes))}")
