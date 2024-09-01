import json
import random
from classes.Book import Book

booklist = json.load(open("books.json", "r"))

for bookinfo in booklist:
    book = Book(bookinfo["title"], bookinfo["author"], bookinfo["pages"], random.randint(100, 1000))
    print(f"[{book.formatPrice()}] {book.title} ({book.author})")