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
