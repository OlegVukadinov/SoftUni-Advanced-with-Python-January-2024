def students_credits(*args):

    course_data = {}

    for info in args:
        course_name, credits, max_test_points, diyan_points = info.split("-")
        diyan_credits = (int(diyan_points) / int(max_test_points)) * int(credits)
        if course_name not in course_data:
            course_data[course_name] = diyan_credits

    total_sum = sum(course_data.values())

    final_strings = []
    if total_sum >= 240:
        final_strings.append(f"Diyan gets a diploma with {total_sum:.1f} credits.")
    else:
        final_strings.append(f"Diyan needs {240 - total_sum:.1f} credits more for a diploma.")

    sorted_course_data = sorted(course_data.items(), key=lambda x: x[1], reverse=True)
    for k, v in sorted_course_data:
        final_strings.append(f"{k} - {float(v):.1f}")

    return "\n".join(final_strings)


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
