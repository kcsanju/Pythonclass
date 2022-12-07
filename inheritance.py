class Person:    #parent class
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def profile(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")


class Student(Person):
    def __init__(self, name, address, roll_number):
        super().__init__(name, address)
        self.roll_number = roll_number
    def profile(self):
        super().profile()
        print(f"Roll number: {self.roll_number}")

class Teacher(Person):
    def __init__(self, name, address, designation):
        super().__init__(name, address)
        self.designation = designation

s = Student("Ram", "ktm", 1)
s.profile()