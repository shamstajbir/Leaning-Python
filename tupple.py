# Creating tuple objects in Python

tuple1 = (1, 2, 3, 4, 5)
print("Tuple 1:", tuple1)

tuple2 = tuple([6, 7, 8, 9, 10])
print("Tuple 2:", tuple2)

tuple3 = ()
print("Empty Tuple:", tuple3)

tuple4 = (11,)
print("Tuple with single element:", tuple4)

tuple5 = (1, "hello", 3.14, True)
print("Tuple with mixed data types:", tuple5)

tuple6 = (1,) * 5
print("Tuple created using repetition operator:", tuple6)

tuple7 = tuple1 + tuple2
print("Concatenated Tuple:", tuple7)

string = "hello"
tuple8 = tuple(string)
print("Tuple from string:", tuple8)
