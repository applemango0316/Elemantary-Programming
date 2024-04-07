#20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")
from random import randint
secret = randint(1, 10)
print("Welcome")
guess = 0
while guess != secret:
    g = input("Guess the number:")
    guess = int(g)
    if guess == secret:
        print("You win!")
    else:
        if guess > secret:
            print("Too high")
        else:
            print("Too low")
print("Game over")
