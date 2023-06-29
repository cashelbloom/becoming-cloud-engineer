class Student:
    def __int__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

class WorkingStudent(Student):
    def __init__(self,name,school,salary):
        super()
        # self.name = name
        # self.school = school
        self.marks = []
        self.salary = salary

    # def average(self):
    #     return sum(self.marks)/len(self.marks)

    @property
    def weekly_salary(self):
        return self.salary * 37.5

rolf = WorkingStudent('Rolf', 'MIT', 15.50)
print(rolf.salary)
rolf.marks.append(57)
rolf.marks.append(99)
rolf.marks.append(100)
print(rolf.average())
# print(rolf.weekly_salary())
print(rolf.weekly_salary)