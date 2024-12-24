class Employee():
    def __init__(self,employee_id,name,salary):
        self.__employee_id = employee_id
        self.__name = name
        self.__salary = salary
    def set_id(self,employee_id):
        self.__employee_id = employee_id
    def get_id(self):
        return self.__employee_id
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_salary(self,salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary cant be negative!")
    def get_salary(self):
        return self.__salary


employee = Employee(1114,"Ann",1500)
employee.set_salary(-1200)
print(employee.get_name())
print(employee.get_salary())
employee.set_salary(400)
print(employee.get_salary())
