import os.path

path = os.path.join("my_dir", "my_first_file.txt")
file = open(path, "a")

file.write('I just created my first file!')

# print(file.read())