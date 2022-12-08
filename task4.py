students_score = [

    {"name": "Ram", "score": 80},
    {"name": "Sita", "score": 100},
    {"name": "Abc", "score" : 35 },
    {"name": "xyz", "score" :40},
    {"name": "john", "score": 37},
    {"name": "shyam", "score": 90},
    {"name": "hari", "score": 36},
]
out= []
for i in students_score:
    score = i.get("score")
    if score >= 40:
        out.append(i)

print(out)


#using filter
output = list(filter(lambda i:i.get("score") >= 40, students_score))
print(output)


#task 4(2)
colors = ["yellow", "red", "green", "blue", "yellow", "orange", "red"]
remove = ["yellow", "red"]

output = []
for i in colors:
    output.append(i)
output.remove("red")

output.remove("yellow")

print(output)


# del colors[0] 
# del colors[1]
# del colors[2]
# del colors[6]
# print(colors)

# for i in colors:
#     if i == "red": 
#         i.remove("red")
#     print(i)




#task4(3)
 
a = input("enter a first color")
b = input("enter second color")