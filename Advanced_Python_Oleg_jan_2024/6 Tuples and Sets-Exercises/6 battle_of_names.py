n = int(input())

odd_set = set()
even_set = set()

for curr_num in range(1, n + 1):
    name = input()
    sum_of_letters_in_name = 0
    for letter in name:
        sum_of_letters_in_name += ord(letter)
        final_value = int(sum_of_letters_in_name / curr_num)
    if final_value % 2 == 0:
        even_set.add(final_value)
    else:
        odd_set.add(final_value)

if sum(odd_set) == sum(even_set):
    print(*(odd_set.union(even_set)), sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*(odd_set.difference(even_set)), sep=", ")
elif sum(odd_set) < sum(even_set):
    print(*(odd_set.symmetric_difference(even_set)), sep=", ")

