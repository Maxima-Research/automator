class Room():
    def __init__(self, roomConfig):
        self.name = roomConfig['name']
        self.location = roomConfig['location']
        self.state = roomConfig['state']
        self.default_activity = roomConfig['default_activity']
        self.devices = {}
        self.activities = {}

    def load(self, activity):
        if activity == 'default':
            print("LOADING: Activity " + self.default_activity + '...')
