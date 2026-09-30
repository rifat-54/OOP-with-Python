class Student:

    def __init__(self,name,id):
        self.name=name
        self.__id=id

    def view(self):
        print("Name: ",self.name,"Id: ",self.__id)

    def upd_id(self,id):
        if(id>0):
            self.__id=id
        else:
            print("Invaid id")


s1=Student("rifat",32)
s2=Student("jak",56)

# s1.__id="sdf"

# print(s1.__dict__)

s1.upd_id(-78)

s1.view()
s2.view()