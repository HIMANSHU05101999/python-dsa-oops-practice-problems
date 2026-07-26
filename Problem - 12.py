# OOP Revision Exercise 12
#
# Bank
#
# Class variable:
#
# interest_rate = 5
#
#
# Each BankAccount has:
#
# owner
# balance
#
#
# yearly_interest()
#
# Returns the interest earned for one year.
#
#
# Class method:
#
# change_interest_rate(rate)
#
# Changes the interest rate for ALL future calculations.
#
#
# Example:
#
# a = BankAccount("Peter",10000)
#
# print(a.yearly_interest())
#
# BankAccount.change_interest_rate(8)
#
# print(a.yearly_interest())
#
#
# Sample output:
#
# 500
# 800

class Bank:
    interest_rate=5


class BankAccount(Bank):

    def __init__(self, owner, balance):
        self.__owner=owner
        self.__balance=balance

    @property
    def owner(self):
        return self.__owner

    @property
    def balance(self):
        return self.__balance

    def yearly_interest(self):
        return ((self.__balance)*type(self).interest_rate/100)

    @classmethod
    def change_interest_rate(cls, int_rate):
        cls.interest_rate=int_rate


def main():
    a = BankAccount("Peter",10000)

    print(a.yearly_interest())

    BankAccount.change_interest_rate(8)

    print(a.yearly_interest())

    BankAccount.change_interest_rate(12)

    print(a.yearly_interest())
if __name__=="__main__":
    main()
    

