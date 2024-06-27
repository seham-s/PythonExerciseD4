class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager:
    def __init__(self, department):
        self.department = department

class Executive(Employee, Manager):
    def __init__(self, name, salary, department, company_car, bonus):
        Employee.__init__(self, name, salary)
        Manager.__init__(self, department)
        self.company_car = company_car
        self.bonus = bonus
    
    def __str__(self):
        return (f"Executive Information:\n"
                f"Name: {self.name}\n"
                f"Salary: {self.salary}\n"
                f"Department: {self.department}\n"
                f"Company Car: {self.company_car}\n"
                f"Bonus: {self.bonus}")

# Example usage:
executive = Executive('John Doe', 120000, 'IT', 'BMW X5', 15000)
print(executive)