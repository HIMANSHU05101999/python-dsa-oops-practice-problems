# OOP Revision Exercise 7 (Boss Level)
#
# Shopping System
#
# Please define:
#
# Product
# ----------------
# name
# price
#
#
# ShoppingCart
# ----------------
# customer_name
# stores Product objects
#
#
# Methods:
#
# add_product(product)
#
# remove_product(name)
#
# total_price()
#
# most_expensive_product()
#
#
# Operator Overloading:
#
# cart1 + cart2
#
# returns a NEW ShoppingCart:
#
# customer_name = "Merged Cart"
#
# containing products from both carts.
#
#
# Inheritance:
#
# PremiumShoppingCart(ShoppingCart)
#
# Additional attribute:
#
# discount_percentage
#
# Override total_price()
#
# Premium users automatically receive discount.
#
#
# Example:
#
# cart = PremiumShoppingCart("Himanshu",10)
#
# cart.add_product(Product("Laptop",70000))
# cart.add_product(Product("Mouse",1000))
#
# print(cart.total_price())
#
#
# Sample output:
#
# 63900

class Product:
    def __init__(self, name: str, price: float):
        self.__name=name
        self.__price=price

    def __str__(self):
        return f"{self.__name}: {self.__price} euros"

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

class ShoppingCart:
    def __init__(self, cus_name: str):
        self._cus_name=cus_name
        self._cart=[]

    def __str__(self):
        if not self._cart:
            return "Cart is Empty"
        string=""
        for product in self._cart:
            string+=f"{product.name}: {product.price}\n"
        return f"{self._cus_name}:\n{string}"
        
    def add_product(self, product: Product):
        self._cart.append(product)

    def remove_product(self, product_name: str):
        for product in self._cart:
            if product_name == product.name:
                self._cart.remove(product)

    def total_price(self):
        total=0
        for product in self._cart:
            total+=product.price
        return total

    def most_expensive(self):
        most_exp=self._cart[0]
        for product in self._cart:
            if most_exp.price<product.price:
                most_exp=product
        return most_exp

    def view_items(self):
        return self._cart

    def __add__(self, other: Product):
        merged_cart=ShoppingCart("Merged Cart")
        combined_cart=self._cart + other._cart
        for product in combined_cart:
            merged_cart.add_product(product)
        return merged_cart


class PremiumShoppingCart(ShoppingCart):
    def __init__(self, cus_name, disc_perc: int):
        super().__init__(cus_name)
        self._disc_perc=disc_perc

    def total_price(self):
        total_bill=super().total_price()
        discounted = total_bill-(total_bill*self._disc_perc)/100
        return discounted

def main():
    #cart1=ShoppingCart("Himanshu")
    #cart2=ShoppingCart("Kumar")
    #bhindi=Product("Bhindi",12)
    #dhania=Product("Dhania",15)
    #aloo=Product("Aloo",20)
    #cart1.add_product(bhindi)
    #cart2.add_product(dhania)
    #cart1.add_product(aloo)
    #new=cart1+cart2
    #print(cart1.total_price())
    #most_exp=(cart1.most_expensive())
    #print(cart1.remove_product(most_exp.name))
    #for item in cart1.view_items():
    #    print(item)
    #print(new.total_price())
    
    cart = PremiumShoppingCart("Himanshu",10)

    cart.add_product(Product("Laptop",70000))
    cart.add_product(Product("Mouse",1000))

    print(cart.total_price())
if __name__=="__main__":
    main()