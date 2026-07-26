# OOP Revision Exercise 14 (Boss Level)
#
# Vehicle Registry
#
# Vehicle
#
# Class variable:
#
# next_registration = 1000
#
#
# Every Vehicle receives the next available registration number.
#
#
# Vehicle should also keep a dictionary:
#
# registry
#
# registration_number -> vehicle_object
#
#
# Class methods:
#
# get_vehicle(registration_number)
#
# returns the Vehicle object.
#
#
# total_registered()
#
# returns the number of registered vehicles.
#
#
#
# Car(Vehicle)
#
# Bike(Vehicle)
#
# inherit Vehicle without duplicating any registration logic.
#
#
# Example:
#
# c1 = Car("Tesla")
# c2 = Car("BMW")
# b1 = Bike("Yamaha")
#
# print(Vehicle.total_registered())
#
# print(Vehicle.get_vehicle(1001))
#
#
# Sample output:
#
# 3
# BMW

class Vehicle:
    next_registration = 1000
    count=0
    registry={}

    def __init__(self, name):
        self._name=name
        Vehicle.count+=1
        Vehicle.registry[Vehicle.next_registration]=self
        Vehicle.next_registration+=1

    def __str__(self):
        return f"{self._name}"
    
    @classmethod
    def total_registered(cls):
        return cls.count

    @classmethod
    def get_vehicle(cls, reg_no):
        return cls.registry[reg_no]


class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)


class Bike(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        

def main():
    c1 = Car("Tesla")
    c2 = Car("BMW")
    b1 = Bike("Yamaha")

    print(Vehicle.total_registered())

    print(Vehicle.get_vehicle(1001))
if __name__=="__main__":
    main()