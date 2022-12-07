email= ["1@gmail.com", "2@gmail.com", "3@yahoo.com", "4@gmail.com", "5@outlook.com", "6@yahoo.com"]
output = []
for i in email:
    if i.endswith("@gmail.com"):
        output.append(i)
print(output)



