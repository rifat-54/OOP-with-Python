class Student:
    uni_name="T-Nu"

    def __init__(self,name,id):
        self.name=name
        self.id=id

    def details(self):
        print("self",self)
        print("Name: ",self.name,", Id: ",self.id,
              "\nUni Name: ",self.uni_name)

    @classmethod
    def up_uni(cls,uName):
        print("cls",cls)
        # print(self)
        cls.uni_name=uName


s1=Student("jak",12)
s2=Student("lusy",34)

s1.details()
s2.details()
print("==================================================================")

# Student.up_uni("iut")
s1.up_uni("iut")

s1.details()
s2.details()
print(s1.__dict__)

