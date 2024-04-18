n = int(input())
unique_usernames = set()
for _ in range(n):
    username = input()
    unique_usernames.add(username)

for el in unique_usernames: # може и така print(*unique_usernames, sep="\n"
    print(el)
