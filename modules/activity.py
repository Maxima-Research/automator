class Activity():
    def __init__(self, activity, devices):
        self.name = activity['name']
        self.description = activity['description']
        self.input = activity['input']
        self.output = activity['output']

        self.device = {}

        #Verify setting refers to a device

        print(self.name)
        for device in activity:
            if device in devices:
                self.device[device] = {}
                for x,y in activity[device].items():
                    self.device[device][x] = y
                    print(device + ': ' + str(x) + ':' + str(y))