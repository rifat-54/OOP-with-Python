class Employee():
    org_name="Google"

    def __init__(self,name):
        self.name=name
        print(self.name," in now ->",self.org_name)


    @classmethod
    def info(cls):
        return cls.org_name

    @staticmethod
    def details():
        print("Rifat is now on fire")


print(Employee.info())
Employee.details()

p1=Employee("rifat")