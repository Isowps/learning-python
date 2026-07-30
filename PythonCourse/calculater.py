#Dig-digit

dig1 = (int(input("Enter first digit: ")))
dig2 = (int(input("Enter second digit: ")))
operator = input("operation: ")

if operator is "+":
    print(dig1 + dig2)
if operator is "-":
    print(dig1 - dig2)
if operator is "/":
    print (dig1 / dig2)
if operator is "*":
    print(dig1 * dig2)
else:
    print("invalid operation")