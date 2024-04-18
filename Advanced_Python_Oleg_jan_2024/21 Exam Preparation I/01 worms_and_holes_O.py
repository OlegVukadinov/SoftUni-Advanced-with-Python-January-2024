from collections import deque

worms = list(map(int, input().split()))
hole_size = deque(map(int, input().split()))

matches_counter = 0
non_fit_counter = 0

while worms and hole_size:
    if worms[-1] == hole_size[0]:
        worms.pop()
        hole_size.popleft()
        matches_counter += 1
    else:
        worms[-1] -= 3
        non_fit_counter += 1
        if worms[-1] <= 0:
            worms.pop()
        hole_size.popleft()

if matches_counter > 0:
    print(f"Matches: {matches_counter}")
else:
    print("There are no matches.")

if len(worms) == 0 and non_fit_counter > 0:
    print("Worms left: none")
elif len(worms) == 0 and non_fit_counter == 0:
    print("Every worm found a suitable hole!")

elif len(worms) > 0:
     print(f"Worms left: {', '.join(list(map(str, worms)))}")

if len(hole_size) == 0:
    print("Holes left: none")
elif len(hole_size) > 0:
     print(f"Holes left: {', '.join(deque(map(str,hole_size)))}")