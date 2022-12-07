#print(sum(range(3, 101, 3)))
total = 0
for i in range(1, 101):
    if i%3 == 0 or i %5 == 0:
        total += i
print(total)
