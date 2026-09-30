class Info:

    def __init__(self,*pa):
        if(len(pa)==3):
            self.name=pa[0]
            self.id=pa[1]
            self.CGPA=pa[2]
        if(len(pa)==2):
            self.name=pa[0]
            self.id=pa[1]

        if(len(pa)==1):
            self.name=pa[0]


# s1=Info("rakib",23,2.5)
# s1=Info("nakib",23)
# s1=Info("sakib")

class Info2:

    def __init__(self,**pa):
        if(len(pa)==3):
            self.name=pa['name']
            self.id=pa['id']
            self.CGPA=pa['cgpa']
        if(len(pa)==2):
            self.name=pa['name']
            self.id=pa['id']


        if(len(pa)==1):
            self.name=pa['name']
       


s1=Info2(name="rakib",id=23,cgpa=2.5)
s2=Info2(name="sakib",id=53)
s3=Info2(name="nakib")

print(s2.name)



