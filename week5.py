# Activity 1: Design Your Own Class!

# Smartphone class with attributes and methods
class Smartphone:
    def __init__(self, brand, model, battery_life):
        # Constructor to initialize object attributes
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in percentage

    def display_info(self):
        # Method to display smartphone information
        return f"Brand: {self.brand}, Model: {self.model}, Battery Life: {self.battery_life}%"

    def charge(self, amount):
        # Method to simulate charging the phone
        if self.battery_life + amount > 100:
            self.battery_life = 100
        else:
            self.battery_life += amount
        return f"Phone charged to {self.battery_life}%"

    def use(self, hours):
        # Method to simulate phone usage
        battery_drain = hours * 5  # Each hour drains 5% battery
        if self.battery_life - battery_drain < 0:
            self.battery_life = 0
        else:
            self.battery_life -= battery_drain
        return f"Phone used for {hours} hours. Battery now at {self.battery_life}%"

# To Create an instance of Smartphone
phone = Smartphone("Apple", "iPhone 14", 80)
print(phone.display_info())
print(phone.charge(15))
print(phone.use(4))

# Activity 2: Polymorphism Challenge!

# Base class Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclass Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Testing polymorphism
def test_move(vehicle):
    vehicle.move()

# Create instances of Car and Plane
car = Car()
plane = Plane()

# Test polymorphism
test_move(car)  # Outputs: Driving 🚗
test_move(plane)  # Outputs: Flying ✈️
