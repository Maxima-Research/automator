import socket

class Server():
    def __init__(self, ip, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((str(ip), port))
        self.server.listen(5)
        self.data = ""

    def launch(self):
        print("LOADING network interface")









    def receive(self,queue):
        while True:
            buffer = self.recv(1024)

            if not buffer:
                self.send("ACK!")
                self.close()
                break
            self.data += buffer