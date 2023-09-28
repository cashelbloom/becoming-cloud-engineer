# In hr.py

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass

'''
This change has two nice side-effects:

You’re telling users of the module that objects of type Employee can’t be created.
You’re telling other developers working on the hr module that 
if they derive from Employee, then they must override the .calculate_payroll() abstract method.
'''