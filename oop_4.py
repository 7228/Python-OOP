class Employee():
    raise_amnt = 1.04
    num_of_emps = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    #Helps us access the function like it was an atribute(without parentheses):
    @property
    def email(self):
        return("{}.{}.@company.com".format(self.first,self.last))

    @property
    def full_name(self):
        return("{} {}".format(self.first,self.last))

    @full_name.setter
    def full_name(self,name):
        first,last = name.split()
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        print("Name deleted!")
        self.first = None
        self.last = None

emp_1 = Employee("Vladimir","Cakic",150000)
print(emp_1.email)        
print(emp_1.full_name)

emp_1.full_name = "Vladimir Putin"
print(emp_1.full_name)
print(emp_1.email)

del emp_1.full_name

