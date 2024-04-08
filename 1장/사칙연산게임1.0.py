# 20244021, 컴퓨터공학과, 김성준
from random import randint
print("20244021, 컴퓨터공학과, 김성준")
print("사칙연산게임")
first = randint(1, 10)
second = randint(1, 10)
math = randint(1, 3)
g = 1004
if math == 1:
    correct = int(first) + int(second)
    while int(g) != correct:
        print(first)
        print("+")
        print(second)
        g = input("?")
        if int(g) == correct:
            print("정답")
        else:
            print("틀렸습니다")
if math == 2:
    correct = int(first) - int(second)
    while int(g) != correct:
        print(first)
        print("-")
        print(second)
        g = input("?")
        if int(g) == correct:
            print("정답")
        else:
            print("틀렸습니다")
if math == 3:
    correct = int(first) * int(second)
    while int(g) != correct:
        print(first)
        print("*")
        print(second)
        g = input("?")
        if int(g) == correct:
            print("정답")
        else:
            print("틀렸습니다")
print("GAME OVER")
