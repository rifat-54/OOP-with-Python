class A:
    print("Class A called")
    def __init__(self):
        print("_init_ of class A")

    def method1(self):
        print("Method of class A")

class B:
    def __init__(self):
        print("_init_ of class B")

    def method1(self):
        print("Method of class B")

    def method3(self):
        print("method3 of class B")

class C(A,B):
    def __init__(self):
        # super().__init__()
        B.__init__(self)
        print("_init_ of class C")

    def method2(self):
        print("method2 of class C")

c1=C()
c1.method3()
B.method3(c1)