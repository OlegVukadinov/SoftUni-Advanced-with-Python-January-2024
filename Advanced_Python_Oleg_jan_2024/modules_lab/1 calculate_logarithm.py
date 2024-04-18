from math import log

number = int(input())
try:
    base = int(input())
    log(number, base)
except ValueError:
    print(f"{log(number):.2f}")