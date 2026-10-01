class Student:
    def __init__(self,name,id):
        self.name=name 
        self.id=id
        # print(self)

    def __str__(self):
        return "hi, i am "+self.name

s1=Student("rifat",34)
s2=Student("jak",64)

# print(s1.__str__())
print(s2)