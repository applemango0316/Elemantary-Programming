# 20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")


def print_nums(*args):
    for arg in args:
        print(arg)


print_nums(11)

print_nums(11, 22, 33, 44, 55)

x = [66, 77, 88, 99]
print_nums(x)
