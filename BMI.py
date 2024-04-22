# # 1st input: enter height in meters e.g: 1.95
# height = input()
# # 2nd input: enter weight in kilograms e.g: 89
# weight = input()
#
# height_as_float=float(height)
# weight_as_int=int(weight)
# BMI=weight_as_int/height_as_float**2
# BMI_as_int=int(BMI)
# print("Your BMI:",BMI_as_int)

# Enter your height in meters e.g., 1.55
height = float(input("Enter your height in meters:"))
# Enter your weight in kilograms e.g., 72
weight = int(input("Enter your weight in kilograms:"))
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






