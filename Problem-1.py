# OOP Revision Exercise 1 (Easy)
#
# Product
#
# Please define a class named Product.
#
# The constructor should take the following arguments:
# - name: str
# - price: float
#
# The class should contain the following methods:
#
# 1. discount(percent: int)
#    Reduces the price by the given percentage.
#
# 2. is_expensive()
#    Returns True if the product price is greater than 1000,
#    otherwise returns False.
#
# 3. __str__()
#    Returns the string:
#
#    "<name>: <price> euros"
#
#
# Example usage:
#
# phone = Product("iPhone", 1200)
# print(phone)
# print(phone.is_expensive())
#
# phone.discount(10)
# print(phone)
#
#
# Sample output:
#
# iPhone: 1200 euros
# True
# iPhone: 1080.0 euros

class Product:
    def __init__(self, name: str, price: float):
        self.__name=name
        self.__price=price

    def discount(self, percent: int):
        disc_price = self.__price-(self.__price*percent)
        return disc_price
    
    def is_expensive(self):
        return self.__price>1000
    
    def __str__(self):
        return f"{self.__name}: {self.__price} euros"
    
def main():
    phone = Product("iPhone", 1200)
    print(phone)
    print(phone.is_expensive())

    phone.discount(10)
    print(phone)
if __name__=="__main__":
    main()