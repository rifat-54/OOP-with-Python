class Student:
    uni_name="T-Nu"

    def __init__(self,name,id):
        self.name=name
        self.id=id

    def details(self):
        # print("self",self)
        print("Name: ",self.name,", Id: ",self.id,
              "\nUni Name: ",Student.uni_name)

    @classmethod
    def up_uni(cls,uName):
        # print("cls",cls)
        # print(self)
        cls.uni_name=uName

    @classmethod
    def from_string(cls,info):
        # print(info.split("-"))
        name,id=info.split("-")
        obj=cls(name,id)
        return obj


s1=Student("jak",12)
print(s1)
s2=Student.from_string("lusy-34")
print(s2)

s1.details()
print("==================================================================")
s2.details()

# # Student.up_uni("iut")
# s1.up_uni("iut")

# s1.details()
# s2.details()
# print(s1.__dict__)

