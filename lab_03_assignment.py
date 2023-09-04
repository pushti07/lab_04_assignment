class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"

# Define custom functions for sorting
def sort_by_age(emp):
    return emp.age

def sort_by_name(emp):
    return emp.name

def sort_by_salary(emp):
    return emp.salary

def sort_employee_data(employee_list, key):
    if key == 1:
        return sorted(employee_list, key=sort_by_age)
    elif key == 2:
        return sorted(employee_list, key=sort_by_name)
    elif key == 3:
        return sorted(employee_list, key=sort_by_salary)
    else:
        return employee_list

def main():
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000)
    ]

    print("Employee Table")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    try:
        choice = int(input("Enter sorting parameter (1/2/3): "))
        if choice < 1 or choice > 3:
            raise ValueError("Invalid choice")
    except ValueError:
        print("Invalid input. Please enter a valid choice (1/2/3)")
        return

    sorted_employees = sort_employee_data(employees, choice)

    print("Sorted Employee Data:")
    for employee in sorted_employees:
        print(employee)

if __name__ == "__main__":
    main()
