first_set = set(map(int, input().split()))
second_set = set(map(int,input().split()))
n = int(input())

for _ in range(n):
    line = input().split()
    command = line[0] + " " + line[1]
    numbers = [int(num) for num in line[2:]]

    if command == "Add First":
        first_set.update(numbers)
    elif command == "Add Second":
        second_set.update(numbers)
    elif command == "Remove First":
        for num in numbers:
            if num in first_set:
                first_set.remove(num)
    elif command == "Remove Second":
        for num in numbers:
            if num in second_set:
                second_set.remove(num)
    elif command == "Check Subset":
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")

sorted_first_set = sorted(first_set)
sorted_second_set = sorted(second_set)

print(*sorted_first_set, sep = ", ")
print(*sorted_second_set, sep = ", ")

