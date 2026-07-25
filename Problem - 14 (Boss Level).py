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