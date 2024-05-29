# 20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")


def student(name, dep, year):
    print('이름: ', name)
    print('학과: ', dep)
    print('학년: ', year)


student(dep='컴퓨터', name='홍길동', year='1학년')

x = {'name': '홍길동', 'dep': '컴퓨터', 'year': '1학년'}
student(**x)


def student1(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg)


student1(name='홍길동', year='1학년')

student1(dep='컴퓨터', name='홍길동', year='1학년')

y = {'name': '홍길동', 'dep': '컴퓨터', 'year': '1학년'}
student1(**y)
