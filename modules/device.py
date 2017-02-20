from configobj import ConfigObj

class Device():
    def __init__(self, properties):
        self.name = properties['name']
        self.model = properties['model']
        self.type = properties['type']
        self.state = properties['state']

        self.commands = {}
        self.commands['ir'] = {}
        self.commands['rs232'] = {}

        try:
            print('LOADING .... ' + self.name + ' command set.')

            commands = ConfigObj('devices/' + self.model + '.ini')

            if not commands:
                print('ERROR: No commands found.')

            #Import commandset
            try:
                for protocol in commands:
                    print
                    protocolType = commands[protocol]
                    for mode in protocolType.items():
                        print(mode)
                        self.commands[protocol][mode] = {}
                        for command, code in mode.items():
                            print('LOADING ' + str(protocol).upper() + ' ' + command + ' ' + code)
                            self.commands[protocol][mode][command] = code
            except Exception as error:
                print('ERROR: Loading ' + protocol + ' commands: ' + str(error))
        except Exception as error:
            print('ERROR: Loading ' + self.name + ' commands:' + str(error))
