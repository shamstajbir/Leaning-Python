
def calculate_overall_grade(grades):
    overall_grades = {}
    for student_id, student_grades in grades.items():
        total_marks = sum(student_grades.values())
        overall_grade = total_marks / len(student_grades)
        overall_grades[student_id] = overall_grade
    return overall_grades


grades = {}
total_students = 0
total_marks = 0
highest_grade = float('-inf')
lowest_grade = float('inf')
grade_distribution = {}


while True:
    student_grades = {}
    print("Enter student's grades for each subject (type 'done' when finished): ")
    while True:
        subject = input("Enter subject name (type 'done' to finish entering grades): ")
        if subject == 'done':
            break
        try:
            grade = float(input(f"Enter grade for {subject}: "))
            if grade < 0 or grade > 100:
                print("Invalid grade! Grade should be between 0 and 100.")
                continue
            student_grades[subject] = grade
        except ValueError:
            print("Invalid input! Please enter a valid grade.")

    if not student_grades:
        break

    grades[total_students + 1] = student_grades
    total_students += 1
    total_marks += sum(student_grades.values())
    for grade in student_grades.values():
        if grade > highest_grade:
            highest_grade = grade
        if grade < lowest_grade:
            lowest_grade = grade
        grade_distribution[grade] = grade_distribution.get(grade, 0) + 1


if total_students != 0:
    average_marks = total_marks / total_students
else:
    average_marks = 0


overall_grades = calculate_overall_grade(grades)

print("\nStudent Performance Overview:")
print(f"Total Students: {total_students}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Highest Grade: {highest_grade}")
print(f"Lowest Grade: {lowest_grade}")
print("\nGrade Distribution:")
for grade, count in sorted(grade_distribution.items()):
    print(f"  Grade {grade}: {count} students")


for student_id, student_grades in grades.items():
    print(f"\nStudent {student_id} Grades:")
    for subject, grade in student_grades.items():
        print(f"  {subject}: {grade}")
    print(f"Overall Grade: {overall_grades[student_id]:.2f}")