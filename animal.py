class Animal:
    def __init__(self,name,color,pok):
        self.name=name
        self.color=color
        self.pok=pok
        self.alive=True
        
    def update_color(self,color):
        self.color=color

    def poke(self):
        print(self.color," ",self.name," is ",self.pok)

dog=Animal("dog","black","gew gew")
cat=Animal("cat","gray","mew mew")

dog.update_color("white") 

dog.poke()
cat.poke()

# print(dog.__dict__)
# print(dir(dog))