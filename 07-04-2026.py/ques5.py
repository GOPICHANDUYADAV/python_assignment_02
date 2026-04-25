#employee management (inheritance)
class Employee:
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class Manager(Employee):
    def __init__(self, name, emp_id, base_salary, bonus):
        super().__init__(name, emp_id, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


class Developer(Employee):
    def __init__(self, name, emp_id, base_salary, project_count):
        super().__init__(name, emp_id, base_salary)
        self.project_count = project_count

    def calculate_salary(self):
        return self.base_salary + 500 * self.project_count


# Test
employees = [
    Manager("Alice", "M001", 80000, 10000),
    Developer("Bob", "D001", 70000, 3)
]

total = 0
for emp in employees:
    total += emp.calculate_salary()

print("Total Payroll:", total)