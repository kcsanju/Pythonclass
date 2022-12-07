# a = {
#     "properties":{
#         "profile":{
#             "name": "ram",
#             "education":[ 
#                 {"college": "abc", "year":2018},
#                 {"college": "xyz", "year": 2020},
#             ]
#         },
#         "followers": 1000,
#         "following": 100,
#     }
# }

# p = a.get("properties").get("profile")
# print(p)
# b = p.get("name")
# print (b.capitalize())


# name = a.get("properties").get("profile").get("name")
# followers = a.get("properties").get("followers")
# following = a.get("properties").get("following")
# print(f"Name: {name.capitalize()}")
# print(f"followers : {followers}")
# print(f"following: {following}")
# educations = a.get("properties").get("profile").get("education")
# for education in educations:
#     college = education.get("college")
#     year = education.get("year")
#     print(f"education({year}): {college.upper()}")




oil_prices = [
    {
        "oil_type": "petrol",
        "prices":[
            {"year": 2018, "price": 100},
            {"year": 2019, "price": 150},
            {"year": 2020, "price": 180},
        ]
    },
    {
        
        "oil_type": "diesel",
        "prices":[
            {"year": 2018, "price": 80},
            {"year": 2019, "price": 100},
            {"year": 2020, "price": 160},
        ]

    }   

]



a = (oil_prices[0])

oil_type = a.get("oil_type")

print(f"oil type: {oil_type}")
price = a.get("prices")
total= 0
for prices in price:
    year = prices.get("year")
    price = prices.get("price")
    total = total + price
    print(f"Price({year}): {price}")
avg_price = round(total/ len(prices), 2)   
print(f"average price: {avg_price}")
    


print("                                                   ")

a= (oil_prices[1])

oil_type = a.get("oil_type")

print(f"oil type: {oil_type}")
price = a.get("prices")
total = 0
for prices in price:
    year = prices.get("year")
    price = prices.get("price")
    total = total +price
    print(f"Price({year}): {price}")
avg_price = round(total/ len(prices), 2)   
print(f"average price: {avg_price}")