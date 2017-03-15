class Activity(object):
    def __init__(self, activity, devices):
        for k, v in activity.items():
            setattr(self, k, v)
            print(str(k) + ': ' + str(v))

        self.device = {}

        # #Verify setting refers to a device
        #
        # for device in activity:
        #     if device in devices:
        #         self.device[device] = {}
        #         for x,y in activity[device].items():
        #             self.device[device][x] = y
        #             print(device + ': ' + str(x) + ':' + str(y))

        print('CREATING .... ' + str(self.name) + ' Activity.\n \n')

    def __repr__(self):
        return self.name