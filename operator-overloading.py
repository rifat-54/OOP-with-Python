# class Data:
#     def __init__(self,x):
#         self.x=x


#     def __add__(self, other):
#         return self.x+other.x


# n1=Data(10)
# n2=Data(20)

# print(n1+n2)


# class Data:
#     def __init__(self,x):
#         self.x=x


#     def __gt__(self, other):
#         if(self.x>other.x):
#             return True
#         else:
#             return False


# n1=Data(10)
# n2=Data(20)

# print(n1>n2)


class Data:
    def __init__(self,x):
        self.x=x


    def __lt__(self, other):
        if(self.x<other.x):
            return True
        else:
            return False


n1=Data(10)
n2=Data(20)

print(n1<n2)