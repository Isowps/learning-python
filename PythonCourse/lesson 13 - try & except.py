try:
    age = int(input("enter your age: "))
    print("next year you will be", age + 1)
except:
    print("enter a valid number!")

#mini challenge 1
try:
    number = int(input("Enter a number: "))
    print("double:", number * 2)
except:
    print("Invalid number!")

#mini challenge 2
try:
    digit_1 = int(input("Enter 1st number: "))
    digit_2 = int(input("Enter 2nd number: "))
    print("sum:", digit_1 + digit_2)
except:
    print("enter a valid number!")

#Mini Project — Safe Calculator
try:
    print("Safe Calculator")
    digit1 = int(input("Enter 1st number: ")) 
    digit2 = int(input("Enter 2nd number: "))
    print("sum of both:", digit1 + digit2)
except:
    print("invalid number!") 