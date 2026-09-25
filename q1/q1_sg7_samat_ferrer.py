"""
#05, Reginald Andrei D. Ferrer
9-SAMAT
"""

class Glassware:
    def __init__(self, typeofglassware):
        self.typeofglassware = typeofglassware
        print("I have ", self.typeofglassware)


class Beaker(Glassware):
    def __init__(self):
        super().__init__("beaker")


class Tray:
    def __init__(self):
        self.beakers = [Beaker() for i in range(5)]
        print("Tray created with", len(self.beakers), "beakers")

    def __del__(self):
        self.beakers.clear()
        print("Tray gone, beakers erased")


tray = Tray()

del tray

print(tray)

    