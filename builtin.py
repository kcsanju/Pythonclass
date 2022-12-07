# map , filter


# der total(a, b):
#   return a+b


#lambda a, b:a+b
# total = lambda a, b:a+b
# print(total(10, 15))


#map(func, iterable-object)

# def increment_by_one(n):
#     return n +1

# a = [1, 2, 3, 4, 5, 6, 7, 8,]
# out = map(lambda n:n+1, a)
# print(list(out))

# names = ["ram",  "shyam", "hari", "sita"]
# out = map(lambda name:name.capitalize(), names)
# print(list(out))

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def is_even(num):
#     # if num% 2 == 0
#     #   return true
#     # else:
#     #    return false
#     return num % 2 == 0

# out = filter(lambda num:num %2 ==0, a)
# print(list(out))


# emails = ["1@gmail.com", "2@gmail.com", "3@yahoo.com", "4@gmail.com", "5@yahoo.com", "6@outlook.com"]
# def a(item):
#     return item

# out = filter(lambda item:item.endswith("gmail.com"), emails )
# print(list(out))

# b = "12d57d54d90"



# d = [17, 20, 25, 30]
# print (sum(d))

# c = ["17", "20", "25", "30"]
# total = 0
# for i in c:
#     total = total + int(i)

# print (total)

#or
# print(sum(map(int, c)))

# e = "12d57d54d90"

# f = e.split("d")
# print(f)
# total = 0
# for i in f:
#     total = total +int(i)
# print(total)


a = "457d89e36"
total = 0
for i in a:
    if i.isnumeric():
        total = total + i
print(total)

print(sum(map(int,filter(lambda v:v.isnumeric(),a))))
