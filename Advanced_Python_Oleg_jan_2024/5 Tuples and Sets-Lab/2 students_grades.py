n = int(input())

stud_grades = {}

for _ in range(n):
    name, grade_as_string = input().split()
    grade = float(grade_as_string)

    if name not in stud_grades:
        stud_grades[name] = []
    stud_grades[name].append(grade)

for name, grades in stud_grades.items():
    average_grade = sum(grades) / len(grades)
    formatted_grades = f"{' '.join([f'{g:.2f}' for g in grades])}"
    print(f"{name} -> {formatted_grades} (avg: {average_grade:.2f})")

