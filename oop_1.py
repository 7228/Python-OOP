class Employee():
    raise_amnt = 1.04
    num_of_emps = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = self.first + self.last + "@company.com"
        self.pay = pay

        Employee.num_of_emps += 1

    def full_name(self):
        return("{} {}".format(self.first,self.last))

    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amnt)
        return(self.pay)

    @classmethod
    def set_raise_amnt(cls,amount):
        cls.raise_amnt = amount    


    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split("-")
        return(cls(first,last,pay))

    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True        


employee_1 = Employee("Vladimir","Cakic",1500)
employee_2 = Employee("Momir","Ilic",2000)

print(employee_1.full_name())
print(employee_1.email)
print(employee_1.pay_raise())
print(Employee.num_of_emps)
print(Employee.raise_amnt)
Employee.set_raise_amnt(1.06)
print(Employee.raise_amnt)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp = Employee.from_string(emp_str_1)
print(new_emp.first)
print(Employee.num_of_emps)

import datetime
my_date = datetime.date(2022,6,19)
print(Employee.is_work_day(my_date))