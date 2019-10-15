from random import randint

while(True):
    user_guess = int(input("Enter a value between 1 and 10: "))
    if user_guess > 0 and user_guess <= 10:
        break
    else:
        print("Invalid entry, try again....")

print("Generated random number...")

computer_number = randint(1, 10)

print()
print("The computer came up with:", computer_number)
print("You guessed:", user_guess)

if(computer_number == user_guess):
    print("Congrats, you and the computer came up with the same number!!")
else:
    print("You did not come up with the same number as the computer")