import sys

print("====================")
print("Welcome! To Calculator!")
print("Proceed?")
use = input("Yes or No: ").lower().replace(" ", "")
print("====================")

if use == "yes":
    print("Thanks!")
else:
    print("Okay!")
    sys.exit()

print("Addition______(+)")
print("Subtraction___(-)")
print("Multiplication(*)")
print("Division______(/)")
print("Power_________(^)")
operation = input("Select Operators: ").lower().replace(" ", "")
print("====================")
digit_one = int(input("Enter 1st Digit: "))
digit_two = int(input("Enter 2nd Digit: "))

operations = ["+", "-", "*", "/","**"]

while operation not in operations:
    
    operation = (input("Invalid! Select again: "))

if operation == "+":
        print(digit_one + digit_two)

elif operation  == "-":
        print(digit_one - digit_two)

elif operation == "*":
        print(digit_one * digit_two)

elif operation == "/":
        print(digit_one / digit_two)
elif operation == "**":
      print(digit_one ** digit_two)

