# 20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")


class Dog():
    age = 0
    name = ""
    weight = 0

    def bark(self):
        print("%s -> 멍멍" % self.name)


myDog = Dog()
myDog.name = 'Merry'
myDog.weight = 20
myDog.age = 3
myDog.bark()

yourDog = Dog()
yourDog.name = 'Happy'
yourDog.weight = 30
yourDog.age = 5
yourDog.bark()
