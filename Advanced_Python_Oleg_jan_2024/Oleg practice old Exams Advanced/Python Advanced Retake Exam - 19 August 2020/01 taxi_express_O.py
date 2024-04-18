from collections import deque

cutomers_time_list = deque(map(int, input().split(", ")))
taxis_list = deque(map(int, input().split(", ")))
total_time = 0

while cutomers_time_list and taxis_list:
    if cutomers_time_list[0] <= taxis_list[-1]:
        total_time += cutomers_time_list[0]
        cutomers_time_list.popleft()
        taxis_list.pop()
    else:
        taxis_list.pop()

if len(cutomers_time_list) > 0 and len(taxis_list) == 0:
    print("Not all customers were driven to their destinations")
    print(f'Customers left: {", ".join(map(str, cutomers_time_list))}')

elif len(cutomers_time_list) == 0:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")