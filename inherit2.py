class User:
    def __init__(self, _id, username, pwd):
        self._id = _id
        self.username =username
        self.password = pwd
    
class Person(User):    
    def __init__(self, _id, username, pwd, name, address):
        super().__init__(_id, username, pwd)
        self.name = name
        self.address = address

    def profile(self):
        
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")

class Staff(Person):
    def __init__(self, _id, username, pwd, name, address, designation):
        super().__init__(_id, username, pwd, name, address)
        self.designation = designation
    def profile(self):
        print(f"Username: {self.username}")
        print(f"id: {self._id}")
        super().profile()
        print(f"designation: {self.designation}")
s = Staff(10, "ram12", 1234, "Ram", "ktm", "manager") 
s.profile()     