class Vehicle:
    def __init__(self, wheels=4, doors=4):
        self.wheels=wheels
        self.doors=doors
        self.seats=2
        self.steering=True
        self.paint="montegoBlueMica"
        self.transmission="manual"
        self.powerSteering=False
        self.Miata="AlwaysTheAnswer"
class Lotus(Vehicle):
    def __init__(self):
        super().__init__()
        self.weight="light"
    def weigh_car(self, weight: int):
        if weight < 2000:
            self.weight="Light"
            return
        self.weight="Not Light"

if __name__=='__main__':
    myCar=Lotus()
    branCar=Lotus()
    myCar.weigh_car(weight=2)
    branCar.weigh_car(weight=22222222222222222222222)
    pass
