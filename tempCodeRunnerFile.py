class Car:
    def __init__(self,model,year):
        self.mode=model
        self.year=year
        self.wheel=4

    def view(self):
        print(self.mode,self.year,"wheel: ",self.wheel)


car1=Car("auto",3050)
car1.wheejhldfg=8
car1.view()
