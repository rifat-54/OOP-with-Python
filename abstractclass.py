from abc import ABC,abstractmethod

class A(ABC):

    @abstractmethod
    def method1(self):
        pass

class B(A):

    @abstractmethod
    def method2(self):
        pass


class C(B):

    def method1(self):
        print("method1 is over ridding")

    def method2(self):
        print("method2 is over ridding")
    
    def method3(self):
        print("Method 3")


# a=A()
# b=B()
# b.method1()

c=C()
c.method1()
c.method2()
