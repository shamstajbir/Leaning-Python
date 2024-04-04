num_char=len(input("what is your name?"))
# print("Your name has"+num_char+"characters")
#print(type(num_char))
#যখন জানি না কোন টাইপ এর ইনপুট ,তখন এভাবে করতে হবে

# যখন আগের মত করেই করতে চাইবো তখন একতা কাজ করা লাগবে,সেটা হল string বানাইতে হবে type casting আরকি
new_num_char=str(num_char)
print("Your name has"+new_num_char+"characters")
