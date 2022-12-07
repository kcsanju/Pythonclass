# def decorate_function(func):
#     def wrapper():
#         print("Called before")
#         func()
#         print("Called after")
#     return wrapper

# @decorate_function
# def example ():
#     print("i am example")


# # d = decorate_function(example)
# # d()
# example()
# print (example)

def smart_division(func):
    def wrapper(a, b):
        if b == 0:
            return "can not divide by zero."
        else:
            return func(a, b)
    return wrapper

@smart_division
def division(a, b):
    return a/b

print(division(10, 2))
print(division(10, 0))