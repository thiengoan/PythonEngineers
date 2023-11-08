class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age
       
    def info(self):
        print('Name: {} , Age: {}'.format(self.name,self.age))

class Employer(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary
       
    def info(seft):
        Person.info(self)
        print('Salary: {} '.format(self.salary))

a = Employer('Ngoan',21)

print(a.info())

b = Employer('Tuan',30,2000)
print(b.salary)