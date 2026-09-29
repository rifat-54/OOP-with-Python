class Student:

    def __init__(self,name,Id):
        print(self)
        self.name=name
        self.id=Id
        print("a object created!")
    def details(self):
        print("Name : ",self.name,"Id: ",self.id)


ob1=Student("steven",43)
ob2=Student("jak",22)

# print(ob1.id)
# ob1.id=65

# print(ob1.id)

# print("ob1->",ob1)
# print("ob2->",ob2)

ob1.details()
ob2.details()



