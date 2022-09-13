
import random
counter = 1
number = random.randint(0,100)

guess = int(input("Make your first guess:"))

while (number!=guess):
    if guess<number:
        print("Higher\n")
    else:
        print("Lower\n")
    guess = int(input("Make another guess:"))
    counter = counter + 1

print(f"You won at {counter} time")