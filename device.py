class Device():
    def __init__(self, properties):
        self.name = properties['name']
        self.model = properties['address']
        self.type = properties['type']
        self.state = properties['state']
