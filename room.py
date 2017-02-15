class Room():
    def __init__(self, roomConfig):
        self.name = roomConfig['Name']
        self.location = roomConfig['Location']
        self.state = roomConfig['State']
        self.activity = roomConfig['Activity']
        self.devices = []
        self.activities = []
