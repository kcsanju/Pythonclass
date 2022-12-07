num1 = int(input(" first number"))
num2 = int(input("second number"))
num3 = int(input("third number"))
if num1<=num2 and num1<=num3:
    print(num1,"smallest number")
elif num2<=num1 and num2<=num3:
    print(num2,"smallest number")
elif num3<=num1 and num3<=num2:
    print(num3,"smallest number")