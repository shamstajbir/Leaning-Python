file = open("finalpract.txt", "w")

file.write("Hello, World!")

file.writelines(["\n", "This is a new line", "\n", "This is another new line", "\n", "This is the last new line", "\n"])

file.flush()
print(file.tell())
file.seek(5)
print(file.tell())

file.close()

file = open("finalpract.txt", "r")

contents = file.read()

print(contents)

file.close()