# 1st input: enter height in meters e.g: 1.95
height = input()
# 2nd input: enter weight in kilograms e.g: 88
weight = input()

height_as_float=float(height)
weight_as_int=int(weight)
BMI=weight_as_int/height_as_float**2
BMI_as_int=int(BMI)
print("Your BMI:",BMI_as_int)