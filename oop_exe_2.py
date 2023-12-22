class Student():
    age = 20

    def __init__(self,name,last,gpa):
        self.name = name
        self.last = last
        self.gpa = gpa

    def display_name(self):
        return(f"Student's full name: {self.name} {self.last}")    

    @classmethod
    def create_student(cls,str1):
        name,last,gpa = str1.split("-")
        return(cls(name,last,gpa))

    @classmethod
    def change_age(cls,new_age):
        cls.age = new_age
    

    def __str__(self):
        return(f"{self.display_name()} - {self.gpa}")


djokica = Student("Novak","Djokovic",'9.60')
print(djokica.display_name())

rafa = Student.create_student("Rafael-Nadal-9.20")
print(rafa)
print(djokica)

Student.change_age(22)
print(Student.age)