class Book:
    def __init__(self):
        self.title = ""
        self.year = 0
        self.publisher = ""
        self.genre = ""
        self.author = ""
        self.price = 0.0

    def input_data(self):
        self.title = input("Enter the book title: ")
        self.year = int(input("Enter the publication year: "))
        self.publisher = input("Enter the publisher: ")
        self.genre = input("Enter the genre: ")
        self.author = input("Enter the author: ")
        self.price = float(input("Enter the price: "))

    def output_data(self):
        print("Title:", self.title)
        print("Publication Year:", self.year)
        print("Publisher:", self.publisher)
        print("Genre:", self.genre)
        print("Author:", self.author)
        print("Price:", self.price)

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

    def set_title(self, title):
        self.title = title

    def set_year(self, year):
        self.year = year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def set_genre(self, genre):
        self.genre = genre

    def set_author(self, author):
        self.author = author

    def set_price(self, price):
        self.price = price


if __name__ == "__main__":
    book1 = Book()
    book1.input_data()

    print("Book data:")
    book1.output_data()

    print("Publication Year:", book1.get_year())
    print("Author:", book1.get_author())

    book1.set_price(19.99)
    print("Modified price:", book1.get_price())
