class Room(object):
    def __init__(self, roomConfig):
        self.name = roomConfig['name']
        self.location = roomConfig['location']
        self.power = roomConfig['power']
        self.default_activity = roomConfig['default_activity']
        self.current_activity = None
        self.devices = {}
        self.activities = {}
        self.controller = {}

        print('CREATING ' + self.name + ' in ' + self.location + ' Room Object.\n')

        # for device in self.devices:
        #     for device.state in self.devices[device]:
        #         if device.state == self.activities[activity][device]

    def printActivities(self):
        print(self.activities)