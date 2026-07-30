#round 2 
#mini challenge 1
try:
    age = int(input("enter age: "))
    print("You are", age,"years old")
except:
    print("enter a valid age!")

#mini challenge 2
while True:
    try:
        ages = int(input("enter your age: "))
        print("You are", ages,"years old")
        break
    except:
        print("enter a valid age! ")