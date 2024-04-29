# write a python program to demonstrate various
# ways of accessing the string .by using indexing
# (both positive and negative),
# by using slice operator.

if __name__ == "__main__":

    sample_string =input("Enter a string to demonstrate indexing and slicing: ")

    print("Positive Indexing starting from here:")
    print("Character at index 0:", sample_string[0])
    print("Character at index 4:", sample_string[4])
    print("Character at index 7:", sample_string[7])

    print("\nNegative Indexing:")
    print("Character at index -1:", sample_string[-1])
    print("Character at index -2:", sample_string[-2])
    print("Character at index -7:", sample_string[-7])

    print("\nSlicing Examples:")
    print("Substring from index 0 to 4:", sample_string[0:5])
    print("Substring from index 7 to end:", sample_string[7:])
    print("Substring from start to index 4:", sample_string[:5])
    print("Substring from -7 to -1:", sample_string[-7:-1])
    print("Substring with step of 2:", sample_string[0:13:2])


    reversed_string = sample_string[::-1]
    print("\nReversed String:", reversed_string)


