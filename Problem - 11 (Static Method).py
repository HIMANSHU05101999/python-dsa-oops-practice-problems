# OOP Revision Exercise 11 (Static Methods)
#
# Calculator
#
# Do NOT create Calculator objects.
#
# Instead implement the following static methods:
#
# add(a,b)
# subtract(a,b)
# multiply(a,b)
# divide(a,b)
#
# divide should raise ValueError if b == 0.
#
#
# Example:
#
# print(Calculator.add(10,5))
# print(Calculator.divide(20,4))
#
#
# Sample output:
#
# 15
# 5

class Calculator:
    @staticmethod
    def add(a, b):
        return a+b
    @staticmethod
    def subtract(a, b):
        return a-b
    @staticmethod
    def multply(a, b):
        return a*b
    @staticmethod
    def divide(a, b):
        if b==0:
            raise ValueError
        return a/b

def main():
    print(Calculator.add(10,5))
    print(Calculator.divide(20,4))

if __name__=="__main__":
    main()