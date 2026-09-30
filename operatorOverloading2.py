class Data:
    def __init__(self,x):
        self.x=x


    def __add__(self, other):
        return self.x+other.x

    
num1=Data(3)
num2=Data(7)
print(num1+num2)
print(num1.__add__(num2))

str1=Data("md")
str2=Data("Rifat")

print(str1+str2)