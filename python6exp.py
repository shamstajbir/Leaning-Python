def get_student_info():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")

    return name, age, grade


student_name, student_age, student_grade = get_student_info()

print("Student Name:", student_name)
print("Student Age:", student_age)
print
