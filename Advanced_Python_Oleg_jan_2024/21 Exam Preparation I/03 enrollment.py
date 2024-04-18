def gather_credits(number_of_credits_needed, *course_info):
    current_credits = 0
    courses_enrolled = {}

    for course_name, credits in course_info:
        if current_credits >= number_of_credits_needed:
            break
        if course_name not in courses_enrolled:
            courses_enrolled[course_name] = credits
            current_credits += credits

    if current_credits >= number_of_credits_needed:
        return (f"Enrollment finished! Maximum credits: {current_credits}.\n"
                f"Courses: {', '.join(sorted(courses_enrolled))}")
    else:
        return f"You need to enroll in more courses! You have to gather {number_of_credits_needed - current_credits} credits more."



print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
