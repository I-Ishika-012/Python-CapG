'''
employee->name , salary
child class: manager->name, salary, dept
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, dept):
        super().__init__(name, salary)
        self.dept = dept
        
    def display(self):
        super().display()
        print(f"Department: {self.dept}")
        

emp = Employee("John Doe", 50000)
emp.display()

mgr = Manager("Jane Doe", 60000, "Sales")
mgr.display()