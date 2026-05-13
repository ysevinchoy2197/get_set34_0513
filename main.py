#4-misol
class Teacher:
    def __init__(self, fullname, salary):
        self.fullname = fullname
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.__salary = new_salary

t1 = Teacher('Azamat', 500)

print(t1.fullname)
print(t1.get_salary())
