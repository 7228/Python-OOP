from matplotlib.pyplot import cla


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


class Developer(Employee):
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        
        self.prog_lang = prog_lang


dev_1 = Developer("Nikola","Zigic",100000,'Javascript')
dev_2 = Developer("Milos","Krasic",100000,"Python")
print(dev_1.prog_lang) 
print(dev_1.raise_amnt)       

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)

        if employees is None:  
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def staff(self):
        for x in self.employees:
            print("-->",x.full_name())

    def emp_pay(self):
        for x in self.employees:
            print("{} : {}$".format(x.full_name(),x.pay))        


Vlada = Manager("Vladimir","Cakic",150000,[dev_1,dev_2])
Vlada.staff()

dev_3 = Developer("Suzana","Suzic",13000,"C++")

Vlada.add_emp(dev_3)
Vlada.staff()

Vlada.emp_pay()

print(isinstance(Vlada,Manager))
print(isinstance(Vlada,Employee))
print(isinstance(Vlada,Developer))

print(issubclass(Manager,Developer))
print(issubclass(Manager,Employee))

