n = int(input())

unick_elements = set()

for _ in range(n):
    compound = input().split()
    for el in compound:
        unick_elements.add(el)

for element in unick_elements: # or print(*unick_element, sep="\n")
    print(element)
