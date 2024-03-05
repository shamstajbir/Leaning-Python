# Creating tuple objects

tuple1 = (1, 2, 3, 4, 5)
print("Tuple 1:", tuple1)

tuple2 = tuple([6, 7, 8, 9, 10])
print("Tuple 2:", tuple2)

single_element_tuple = (11,)
print("Single Element Tuple:", single_element_tuple)

heterogeneous_tuple = ('a', 1, True, 3.14)
print("Heterogeneous Tuple:", heterogeneous_tuple)

tuple_packing = 1, 2, 3, 4, 5
print("Tuple Packing:", tuple_packing)

print("\nAccessing elements of the tuple:")
print("First element of tuple1:", tuple1[0])
print("Last element of tuple2:", tuple2[-1])

try:
    tuple1[0] = 100
except TypeError as e:
    print("TypeError:", e)
