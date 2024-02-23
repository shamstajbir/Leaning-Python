def is_palindrome(s):

    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())

    return s == s[::-1]

if __name__ == "__main__":
    string_to_check = input("Enter a number : ")
    if is_palindrome(string_to_check):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
