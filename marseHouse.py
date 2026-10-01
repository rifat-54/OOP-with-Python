class House:
    def __init__(self,w,d):
        self.window=w
        self.door=d


    def view(self):
        print("The house has",self.window,"window and",self.door,"door")

    def __add__(self, other):
        nw=self.window+other.window
        nd=self.door+other.door
        obj=House(nw,nd)
        return obj


h1=House(3,2)
h2=House(6,4)

# h1.view()

# print(h1+h2)
h3=h1+h2

h3.view()
