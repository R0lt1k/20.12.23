class Car:
    def __init__(self):
        self.model = ""
        self.year = 0
        self.manufacturer = ""
        self.engine_volume = 0.0
        self.color = ""
        self.price = 0.0

    def input_data(self):
        self.model = input("Enter the model name: ")
        self.year = int(input("Enter the year of manufacture: "))
        self.manufacturer = input("Enter the manufacturer: ")
        self.engine_volume = float(input("Enter the engine volume: "))
        self.color = input("Enter the car color: ")
        self.price = float(input("Enter the price: "))

    def output_data(self):
        print("Model:", self.model)
        print("Year of manufacture:", self.year)
        print("Manufacturer:", self.manufacturer)
        print("Engine volume:", self.engine_volume)
        print("Car color:", self.color)
        print("Price:", self.price)

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_engine_volume(self):
        return self.engine_volume

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def set_model(self, model):
        self.model = model

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


if __name__ == "__main__":
    car1 = Car()
    car1.input_data()

    print("Car data:")
    car1.output_data()

    print("Year of manufacture:", car1.get_year())
    print("Car color:", car1.get_color())
