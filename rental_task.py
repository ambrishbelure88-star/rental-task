class Vehicle:
    def __init__(self, vehicle_number, brand, rental_price):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.rental_price = rental_price

    def display_details(self):
        print(self.vehicle_number)
        print(self.brand)
        print(self.rental_price)

    def calculate_rental(self, days):
        return self.rental_price * days
    
class Car(Vehicle):
    def __init__(self, vehicle_number, brand, rental_price, seats):
        super().__init__(vehicle_number, brand, rental_price)
        self.seats = seats
        
class Bike(Vehicle):
    def __init__(self, vehicle_number, brand, rental_price, engine_capacity):
        super().__init__(vehicle_number, brand, rental_price)
        self.engine_capacity = engine_capacity
        
car = Car(
    "KA01AB1234",
    "Toyota",
    1000,
    5
)

bike = Bike(
    "KA02XY5678",
    "Yamaha",
    500,
    150
)

car.display_details()
bike.display_details()

print(car.calculate_rental(3))
print(bike.calculate_rental(4))