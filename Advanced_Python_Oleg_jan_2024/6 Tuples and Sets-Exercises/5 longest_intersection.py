n = int(input())
longest_intersection = set()

for _ in range(n):
    first_data, second_data = [el.split(",") for el in input().split("-")]

    first_set = set(range(int(first_data[0]), int(first_data[1]) + 1))  # set1
    second_set = set(range(int(second_data[0]), int(second_data[1]) + 1))  # set2

    intersection = (first_set).intersection(second_set)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] with length {len(longest_intersection)}")