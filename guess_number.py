import random
guess_count = 0
guess_limit = 3

random_number = random.randint(1, 10)

while guess_count < guess_limit:
    number = int(input("Guess a number(1-10): "))
    guess_count += 1

    if number == random_number:
        print("Voila, That's Correct")
        break
    else:
        print("You Lost, Better Luck Next time")

print("The random number was ", random_number)