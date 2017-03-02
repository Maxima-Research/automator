from configobj import ConfigObj

class Device():
    def __init__(self, properties):
        self.name = properties['name']
        self.model = properties['model']
        self.type = properties['type']
        self.power = properties['power']

        self.commands = {}
        self.commands['ir'] = {}
        self.commands['rs232'] = {}
        self.commands['ip'] = {}

        try:
            print('LOADING .... ' + self.name + ' command set.')

            commands = ConfigObj('devices/' + self.model + '.ini')

            if not commands:
                print('ERROR: No commands found.')

            #Import commandset
            try:
                for protocol in commands:
                    for options in commands[protocol].keys():
                        self.commands[protocol][options] = {}
                        for command, code in commands[protocol][options].items():
                            print('LOADING ' + str(protocol).upper() + ' Command ' + str(options).upper() + ' ' + command + ' ' + code)
                            self.commands[protocol][options][command] = code
            except Exception as error:
                print('ERROR: Loading ' + protocol + ' commands: ' + str(error))
        except Exception as error:
            print('ERROR: Loading ' + self.name + ' commands:' + str(error))
