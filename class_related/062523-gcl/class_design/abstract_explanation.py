from abc import *

class MyAbstractEmployee(ABC):

    @abstractmethod
    def calc_payroll(self):
        pass


class MySalariedEmployee(MyAbstractEmployee):
    def __init__(self, hourly_rate, num_hours):
        self.hourly_rate = hourly_rate
        self.num_hours = num_hours

    def calc_payroll(self):
        # print(f'This is the hourly rate: {self.hourly_rate}')
        # print(f'Your salary for this period is: {self.hourly_rate * self.num_hours}')
        return (self.hourly_rate * self.num_hours)

my_salaried_employee = MySalariedEmployee(60, 30)
print(f'The salary for 1st employee is: {my_salaried_employee.calc_payroll()}')

my_salaried_employee2 = MySalariedEmployee(80, 20)
print(f'The salary for 2nd Employee is: {my_salaried_employee2.calc_payroll()}')
