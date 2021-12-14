class Vehicle:
    def __init__(self, price, model_name):
        self.price = price
        self.model_name = model_name
        print("This is a Vehicle")

    def printVehicleContent(self):
        s = "Model: "+ self.model_name + " Price: ", self.price
        print(s)

    def updatePrice(self, percent):
        newPrice = self.price + (self.price * percent /100)
        self.price = newPrice

    def function1(self):
        print("This is a Vehicle")

# main

class Car(Vehicle):
    wheels = 4
    def __init__(self, price, model_name):
        self.price = price
        self.model_name = model_name
        print("This is a Car Vehicle")

    def function1(self):
        print("This is a Car Vehicle")

a = Vehicle(50000, "Maruti 800")
b = Car(15000.25, "Kia Super Car")
b.printVehicleContent()