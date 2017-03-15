class Controller(object):
    def __init__(self, controllerConfig):
        for k, v in controllerConfig.items():
            setattr(self, k, v)
            print(str(k) + ': ' + str(v))

        print('CREATING .... ' + str(self.name) + ' Controller at ' + str(self.ip) + '.\n')

    def sendCommand(self, command):
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        try:
            client.connect((self.ip,self.port))

            client.send(command)

            while True:
                received_len = 1
                response = ""

                while received_len:
                    data = client.recv(4096)
                    received_len = len(data)
                    response += data

                    if received_len < 4096:
                        break
                print(self.name + ": Command sent successfully.")
                client.close()

        except:
            print("Error: Unable to connect to controller.")
