class Room():
    def __init__(self, roomConfig):
        self.name = roomConfig['name']
        self.location = roomConfig['location']
        self.state = roomConfig['state']
        self.activity = roomConfig['default_activity']
        self.devices = {}
        self.activities = {}
