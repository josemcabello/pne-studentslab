
class Vehicle():
    def set_speed(self, speed=0):
        self.speed = speed

class Car(Vehicle):
    def __init__(self, brand, speed=0):
        self.car_brand = brand
        self.speed = speed

class Ferrari(Car):
    def __int__(self):
        super().__init__("Ferrari")
        self.music = "Classic"
    def make_cabrio(self):
        self.speed = 20
        self.music = "loud"
        return "WoW"

mycar = Car("Renault")
yourcar = Ferrari("Ferrari")
print(yourcar.car_brand)
yourcar.set_speed(120)
print(yourcar.speed)

print(yourcar.make_cabrio(), "The music is", yourcar.music, "and speed is", yourcar.speed)