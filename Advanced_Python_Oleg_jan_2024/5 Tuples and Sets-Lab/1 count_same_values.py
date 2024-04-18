numbers = list(map(float, input().split()))

numbers_dict = {}

for el in numbers:
    if el not in numbers_dict:
        numbers_dict[el] = 1
    else:
        numbers_dict[el] += 1

for number, count in numbers_dict.items():
    print(f"{number} - {count} times")