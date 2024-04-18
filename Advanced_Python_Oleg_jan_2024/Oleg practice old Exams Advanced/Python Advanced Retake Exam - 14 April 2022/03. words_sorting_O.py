def words_sorting(*words):
    my_dict = {}

    for word in words:
        if word not in my_dict:
            my_dict[word] = 0
            for word in my_dict:
                counter = 0
                for letter in word:
                    counter += ord(letter)
                    my_dict[word] = counter

    total_sum = sum(my_dict.values())

    result = ""
    if total_sum % 2 == 1:
        sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    else:  # If the sum is even, sort by keys in ascending order
        sorted_dict = sorted(my_dict.items(), key=lambda x: x[0])

    for k, v in sorted_dict:
        result += f"{k} - {v}\n"

    return (result)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))

print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
