class Activity():
    def __init__(self, activity, devices):
        self.name = activity['name']
        self.description = activity['description']
        self.input = activity['input']
        self.output = activity['output']

        self.device = {}

        #Verify setting refers to a device
        for device in activity:
            #print(device)
            if device in devices:
                for x,y in activity[device].items():
                    self.device[x] = y