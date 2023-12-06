employee_number = int(input("Enter employee's number: "))
employee_name = input("Enter employee's name: ")
employee_department = input("Enter employee's department: ")

# file = open('employee-record.txt', 'w')
file = open('employee-record.txt', 'a')

file.writelines([f"Employee's number: {employee_number}\n",
                 f"Employee's name: {employee_name}\n",
                 f"Employee's department: {employee_department}\n\n"])

file.close()
