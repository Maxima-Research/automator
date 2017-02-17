class Device():
    def __init__(self, properties):
        self.name = properties['name']
        self.model = properties['model']
        self.type = properties['type']
        self.state = properties['state']
