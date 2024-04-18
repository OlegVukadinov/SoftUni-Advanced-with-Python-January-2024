from collections import Counter

def naughty_or_nice_list(names_list, *args, **kwargs):
    lists = {'Naughty': [], 'Nice': [], 'Not found': []}
    num_counter = Counter(el[0] for el in names_list)

    for pair in args:
        counting_num = int(pair.split('-')[0])
        list_name = pair.split('-')[1]
        if num_counter[counting_num] == 1:
            name = [name for num, name in names_list if num == counting_num]
            lists[list_name].extend(name)
            names_list = [el for el in names_list if el[0] != counting_num]
    name_counter = Counter(el[1] for el in names_list)

    for name, type in kwargs.items():
        if name_counter[name] == 1:
            lists[type].append(name)
            names_list = [el for el in names_list if el[1] != name]

    for num, name in names_list:
        lists["Not found"].append(name)

    output = ""

    for type, kids in lists.items():
        if kids:
            output += f"{type}: {', '.join(kids)}\n"

    return output


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
