from collections import deque

food = deque(map(int, input().split(", ")))
stamina = deque(map(int, input().split(", ")))
all_peaks = deque([("Vihren", 80), ("Kutelo", 90), ("Banski Suhodol", 100), ("Polezhan", 60), ("Kamenitza", 70)])

conquered_peaks = []
day_counter = 1
while food and stamina and all_peaks:
    result = food[-1] + stamina[0]

    if result >= all_peaks[0][1]:
        food.pop()
        stamina.popleft()
        conquered_peaks.append(all_peaks[0][0])
        all_peaks.popleft()
        day_counter += 1

    elif result < all_peaks[0][1]:
        food.pop()
        stamina.popleft()
        day_counter += 1

if len(conquered_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
elif day_counter > 7:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    for el in conquered_peaks:
        print(el)



