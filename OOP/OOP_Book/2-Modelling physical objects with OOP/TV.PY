class TV():
    def __init__(self,brand,location):
        self.isOn = False
        self.isMuted = False
        #default list channels:
        self.ChannelList = [2,4,5,7,9,11,20,36,44,54,65]
        self.nChanells = len(self.ChannelList)
        self.chanelIndex = 0
        self.VOLUME_MINIMUM = 0 #CONSTANTE
        self.VOLUME_MAXIMUM = 10 #CONSTANTE
        self.volume = self.VOLUME_MAXIMUM
        self.brand = brand
        self.location = location
    
    def power(self):
        self.isOn = not self.isOn
    
    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1
    
    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume - 1
    
    def channelUp(self):
        if not self.isOn:
            return
        self.chanelIndex = self.chanelIndex + 1
        if self.chanelIndex > self.nChanells:
            self.chanelIndex = 0 
    
    def channelDown(self):
        if not self.isOn:
            return
        self.chanelIndex = self.chanelIndex - 1
        if self.chanelIndex < 0 :
            self.chanelIndex = self.nChanells - 1

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted 
    
    def setChannel (self,newChannel):
        if newChannel in self.ChannelList:
            self.chanelIndex = self.ChannelList.index(newChannel)
        
    def showInfo(self):
        print()
        print(f'Status of TV: {self.brand}')
        print(f'Location: {self.location}')

        print('TV Status: ')
        if self.isOn:
            print('    TV is : On')
            print(f'    Channel is: : {self.ChannelList[self.chanelIndex]}')
            if self.isMuted:
                print(f'    Volume is: {self.volume}, (sound is muted)')
            else:
                print(f'     Volume is: {self.volume} ')
        else:
            print('TV is: Off')


# Main code
oTV1 = TV('Samsung', 'Family room')  # create the TV object
oTV2 = TV('Sony', 'Bedroom')

# Turn the TV on and show the status
oTV1.power()
oTV2.power()
oTV1.showInfo()
oTV2.showInfo()

# Change the channel up twice, raise the volume twice, show status
oTV1.channelUp()
oTV1.channelUp()
oTV1.volumeUp()
oTV1.volumeUp()
oTV1.showInfo()

# Turn the TV off, show status, turn the TV on, show status
oTV2.power()
oTV2.showInfo()
oTV2.power()
oTV2.showInfo()

# Lower the volume, mute the sound, show status
oTV1.volumeDown()
oTV2.mute()
oTV2.showInfo()

# Change the channel to 11, mute the sound, show status
oTV1.setChannel(11)
oTV2.setChannel(3)

print(f'oTV1 variables: {vars(oTV1)}')