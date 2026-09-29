class House:
    def __init__(self):
        self.window=4
        self.door=2

    def view(self):
        print("house has: ",self.door," door and: ",self.window," window")


h1=House()
h2=House()

h1.door=5
h2.window=8

h1.view()
h2.view()