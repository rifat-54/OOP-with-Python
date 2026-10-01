class Student:

    def __init__(self,name,id):
        # print(self)
        self.name=name
        self.id=id

    def details(self):
        print("Name: ",self.name,", Id: ",self.id)


class Cse(Student):
    def __init__(self,name,id,labs):
        # print(self)
        super().__init__(name,id)
        self.labs=labs

    def cry(self):
        print("Cse, they are crying")


class BBA(Student):

    def party(self):
        print("BBA, they are doing party")

s1=Cse("rifat",23,5)
s2=BBA("Daku",34)

s1.details()
s2.details()

s1.cry()
s2.party()

