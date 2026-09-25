"""
#05, Reginald Andrei D. Ferrer
9-SAMAT
"""

class Car:
    def __init__(self,brand,model,battery=35):
        self.brand = model
        self.model = model
        self.battery = battery
    def go(self,distance):
        self.battery -= distance / 20
        print("You travelled", distance)
        print("You have",self.battery,"wH left")
    def charge(self,wH):
        self.battery += wH
        print("You recharged with", wH, "wH")
        
car = Car("Geely", "EX5")
while car.battery > 0:
    act = input("What do we do? (g or c) ")
    if act== "g":
        distance = int(input("How far? "))
        car.go(distance)
    elif act == "c":
        wH = int(input("How much to charge?" ))
        car.charge(wH)
    else:
        print("Invalid Action")
        
print("Game over, you ran out of batteries")
