# num_char=len(input("what is your name?"))
# # print("Your name has"+num_char+"characters")
# #print(type(num_char))
# #যখন জানি না কোন টাইপ এর ইনপুট ,তখন এভাবে করতে হবে
#
# # যখন আগের মত করেই করতে চাইবো তখন একতা কাজ করা লাগবে,সেটা হল string বানাইতে হবে type casting আরকি
# new_num_char=str(num_char)
# print("Your name has"+new_num_char+"characters")
two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
The_first_Digit=int(two_digit_number[0])
The_second_Digit=int(two_digit_number[1])
The_output_Digit=int(two_digit_number[0])+int(two_digit_number[1])
print("The output:",The_output_Digit)