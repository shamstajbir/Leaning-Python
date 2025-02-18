def validate_price(price):
    try:
        return float(price)
    except ValueError:
        print("Invalid price. Please enter a floating number.")
        return validate_price(input("Enter price: "))

def validate_quantity(quantity):
    try:
        return int(quantity)
    except ValueError:
        print("Invalid quantity. Please enter an integer.")
        return validate_quantity(input("Enter quantity: "))
