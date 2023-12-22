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

    def __repr__(self):
        return("Employee ('{}','{}',{})".format(self.first,self.last,self.pay))    

    def __str__(self):
        return("{} - {}".format(self.full_name(),self.email))

    def __add__(self,other):
        return self.pay + other.pay   

    def __len__(self):
        return(len(self.full_name()))       

emp_1 = Employee("Vladimir","Cakic",150000)
emp_2 = Employee("Dejan","Cojic",120000)
print(emp_1)

print(emp_1 + emp_2)
print(len(emp_1))