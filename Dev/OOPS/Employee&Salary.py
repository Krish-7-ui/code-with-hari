class Employee():
    def __init__(self,id,name,salary=0):
        self.id = id
        self.name = name
        self.salary = salary

class FulltimeEmployee(Employee):
    def __init__(self,id,name,fixed_salary):
        super().__init__(id,name,fixed_salary)

    def calculate_Salary(self):
        return self.salary

class ParttimeEmployee(Employee):
    def __init__(self,id,name, hourly_rate, hourly_worked):
        super().__init__(id,name)
        self.hourly_rate = hourly_rate
        self.hourly_worked = hourly_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hourly_worked

Fte = FulltimeEmployee(1,"Hari",60000)
Pte = ParttimeEmployee(2,"Pavi",20,90)

print (Fte.calculate_Salary())
print (Pte.calculate_salary())