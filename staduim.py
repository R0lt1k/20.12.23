class Stadium:
    def __init__(self):
        self.name = ""
        self.opening_date = ""
        self.country = ""
        self.city = ""
        self.capacity = 0

    def input_data(self):
        self.name = input("Enter the stadium name: ")
        self.opening_date = input("Enter the opening date: ")
        self.country = input("Enter the country: ")
        self.city = input("Enter the city: ")
        self.capacity = int(input("Enter the seating capacity: "))

    def output_data(self):
        print("Stadium Name:", self.name)
        print("Opening Date:", self.opening_date)
        print("Country:", self.country)
        print("City:", self.city)
        print("Seating Capacity:", self.capacity)

    def get_name(self):
        return self.name

    def get_opening_date(self):
        return self.opening_date

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity

    def set_name(self, name):
        self.name = name

    def set_opening_date(self, opening_date):
        self.opening_date = opening_date

    def set_country(self, country):
        self.country = country

    def set_city(self, city):
        self.city = city

    def set_capacity(self, capacity):
        self.capacity = capacity


if __name__ == "__main__":
    stadium1 = Stadium()
    stadium1.input_data()

    print("Stadium data:")
    stadium1.output_data()

    print("Country:", stadium1.get_country())
    print("Seating Capacity:", stadium1.get_capacity())

    stadium1.set_name("New Stadium")
    print("Modified Stadium Name:", stadium1.get_name())
