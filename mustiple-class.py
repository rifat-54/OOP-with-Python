class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id


class Dummy:
    def __init__(self):
        self.val=0

    def details(self,std):
        self.val=std
        std.val=234


# ====================================================================================
s1=Student("jak",23)
d1=Dummy()

d1.details(s1)

# print(d1.val)
# print(d1.val.name)
print(d1.val.id)

print(d1.val.val)

# print(s1.val)