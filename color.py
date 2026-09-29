class Color:
    def __init__(self,name):
        self.name=name

    def view(self,num,clr):
        print(clr)
        num=num+5
        clr1=clr
        clr1[1]="tomatto"

        print("Method inside: num: ",num) 
        print("Method inside: color: ",clr1) 


c1=Color("ketton")

x=3

color=["green","blue","yellow","pink"]

c1.view(x,color)

print("Method outside color: ",color)
print("Method outside x: ",x)