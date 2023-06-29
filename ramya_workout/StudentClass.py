class Student:
    def __int__(self, name, grade):
        self.name = name
        self.grade = grade

    def avg(self):
        return sum(self.grade)/len(self.grade)

student_one = Student('Ramya')
print(student_one.name)
