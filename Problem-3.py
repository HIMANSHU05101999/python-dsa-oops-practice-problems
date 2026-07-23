# OOP Revision Exercise 3 (Difficult)
#
# Bank Account System
#
# Please define a class named BankAccount.
#
# Constructor arguments:
# - owner: str
# - balance: float
#
#
# Methods:
#
# deposit(amount)
# withdraw(amount)
#
# __str__()
# Returns:
#
# "<owner>: <balance> euros"
#
#
# Operator overloading:
#
# account1 + account2
#
# should return a NEW BankAccount object where:
#
# owner = "Joint Account"
# balance = sum of both balances
#
#
# account1 > account2
# should compare balances.
#
#
# withdraw(amount)
# should raise ValueError if the balance becomes negative.
#
#
# Example usage:
#
# a1 = BankAccount("Peter", 500)
# a2 = BankAccount("Maria", 700)
#
# joint = a1 + a2
#
# print(joint)
# print(a2 > a1)
#
# a1.withdraw(200)
# print(a1)
#
#
# Sample output:
#
# Joint Account: 1200 euros
# True
# Peter: 300 euros

class BankAccount:
    def __init__(self, name: str, balance: float):
        self.__name=name
        self.__balance=balance

    def deposit(self, amount: float):
        self.__balance+=amount

    def withdraw(self, amount: float):
        if self.__balance-amount<0:
            raise ValueError ("Insufficient Balance")
        if amount<0:
            raise ValueError ("Withdraw amount can not be 0 or -ve")
        
        self.__balance-=amount

    def __str__(self):
        return (f"{self.__name}: {self.__balance} euros")
    
    def __add__(self, other: BankAccount):
        return BankAccount("Joint Account", self.__balance+other.__balance)

    def __gt__(self, other: BankAccount):
        return self.__balance>other.__balance

def main():

    a1 = BankAccount("Peter", 500)
    a2 = BankAccount("Maria", 700)

    joint = a1 + a2

    print(joint)
    print(a2 > a1)

    a1.withdraw(200)
    print(a1)
if __name__=="__main__":
    main()
    