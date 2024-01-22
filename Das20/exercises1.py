# Write an abstract class with name Employee
# Write 2 employee classes by inheriting from abstract Employee
# Write function
# get_info -> return string with name and position
# calculate_salary -> return float with information about employee salary.
from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def get_info(self):
        pass
    @abstractmethod
    def calculate_salary(self):
        pass
class Banker(Employee):
    def __init__(self,salary,name,position) :
        self.__salary=salary
        self.__name=name
        self.__position=position
    def get_info(self):
        return f"{self.__name} is {self.__position}"
    def calculate_salary(self):
        return f"Artur salary is {self.__salary}"
k=Banker(200000,"Artur","Bank Manager")
print(k.get_info())
print(k.calculate_salary())
class Programmer(Employee):
    def __init__(self,name,position,salary,interest=15) :
        self.__name=name
        self.__position=position
        self.__salary=salary
        self.__interest=interest
    def get_info(self):
        return f"{self.__name} is {self.__position}"
    def calculate_salary(self):
        if self.__salary>0:
            print(f"{self.__name} is salary {self.__salary}")
            self.__salary+=self.__salary/100*self.__interest
            return f"Salary and interest =={self.__salary}"
empoyee=Programmer("Sargis","junior python developer",200000)           
print(empoyee.get_info())
print(empoyee.calculate_salary())
