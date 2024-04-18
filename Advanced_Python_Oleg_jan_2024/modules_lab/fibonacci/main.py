from Advanced_Python_Oleg_jan_2024.modules_lab.fibonacci.core import create_sequence, locate_number

command = input()
sequence = []

while command != "Stop":
    if "Create" in command:
        _, _, number = command.split()
        number = int(number)
        sequence = create_sequence(number)
        print(*sequence)
    else:
        _, number = command.split()
        number = int(number)
        result = locate_number(number, sequence)
        print(result)

    command = input()