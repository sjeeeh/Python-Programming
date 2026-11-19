class Publisher:
    def __init__(self, pid, pname):
        self.pid = pid
        self.pname = pname
    def display(self):
        print(f"Publisher ID   : {self.pid}")
        print(f"Publisher Name : {self.pname}")

class Book(Publisher):
    def __init__(self, pid, pname, title, author):
        super().__init__(pid, pname)
        self.title = title
        self.author = author
    def display(self):
        super().display()
        print(f"Title          : {self.title}")
        print(f"Author         : {self.author}")

class Python(Book):
    def __init__(self, pid, pname, title, author, price, no_of_pages):
        super().__init__(pid, pname, title, author)
        self.price = price
        self.no_of_pages = no_of_pages
    def display(self):
        print("\n----- Python Book Details -----")
        super().display()
        print(f"Price          : {self.price:.2f}")
        print(f"No. of Pages   : {self.no_of_pages}")
        print("-------------------------------\n")


book = Python(101, "ABC Publishers", "Pyhton Programming", "John", 450.0, 300)
book.display()
