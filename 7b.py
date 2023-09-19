#Write a python program by creating a class called Employee to store the details of Name, Employee_ID, Department and Salary, and implement a method to update salary of employees belonging to a given department.

class Employee:
  def __init__(self, name, employee_id, department, salary):
    self.name = name
    self.employee_id = employee_id
    self.department = department
    self.salary = salary

  def display_details(self):
    print("Employee Name: ",self.name)
    print("Employee ID: ",self.employee_id)
    print("Employee Department: ",self.department)
    print("Employee Salary: ",self.salary)
    print()

  def update_salary(self, department, new_salary):
    if self.department == department:
      self.salary = new_salary

e1 = Employee("Anil Kumar","CITCSE004","CSE",10000)
e2 = Employee("Sunil Kumar","CITISE005","ISE",20000)
e3 = Employee("Hari","CITME006","ME",5000)

e1.display_details()
e2.display_details()
e3.display_details()

department = "CSE"
new_salary = 20000

e1.update_salary(department,new_salary)

if e2.department == "ISE":
  e2.salary = 30000

e1.display_details()
e2.display_details()
e3.display_details()

