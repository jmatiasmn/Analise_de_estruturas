class LigthSwitch():
    def __init__(self):
        self.switchIsOn = False
    def turnOn (self):
        self.switchIsOn = True
    def turnOff (self):
        self.switchIsOn = False
    def show(self):
        print(self.switchIsOn)

TurnLight1 = LigthSwitch()
TurnLight2 = LigthSwitch()

TurnLight1.show()
TurnLight1.turnOn()
TurnLight2.show()
TurnLight2.turnOn()
TurnLight2.show()
TurnLight1.show()

