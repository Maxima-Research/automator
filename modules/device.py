from configobj import ConfigObj

class Device():
    def __init__(self, properties):
        self.name = properties['name']
        self.model = properties['model']
        self.type = properties['type']
        self.state = properties['state']

        self.commands = {}
        try:
            print('Loading .... ' + self.name + ' command set.')

            command = ConfigObj('devices/' + self.model + '.ini')

            #Import IR commands
            try:
                irCommands = command['IR']
                for command, code in irCommands.items():
                        self.commands['IR'][command] = irCommands[code]
            except Exception as error:
                print('No IR commands found.')
        except Exception as error:
            print('ERROR: Loading ' + self.name + ' commands:' + error)
