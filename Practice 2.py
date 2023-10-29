class Book:
    def __init__(self,name, year, manufacturer, genre, author, price):
        self.name = name
        self.year = year
        self.manufacturer = manufacturer
        self.genre = genre
        self.author = author
        self.price = price

    def set_name(self, name):
        self.name = name

    def set_year(self, year):
        self.year = year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def set_genre(self, genre):
        self.genre = genre

    def set_author(self, author):
        self.author = author

    def set_price(self, price):
        self.price = price

    def get_name(self):
        print(self.name)

    def get_year(self):
        print(self.year)

    def get_manufacturer(self):
        print(self.manufacturer)

    def get_genre(self):
        print(self.genre)

    def get_author(self):
        print(self.author)

    def get_price(self):
        print(self.price)

book = Book("ыфвф", "2019", "рухани жангыру", "научная фантастика", "том сойер", "2000")
book.get_author()
book.set_author("шавкат рахманов")
book.get_author()