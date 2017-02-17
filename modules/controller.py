class Controller():
    def __init__(self, name, address, state, port):
        self.name = name
        self.address = address
        self.port = port
        self.state = state

    def sendCommand(self, command):
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        try:
            client.connect((self.address,self.port))

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
