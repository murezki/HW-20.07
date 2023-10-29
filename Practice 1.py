class Car:
    def __init__(self, model_name, year, manufacturer, engine_volume, color, price):
        self.model_name = model_name
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def set_model_name(self, model_name):
        self.model_name = model_name

    def set_year(self, year):
        self.year = year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def set_engine_volume(self, engine_volume):
        self.engine_volume = engine_volume

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price

    def get_model_name(self):
        print(self.model_name)

    def get_year(self):
        print(self.year)

    def get_manufacturer(self):
        print(self.manufacturer)

    def get_engine_volume(self):
        print(self.engine_volume)

    def get_color(self):
        print(self.color)

    def get_price(self):
        print(self.price)

car = Car("тойота камри", 2020, "тойота", "2.5 L", "белый", "22 млн")
car.set_year(2021)
car.set_price("24 млн")
car.get_year()
car.get_price()