from multipledispatch import dispatch

class my_calculator:
    
    @dispatch(int,int)
    def product(self,a,b):
        print(a*b)


    @dispatch(int,str)
    def product(self,a,b):
        print(a*int(b))


c1=my_calculator()

c1.product(2,5)