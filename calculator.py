class Calculator:

    # def multi(self,n1,n2=None,n3=None):

    #     if n1!=None and n2!=None and n3!=None:
    #         print(n1*n2*n3)
    #     elif n1!=None and n2!=None:
    #         print(n1*n2)
    #     else:
    #         print(n1)

    def multi(self,*num):
        print(num)
        print(type(num))
        sum=1
        for x in num:
            sum=sum*x

        print(sum)




c1=Calculator()

c1.multi(2)
c1.multi(2,3)
c1.multi(2,3,4)
c1.multi(2,3,4,5)