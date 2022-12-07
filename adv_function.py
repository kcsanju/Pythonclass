# def welcome(name):
#     print(f"welcome {name}!")
# a = welcome
# a("shyam")

def increment(num):
    def increase_by(factor):
        return num + factor
    return increase_by
increase_by = increment(20)
print(increase_by(20))
print(increase_by(10))


    