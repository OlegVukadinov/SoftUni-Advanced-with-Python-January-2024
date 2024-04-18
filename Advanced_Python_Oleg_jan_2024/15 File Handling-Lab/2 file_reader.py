import os.path

path = os.path.join("my_dir", "numbers.txt")
file = open(path)

total_amount = 0

for line in file.readlines():
    total_amount += int(line.strip())

print(total_amount)




print(file.read())