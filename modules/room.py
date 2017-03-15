class Room(object):
    def __init__(self, roomConfig):
        self.name = roomConfig['name']
        self.location = roomConfig['location']
        self.power = roomConfig['power']
        self.default_activity = roomConfig['default_activity']
        self.current_activity = None
        self.devices = {}
        self.activities = {}

        print('CREATING ' + self.name + ' in ' + self.location + ' Room Object.\n')

        # for device in self.devices:
        #     for device.state in self.devices[device]:
        #         if device.state == self.activities[activity][device]

    def loadActivity(self, activity, controller):
        if activity == 'default':
            self.current_activity = self.default_activity
        else:
            self.current_activity = activity

        for x in self.activities[self.current_activity][x].items():
            print(x)

    def printActivities(self):
        print(self.activities)