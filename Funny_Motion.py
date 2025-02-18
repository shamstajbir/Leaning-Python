# Probelem-1 Code:
import math
def calculate_area(radius):
    return math.pi * radius * radius
radius = float(input("Enter the radius: "))
area = calculate_area(radius)
print(f"A = {area}")