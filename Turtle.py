
tuple1 = tuple(input("Enter elements for tuple1 separated by spaces: ").split())
tuple2 = tuple(input("Enter elements for tuple2 separated by spaces: ").split())
tuple3 = tuple(input("Enter elements for tuple3 separated by spaces: ").split())

common_elements = tuple(set(tuple1) & set(tuple2) & set(tuple3))


print("New tuple containing common elements:", common_elements)
