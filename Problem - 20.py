# OOP Revision Exercise 20
#
# Online Store Inventory
#
# Difficulty: ★★★★☆
#
# Product
#
# Stores:
# - product id
# - name
# - price
# - stock
#
#
# Inventory
#
# Dictionary:
#
# product id -> Product object
#
#
# add_product(product)
#
# If product exists:
#
# Update stock by adding quantities.
#
# Keep the LOWER price.
#
#
# sell_product(id, quantity)
#
# Reduce stock.
#
# Don't allow negative stock.
#
#
# statistics()
#
# total products
# total stock
# inventory value
#
# most expensive product

class Product:
    def __init__(self, prod_id: str, name: str, price: float, stock: int):
        self.__prod_id=prod_id
        self.__name=name
        self.__price=price
        self.__stock=stock

    @property
    def prod_id(self):
        return self.__prod_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def stock(self):
        return self.__stock

    @price.setter
    def price(self,val):
        self.__price=val

    @stock.setter
    def stock(self, val):
        self.__stock=val

    def __str__(self):
        return f"Product ID: {self.__prod_id} Product Name: {self.__name} Price: {self.__price} Stock: {self.__stock}"
class Store:
    def __init__(self):
        self.__storage={}

    def add_product(self, prod_id, name, price, stock):
        prod_obj=Product(prod_id, name, price, stock)
        if prod_obj.prod_id  in self.__storage:
            self.__storage[prod_obj.prod_id].stock += prod_obj.stock
            if prod_obj.price>self.__storage[prod_id].price:
                self.__storage[prod_obj.prod_id].price=prod_obj.price
        else:
            self.__storage[prod_obj.prod_id]=prod_obj

    def sell_product(self, prod_id, amt):
        if prod_id in self.__storage:
            if self.__storage[prod_id].stock>=amt:
                self.__storage[prod_id].stock-=amt
            else:
                print(f"Not Enough Stock, Available: {self.__storage[prod_id].stock}")
        else:
            print("Item not available")

    def view_product(self, prof_id):
        if prof_id in self.__storage:
            return self.__storage[prof_id]

    def stats(self):
        if len(self.__storage)==0:
            print("Empty!!!")
            return
        
        print(f"Total Product: {len(self.__storage)}")
        print(f"Total Stock: {sum([product.stock for _,product in self.__storage.items()])}")
        print(f"Total Inventory Value: {sum([(product.price*product.stock) for _,product in self.__storage.items()])}")
        highest_price=0
        for prod_id,product in self.__storage.items():
            print(product)
            if product.price>highest_price:
                highest_price=product.price
                highest_product=product
        print(f"Highest Value Item: {highest_product}")
        
class Application:
    def __init__(self):
        self.__interact=Store()

    def option(self):
        print("1 add product\n2 sell product\n3 view product\n4 stats\n0 exit")

    def exe(self):
        self.option()
        while True:
            ch=input("Enter Choice: ")
            if ch=="1":
                prod_id=input("Enetr Product ID: ")
                name=input("Enter Product Name: ")
                price=float(input("Enter Product Price: "))
                if price<0:
                    raise ValueError ("Price cannot be less than 0")
                stock=int(input("Enter Stock: "))
                if stock<0:
                    raise ValueError ("Stock cannot be less than 0")
                self.__interact.add_product(prod_id,name,price,stock)
            if ch=="2":
                prod_id=input("Enter the product ID: ")
                amt=int(input("Enter the quantity: "))
                self.__interact.sell_product(prod_id,amt)
            if ch=="3":
                prod_id=input("Enter Product ID: ")
                print(self.__interact.view_product(prod_id))
            if ch=="4":
                self.__interact.stats()
            if ch=="0":
                return

#if __name__=="__main__":
app=Application()
app.exe()