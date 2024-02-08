class Student:
    def __init__(self):
        self.uid = 0
        self.name = ""

    def in_info(self):
        self.uid = int(input("Enter your uid: "))
        self.name = input("Enter your name: ")


class Subjects(Student):
    def __init__(self):
        super().__init__()
        self.m1 = 0

    def in_subjects(self):
        self.m1 = float(input("Enter your marks in 5 subjects (out of 500): "))


class Sports(Student):
    def __init__(self):
        super().__init__()
        self.m2 = 0

    def in_sports(self):
        self.m2 = int(input("Enter your marks in sports: "))


class Result(Subjects, Sports):
    def out_result(self):
        print("\nuid:", self.uid)
        print("Name:", self.name)
        print("Academic Marks:", self.m1 / 5)
        print("Sports marks:", self.m2)
        print("Final Result (out of 100):", float((self.m1 / 5 + self.m2) / 2.00))


def main():
    a = Result()
    a.in_info()
    a.in_subjects()
    a.in_sports()
    a.out_result()


if __name__ == "__main__":
    main()
