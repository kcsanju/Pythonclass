a = input("name")
b = input("class")
c = input("roll")
sci = int(input("marks in science"))
math = int(input("marks in math"))
eng = int(input("marks in english"))
print("name=",a) ; print("class=",b) ; print("roll=",c)
print("marks in science=",sci)
print("marks in math=",math)
print("marks in english=",eng)
total = sci + math + eng
per = (total/300) * 100
print("total marks=",total)
print("percentage=",per)
if per < 40:
    print("fail")
else:
    print("pass")