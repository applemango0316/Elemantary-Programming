# 20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")


class Person():
    name = ""

    def __init__(self):
        print("Person created")


class Employee(Person):
    job_title = ""

    def __init__(self):
        print("Employee created")


class Customer(Person):
    email = ""

    def __init__(self):
        print("Customer created")


johnSmith = Person()
janeEmployee = Employee()
bobCustomer = Customer()


class Person():
    name = ""

    def __init__(self):
        print("Person created")


class Employee(Person):
    job_title = ""

    def __init__(self):
        Person.__init__(self)
        print("Employee created")


class Customer(Person):
    email = ""

    def __init__(self):
        Person.__init__(self)
        print("Customer created")


johnSmith = Person()
janeEmployee = Employee()
bobCustomer = Customer()
