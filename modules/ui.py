class UI():
    def __init__(self):




class network_ui():
    def __init__(self, ip, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("0.0.0.0", 8080))
        self.server.listen(5)


