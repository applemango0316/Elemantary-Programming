#20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")
print("사칙연산게임")
from random import randint
first1 = randint (1, 10)
second1 = randint (1, 10)
math1 = randint (1, 3)
g1 = 1004
print("1단계")
if math1 == 1:
    correct1 = int(first1) + int(second1)
    while int(g1) != correct1:
        print(first1)
        print("+")
        print(second1)
        g1 = input("?")
        if int(g1) == correct1:
            print("정답")
        else:
            print("틀렸습니다")
if math1 == 2:
    correct1 = int(first1) - int(second1)
    while int(g1) != correct1:
        print(first1)
        print("-")
        print(second1)
        g1 = input("?")
        if int(g1) == correct1:
            print("정답")
        else:
            print("틀렸습니다")
if math1 == 3:
    correct1 = int(first1) * int(second1)
    while int(g1) != correct1:
        print(first1)
        print("*")
        print(second1)
        g1 = input("?")
        if int(g1) == correct1:
            print("정답")
        else:
            print("틀렸습니다")
print("1단계 클리어!")
print("2단계")
from random import randint
first2 = randint (10, 100)
second2 = randint (10, 100)
math2 = randint (1, 3)
g2 = 1004100410041004
if math2 == 1:
    correct2 = int(first2) + int(second2)
    while int(g2) != correct2:
        print(first2)
        print("+")
        print(second2)
        g2 = input("?")
        if int(g2) == correct2:
            print("정답")
        else:
            print("틀렸습니다")
if math2 == 2:
    correct2 = int(first2) - int(second2)
    while int(g2) != correct2:
        print(first2)
        print("-")
        print(second2)
        g2 = input("?")
        if int(g2) == correct2:
            print("정답")
        else:
            print("틀렸습니다")
if math2 == 3:
    correct2 = int(first2) * int(second2)
    while int(g2) != correct2:
        print(first2)
        print("*")
        print(second2)
        g2 = input("?")
        if int(g2) == correct2:
            print("정답")
        else:
            print("틀렸습니다")
print("2단계 클리어")
from random import randint
first3 = randint (100, 1000)
second3 = randint (100, 1000)
math3 = randint (1, 3)
g3 = 1004100410041004100410041004
print("3단계")
if math3 == 1:
    correct3 = int(first3) + int(second3)
    while int(g3) != correct3:
        print(first3)
        print("+")
        print(second3)
        g3 = input("?")
        if int(g3) == correct3:
            print("정답")
        else:
            print("틀렸습니다")
if math3 == 2:
    correct3 = int(first3) - int(second3)
    while int(g3) != correct3:
        print(first3)
        print("-")
        print(second3)
        g3 = input("?")
        if int(g3) == correct3:
            print("정답")
        else:
            print("틀렸습니다")
if math3 == 3:
    correct3 = int(first3) * int(second3)
    while int(g3) != correct3:
        print(first3)
        print("*")
        print(second3)
        g3 = input("?")
        if int(g3) == correct3:
            print("정답")
        else:
            print("틀렸습니다")
print("YOU WIN")
print("GAME OVER")
