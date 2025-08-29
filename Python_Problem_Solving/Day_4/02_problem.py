#Library Management 📚

'''Create a Book class with attributes title, author, available_copies.
Method: borrow_book(), return_book()
If no copies left, print "Not available".
'''

class Book:
    def __init__(self,title, author, available_copies):
        self.title = title
        self.author = author
        self.available_copies = available_copies

    def borrow_book(self):
        if(self.available_copies > 0):
            self.available_copies -= 1
            print(f"Borrowed book: {self.title} by {self.author}")
        else:
            print("Not available")
    
    def return_book(self):
        self.available_copies += 1
        print(f"Returned book: {self.title} by {self.author}")

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10)
book1.borrow_book()
book1.borrow_book()
book1.return_book()