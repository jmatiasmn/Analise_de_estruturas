class DimmerSwitch():
    def __init__(self):
        self.switchisOn = False
        self.brightnesss = 0
    
    def turnOn(self):
        self.switchisOn = True
    
    def turnOff(self):
        self.switchisOn = False
    
    def raiseLevel(self):
        if self.brightnesss < 10:
            self.brightnesss == self.brightness + 1

    def lowerLevel(self):
        if self.brightnesss > 0:
            self.brightnesss == self.brightness - 1
    def show(self):
        print(f'Switch is on? {self.switchisOn}')
        print(f'Brightness is : {self.brightnesss}')
        
# Main code
oDimmer = DimmerSwitch()
# Turn switch on, and raise the level 5 times
oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()
# Lower the level 2 times, and turn switch off
oDimmer.lowerLevel()
oDimmer.lowerLevel()
oDimmer.turnOff()
oDimmer.show()
# Turn switch on, and raise the level 3 times
oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()