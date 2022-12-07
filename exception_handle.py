# try:
#     #code
# except Exception : #catch specific error or exception
#         #code
# except Exception : #catch spevific error or exception
#         #code
# else:
#         #code
try:
     
    a = int(input("num1"))
    b = int(input("num2"))
except ValueError:
    print("can not converted to integer")
else:

    print (a + b)
name = input("enter name:")
print(name) 
