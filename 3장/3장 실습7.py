#20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")
def sum(n):
        if (n == 1):
            return 1
        else:
            return sum(n-1)+n
    
print("----sum(10)")
print(sum(10))

print("----sum(100)")
print(sum(100))