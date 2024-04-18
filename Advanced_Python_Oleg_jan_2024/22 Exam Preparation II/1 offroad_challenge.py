from collections import deque

fuel = deque(map(int, input().split()))
consumption = deque(map(int, input().split()))
fuel_needed  = deque(map(int, input().split()))

altitude_counter = 0

while fuel and consumption and fuel_needed:
    result = fuel[-1] - consumption[0]
    if result >= fuel_needed[0]:
        fuel.pop()
        consumption.popleft()
        fuel_needed.popleft()
        altitude_counter += 1
        print(f"John has reached: Altitude {altitude_counter}")
    else:
        print(f"John did not reach: Altitude {altitude_counter + 1}")
        break

# if altitude_counter == 4: # if not fuel:
#     print("John has reached all the altitudes and managed to reach the top!")
#     exit()

if altitude_counter and fuel_needed:# 0 < len(fuel_needed) < 4:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join([f'Altitude {num}' for num in range(1, altitude_counter + 1)])}")

if not altitude_counter and fuel_needed:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")

if altitude_counter == 4: # if not fuel:
    print("John has reached all the altitudes and managed to reach the top!")
    #exit()





