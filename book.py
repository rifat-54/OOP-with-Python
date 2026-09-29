class Book:

    def __init__(self,name,author):
        self.name=name
        self.author=author
        self.price=0

    def set_price(self,price):
        self.price=price

    def get_price(self):
        return self.price

    def details(self):
        print("Book Name: ",self.name,
             "\nAuthor: ",self.author,
             "\nPrice: ",self.price," Taka.")


b1=Book("nam nai","rifat")
b1.set_price(655)

b1.details()
        