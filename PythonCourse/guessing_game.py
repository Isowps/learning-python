import random
secret = random.randint(1, 10)

attempt = 1
guess = int(input("Guess the number: "))


while guess != secret:
    
    print("attempt",attempt)
    if guess < secret:
        print("Too low! Try a higher number.")

    elif guess > secret:
        print("Too high! Try a lower number.")
    
    guess = int(input("Try again: "))
    attempt += 1

print("================================")
print("You Win!")
print("The secret number was:",secret)
if attempt == 1:
    print("you got it in your first try!")
else:
    print("You guessed it in",attempt, "attempts!")
print("================================")