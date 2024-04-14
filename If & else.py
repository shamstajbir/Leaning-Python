# number= int(input("Enter the number:"))
# if number%2==0:
#   print("The  number is even.")

# else:
#   print("The number is odd.")


print("Welcome to the rollercoaster!")
height = int(input ("What is your height in cm? "))
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int (input("What is your age? "))
  if age <= 18:
    print ("Please pay $7.")
  else:
    print ("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")