class Student:
    uni_name="T-Nu"

    def __init__(self,name,id):
        self.name=name
        self.id=id

    def details(self):
        # print("self",self)
        print("Name: ",self.name,", Id: ",self.id,
              "\nUni Name: ",Student.uni_name)

    @staticmethod
    def check_departmant(Id):
        if(Id[2:4]=="01"): print("CSE")
        elif(Id[2:4]=="23"):print("CS")



Student.check_departmant("21016456")
Student.check_departmant("202364565")

# s1=Student("jak",12)

# s2=Student.from_string("lusy-34")



