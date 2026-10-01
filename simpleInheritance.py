class Animal:

    def __init__(self,name):
        self.name=name

    def eat(self):
        print(self.name,"is eating")


class Dog(Animal):

    def bark(self):
        print(self.name,"is barking")



a1=Animal("jak")
d1=Dog("tom")

# print(a1)
# print(d1)

# a1.eat()
# d1.bark()
# d1.eat()
# a1.bark()

# print(isinstance(a1,Animal))
# print(isinstance(d1,Animal))

# print(issubclass(Animal,Dog))
print(issubclass(Dog,Animal))

