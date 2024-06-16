# 20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")


class Dog():
    age = 0
    name = "noname"
    weight = 0

    def bark(self, name):
        print("1. %s -> 멍멍" % self.name)
        print("2. %s -> 멍멍" % Dog.name)
        print("3. %s -> 멍멍" % name)


myDog = Dog()
myDog.name = 'Merry'
myDog.weight = 20
myDog.age = 3
myDog.bark("메리")

yourDog = Dog()
yourDog.name = 'Happy'
yourDog.weight = 30
yourDog.age = 5
yourDog.bark("해피")
