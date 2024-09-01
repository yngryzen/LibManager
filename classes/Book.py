class Book:
    def __init__(self, title, author, stock, price):
         self.title = title
         self.author = author
         self.stock = stock
         self.price = price

    def formatPrice(self):
         return f"£{(self.price / 100):.2f}"