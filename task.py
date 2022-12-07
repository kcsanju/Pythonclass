m = []
e = []
o = []
d = []
for i in range(15):
    num = int(input("enter the number"))
    print(num)
    if num in m:
        d.append(num)
    else:

        if (num%2 == 0):
            e.append(num)
        else:
            o.append(num)
    m.append(num)
print(f"main list: {m}")
print(f"even list: {e}")
print(f"odd list : {o}")
print(f"duplicate list: {d}")

