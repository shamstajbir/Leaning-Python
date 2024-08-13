def is_palindrome(s):

    return s == s[::-1]


def show_palindromic_substrings(s):

    n = len(s)
    palindromic_substrings = set()


    for start in range(n):
        for end in range(start + 1, n + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                palindromic_substrings.add(substring)

    print("Palindromic substrings are:")
    for palindrome in palindromic_substrings:
        print(palindrome)


if __name__ == "__main__":
    input_string = input("Enter a string: ").strip()


    if is_palindrome(input_string):
        print(f"The string '{input_string}' is a palindrome.")
    else:
        print(f"The string '{input_string}' is not a palindrome.")


    show_palindromic_substrings(input_string)
