import os
file_name = "text.txt"
path = os.path.join("my_dir", file_name)


try:
    file_name = open("my_dir/text.txt", "a")
    print('File found')
except FileNotFoundError:
    print('File not found')