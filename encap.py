# class ProductPriceError(Exception):
#     pass

# class Product:

#     def __init__(self, name, sku, price):
#             self.name = name
#             self.sku = sku
#             self.__price = price
#     @property                      #getter
#     def price(self):
#         return self.__price

#     @price.setter                 #setter
#     def price(self, price):
#         if price <=0:
#             raise ProductPriceError("Price can not be smaller then zero")
#         self.__price = price
# tshirt = Product("T-shirt", "123", 500)
# # print(f"price of tshirt: {tshirt.price}")
# # tshirt.price = -1

# print(tshirt.__dict__)
# try:
#     tshirt.price = -200
# except ProductPriceError as err:
#        print(err)
# # tshirt.price = -1
# print(tshirt.__dict__)






class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    @staticmethod
    def sqrt(num):
        return num**0.5

c = Calculator(20, 10)
print(c.add())
print(c.subtract())
print(c.multiply())
print(Calculator.sqrt(25))