#20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")
def add(n):
    number = 1
    sum = 0
    while number <= n:
        sum = sum + number
        number = number + 1
    return sum

print("----add(10)")
print(add(10))
print("----add(100)")
print(add(100))