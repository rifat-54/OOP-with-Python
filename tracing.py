class Trace:
    def __init__(self):
        self.sum=0
        self.y=0

    def methodA(self):
        x=2
        y=3
        msg=[0]
        y=self.y+msg[0]
        self.methodB(msg,msg[0])
        x=self.y+msg[0]
        self.sum=x+y+self.sum
        print(x,y,self.sum)

    def methodB(self,ls,value):
        x=0
        self.y=self.y+ls[0]
        x=x+3+value
        self.sum=self.sum+x+self.y
        ls[0]=self.y+value
        value=value+x+2
        print(x,self.y,self.sum)


t2=Trace()

t2.methodA()
t2.methodA()
