numbers = tuple(map(float, input().split()))

numbers_dict = {}

for el in numbers:
    if el not in numbers_dict:
        numbers_dict[el] = numbers.count(el)

for number, count in numbers_dict.items():
    print(f"{number} - {count} times")