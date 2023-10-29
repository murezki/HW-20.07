class Stadium:
    def __init__(self,name, year, country, city, capacity):
        self.name = name
        self.year = year
        self.country = country
        self.city = city
        self.capacity = capacity

    def set_name(self, name):
        self.name = name

    def set_year(self, year):
        self.year = year

    def set_country(self, country):
        self.country = country

    def set_city(self, city):
        self.city = city

    def set_capacity(self, capacity):
        self.capacity = capacity

    def get_name(self):
        print(self.name)

    def get_year(self):
        print(self.year)

    def get_country(self):
        print(self.country)

    def get_city(self):
        print(self.city)

    def get_capacity(self):
        print(self.capacity)


stadium = Stadium("ыавфы", "2000", "США", "Сан Диего", "20000")
stadium.get_capacity()
stadium.set_capacity(21000)
stadium.get_capacity()