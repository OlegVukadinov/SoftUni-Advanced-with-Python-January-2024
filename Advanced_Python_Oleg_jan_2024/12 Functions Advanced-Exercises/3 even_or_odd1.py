def even_odd(*args):
    command = args[-1]
    if command == "even":
        even_list = []
        for el in args[:-1]:
            if el % 2 == 0:
                even_list.append(el)
        return even_list

    elif command == "odd":
        odd_list = []
        for el in args[:-1]:
            if el % 2 != 0:
                odd_list.append(el)
        return odd_list

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))