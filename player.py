class Player:

    def __init__(self,name,id):
        # print(self)
        self.name=name
        self.id=id

    def details(self):
        print("name: ",self.name,"id: ",self.id)
 


p1=Player("rakib",34)
print(p1)

p1.details()