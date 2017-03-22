from modules.device import Device

class Activity(object):
    def __init__(self, activity, devices):
        self.devices = {}

        for k, v in activity.items():
            if k == 'devices':
                for x in v.keys():
                    # print(x)
                    # print(activity[k][x])
                    self.devices[x] = Device(activity[k][x])
                break

            setattr(self, k, v)
            print(str(k) + ': ' + str(v))

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