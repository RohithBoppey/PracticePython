class Car:
    wheels = 4

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def printCar(self):
        print("Name: ", self.name, " Price: ", self.price)

    def compareCarOnPrice(self, c2):
        if(self.price > c2.price):
            self.printCar()
        else:
            c2.printCar()

    # Class methods

    @classmethod
    def noOfWheels(cls):
        return cls.wheels



#main

c0 = Car("Maruti 800", 150000)
c1 = Car("Alto1", 200000)
c2 = Car("Alto2", 180000)
c3 = Car("Alto3", 190000)

list = [c0, c1, c2, c3]
list.sort(key = lambda x: x.name, reverse=True)
for i in list:
    i.printCar()

print(Car.noOfWheels())
