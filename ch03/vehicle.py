class Vehicle:
    """Base class for all vehicles"""

    def __init__(self, name, manufacturer, color):
        print("Creating a vehicle")
        self.name = name
        self.manufacturer = manufacturer
        self.color = color


class Car(Vehicle):
    """Car class"""

    def __init__(self, name, manufacturer, color, year):
        print("Creating a car")
        super().__init__(name, manufacturer, color)
        self.year = year
        self.wheels = 4


if __name__ == "__main__":
    c = Car("Mustang GT", "Ford", "Red", 2024)
    print(c.name, c.year, c.wheels)
