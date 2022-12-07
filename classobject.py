# class Student:

#     def __init__(self, _id, roll_no, name, gender):
#         self._id = _id
#         self.roll_number = roll_no
#         self.name = name
#         self.gender = gender
#         self.total_attendance = 0
#     def view_attendance(self):
#         return f"Total attendance of {self.name} is {self.total_attendance}"

# s = Student(1, 2, "Ram", "Male")
# #print(s.__dict__)
# print(f"name: {s.name}")
# print(f"roll_number: {s.roll_number}")
# print(s.view_attendance())
# s2 = Student(2, 3, "Sita", "Female")
# print(s2.view_attendance())

# #################STUDENTS RECORD###################
# students = []
# for i in range(1, 6):
#     roll_n = input("Enter a roll number:")
#     name = input("Enter name:")
#     gender = input("Enter gender:")
#     s = Student(i , roll_n, name, gender)
#     students.append(s)

# for student in students:
#     print(f"Name: {student.name}")
#     print(f"roll number: {student.roll_number}")
#     print(student.view_attendance())
#     print("-"*50)


class Staff:

    def __init__(self, _id, designation, name, contact):
        self._id = _id
        self.designations = designation
        self.name = name
        self.contacts = contact
        self.contact_num = 100
    def view_contact_num(self):
        return f"contact number of {self.name} is {self.contact_num}"

# s = Staff(1, 10, "Ram", "11")
# print(f"name: {s.name}")
# print(f"designations : {s.designations}")
# # print(s.view_contacts())

staffs = []
for i in range(1, 6):
    designations = input("Enter a designation :")
    name = input("Enter name:")
    contact = input("Enter contact number:")
    s = Staff(i , designations, name, contact)
    staffs.append(s)

for staff in staffs:
    print(f"Name: {staff.name}")
    print(f"designation: {staff.designations}")
    print(staff.view_contact_num())
    print("-"*50)