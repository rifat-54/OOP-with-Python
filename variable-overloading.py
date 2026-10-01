class Animal:
    def __init__(self,name):
        self.name=name
        self.color="White"
        print(self.color,self.name,"is jumping")

    def eat(self):
        print(self.color,self.name,"is eating")

    def method1(self):
        print("Aleays working")


class Dog(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color=color
        print(self.color,self.name,"is jumping")

    def bark(self):
        print(self.color,self.name,"is barking")

    def method1(self):
        super().method1()
        print("always eating")


d1=Dog("jak","brown")
d1.method1()

# d1.bark()
# d1.eat()