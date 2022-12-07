# *args, **kwargs

def example(*args):
    print(args)

example(1, 2, 3, 4, 5)


def example2(**kwargs):
    print(kwargs)

example2(name = "ram", contact= "1212", nickname = "rr")


def example3(*args, **kwargs):
    print(args, kwargs)

example3(1, 2, 3, name = "ram", roll ="37")

def multiple_of_num(num1, Factor = 5):
    return num1 * Factor
print(multiple_of_num(10))