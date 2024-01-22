# 10. Class Exercise:
# Create a Python class representing a car with methods for accelerating and braking.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerating(self, speeding):
        self.speed += speeding
        print(f"The car is speeding. speed is {self.speed} mph")

    def braking(self, braking):
        if self.speed - braking > 0:
            self.speed -= braking
            print(f"The car is braking. speed is {self.speed} mph")
my_car = Car(make="Mercedes", model="G500", year=2022)
my_car.accelerating(30)
my_car.braking(10)
my_car.accelerating(50)
