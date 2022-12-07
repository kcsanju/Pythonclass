def profile(name, address, contact):
    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"Contact: {contact}")

profile("Ram", "Ktm", "1272873")  #positional argument
print("----------------------------------------------")
profile("Ram", "1272873", "Ktm")

print("---------------------------------------")
print("-------------------------------------")
profile(name= "Ram", address ="ktm", contact="221213")
print("-------------------------------------------------")
profile(name= "Ram", contact="121212121", address= "ktm",)
#keyword argument

