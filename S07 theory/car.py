class Car:
    def __init__(self, brand, speed = 0):
        self.car_brand = brand
        self.speed = speed
    def set_speed(self, speed):
        self.speed = speed
class Ferrari(Car):
    pass

mycar = Car("Renault", 50)

mycar.set_speed(80)

yourcar = Ferrari("Ferrari")
print(yourcar.car_brand)
