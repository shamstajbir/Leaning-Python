# number= int(input("Enter the number:"))
# if number%2==0:
#   print("The  number is even.")

# else:
#   print("The number is odd.")


# print("Welcome to the rollercoaster!")
# height = int(input ("What is your height in cm? "))
# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int (input("What is your age? "))
#   if age <= 18:
#     print ("Please pay $7.")
#   else:
#     print ("Please pay $12.")
# else:
#   print("Sorry, you have to grow taller before you can ride.")
# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆
BMI=weight/(height*height)
if BMI<=18.5:
 print(f"your bmi is:{BMI},you are underweight.")
elif BMI<=25:
 print(f"your bmi is:{BMI},you are normal weight.")
elif BMI<=30:
 print(f"your bmi is:{BMI},you are overweight.")
elif BMI<=35:
 print(f"your bmi is:{BMI},you are obese.")
else:
 print(f"your bmi is:{BMI},clinically obese.")

