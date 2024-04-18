# text = input()
# sorted_text = sorted(text)
# sorted_text = tuple(sorted_text)
# for el in sorted_text:
#     occur = text.count(el)
#     print(f"{el}: {occur} time/s")

text = input()

my_dict = {}

for el in text:
    if el not in my_dict:
        my_dict[el] = 0
    my_dict[el] += 1

some_dict = dict(sorted(my_dict.items(), key=lambda x:x[0]))

for k, v in some_dict.items():
    print(f"{k}: {v} time/s")