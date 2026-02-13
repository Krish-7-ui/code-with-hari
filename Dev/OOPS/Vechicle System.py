class Vehicle():
    def __init__(self,brand,speed=0):
        self.brand = brand
        self.speed = speed

    def move(self):
        print("Car or bike is moving")

class Car(Vehicle):
    def __init__(self, brand, speed):
        super().__init__(brand, speed)

    def move(self):
        print(f"Car from the brand {self.brand} moving at {self.speed} Kms speed")

class Bike(Vehicle):
    def __init__(self, brand, speed=0):
        super().__init__(brand, speed)

    def move(self):
        print(f"Bike from the brand {self.brand} moving at {self.speed} Kms speed")


car = Car("BMW",250)
bike = Bike("RE",150)

car.move()
bike.move()

