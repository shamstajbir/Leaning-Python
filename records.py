class Record:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return self.age > other.age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


if __name__ == "__main__":
    p1 = Record("Shams", 18)
    p2 = Record("Tajbir", 20)

    if p1 > p2:
        print(f"{p1.get_name()} is older than {p2.get_name()}")
    else:
        print(f"{p2.get_name()} is older than {p1.get_name()}")
