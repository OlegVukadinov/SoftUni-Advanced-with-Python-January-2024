num_of_guests = int(input())

regular_guests = set()
vip_guests = set()

while True:
    command = input()
    if command == "END":
        break

    if command[0].isdigit():
        if command not in vip_guests:
            vip_guests.add(command)
        elif command in vip_guests:
            vip_guests.remove(command)
    else:
        if command not in regular_guests:
            regular_guests.add(command)
        elif command in regular_guests:
            regular_guests.remove(command)

all_in_one = sorted(vip_guests.union(regular_guests))
print(len(all_in_one))
for el in all_in_one:
    print(el)
