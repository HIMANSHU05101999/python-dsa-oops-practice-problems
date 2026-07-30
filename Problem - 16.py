# OOP Revision Exercise 16
#
# Employee Management
#
# Difficulty: ★★☆☆☆
#
# Employee
#
# Stores:
# - employee id
# - name
# - salary
#
#
# Company
#
# Dictionary:
#
# employee_id -> Employee object
#
#
# add_employee(employee)
#
# If an employee id already exists:
#
# Keep whichever Employee has the HIGHER salary.
#
#
# statistics()
#
# Print:
#
# total employees
# highest salary
# average salary
#
#
# Interface:
#
# 1 add employee
# 2 search employee
# 3 statistics
# 0 exit


class Employee:
    def __init__(self, emp_id: int,emp_name: str,emp_salary: float):
        self.__emp_id=emp_id
        self.__emp_name=emp_name
        self.__emp_salary=emp_salary

    @property
    def emp_id(self):
        return self.__emp_id

    @property
    def emp_name(self):
        return self.__emp_name

    @property
    def emp_salary(self):
        return self.__emp_salary

    @emp_salary.setter
    def emp_salary(self,val):
        self.__emp_salary=val

    def __str__(self):
        return f"ID: {self.__emp_id} Name: {self.__emp_name}, Salary: {self.__emp_salary}"
    
class Company:
    def __init__(self):
        self.__employees={}

    def add_employee(self,emp_id,name,sla):
        emp_obj=Employee(emp_id,name,sla)
        if emp_id in self.__employees:
            if emp_obj.emp_salary>self.__employees[emp_id].emp_salary:
                self.__employees[emp_id]=emp_obj

        self.__employees[emp_id]=emp_obj

    def search_employee(self,emp_id):
        if emp_id in self.__employees:
            return self.__employees[emp_id]

    def stats(self):
        total_employee=len(self.__employees)
        highest_salary=0
        total_salary=0
        for emp_id, emp_obj in self.__employees.items():
            total_salary+=emp_obj.emp_salary
            if highest_salary<emp_obj.emp_salary:
                highest_salary=emp_obj.emp_salary
        average_salary=total_salary/total_employee
        return (total_employee,highest_salary,average_salary)



class Interface:
    def __init__(self):
        self.__manage=Company()

    def option(self):
        print("1 add employee")
        print("2 search employee")
        print("3 stats")
        print("0 quit")

    def execute(self):
        self.option()
        while True:
            pick=input("Pick: ")
            if pick=="1":
                self.add_employee()
            if pick=="2":
                self.search_employee()
            if pick=="3":
                self.stats()
            if pick=="0":
                return
            
    def add_employee(self):
        emp_id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        slry = float(input("Enter Salary: "))
        self.__manage.add_employee(emp_id,name,slry)

    def search_employee(self):
        emp_id=int(input("Enter ID: "))
        obj=self.__manage.search_employee(emp_id)
        self.print_emp_detail(obj)

    def stats(self):
        tot_emp,hig_sal,avg_sal=self.__manage.stats()
        print(f"total employee: {tot_emp}")
        print(f"highest salary: {hig_sal}")
        print(f"average salary: {avg_sal}")

    def print_emp_detail(self,obj):
        print(obj)

app=Interface()
app.execute()
    