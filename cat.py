class Cat:
    def __init__(self,name,action):
        self.name=name
        self.action=action

    def view(self):
        print(self.name," is ",self.action)

    def compare(self,ct):
        print("self-=> ",self)
        print("compaer-> ",ct)
        if(self.action==ct.action):
            print("Both are same")
        else:
            print("they are different")


cat1=Cat("tom","jumping")
cat2=Cat("jak","laying")

print(cat1,cat2)

cat1.view()
cat2.view()

cat2.action="jumping"

cat1.compare(cat2)