class Data:
    def __init__(self,x,y):
        self.x=x
        self.__y=y

    def get_data(self):
        print(self.__y)
        # return self.__y
        self.__pmeth()

    def __pmeth(self):
        print("Private method called!!")

d1=Data(23,5)

# print(d1.__y)
# d1.pmeth()

# print(d1.get_data())

d1.get_data()