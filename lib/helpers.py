from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    #use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')
    


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    employee_name = input('Please enter the employee name: ')
    employee = Employee.find_by_name(employee_name)
    print(employee) if employee else print(
        f'Employee {employee_name} not found')


def find_employee_by_id():
    employee_id = int(input('Please enter the employee ID: '))
    employee = Employee.find_by_id(employee_id)
    print(employee) if employee else print(
        f'Employee {employee_id} not found')
    

def create_employee():
    new_name = input('Please enter the new employee name: ')
    new_job_title = input('Please enter the new employee job title: ')
    new_department_id = int(input('Please enter the department ID: '))
    try:
        new_employee = Employee.create(new_name, new_job_title, new_department_id)
        print(f'Success: {new_employee}')
    except Exception as exc:
        print('Error creating employee: ', exc)


def update_employee():
    id_ = int(input('Please enter the id of the employee: '))
    if employee := Employee.find_by_id(id_):
        try:
            new_name = input('Please enter the new employee name: ')
            employee.name = new_name
            new_job_title = input('Please enter the new employee job title: ')
            employee.job_title = new_job_title
            new_department_id = int(input('Please enter the department ID: '))
            employee.department_id = new_department_id

            employee.update()
            print(f'Success: {employee}')
        except Exception as exc:
            print('Error updating employee: ', exc)
    else:
        print(f'Employee {id_} not found')


def delete_employee():
    id_ = int(input('Please enter the id of the employee: '))
    if employee := Employee.find_by_id(id_):
        employee.delete()
        print(f'Employee {id_} deleted')


def list_department_employees():
    department_id = int(input('Please enter the department ID: '))
    department = Department.find_by_id(department_id)
    if department:
        employees = Employee.get_all()
        dept_employees = list(filter(lambda employee: employee.department_id == department_id, employees))
        
        for employee in dept_employees:
                print(employee)
    else:
        print(f'Department {department_id} not found')
            
   

