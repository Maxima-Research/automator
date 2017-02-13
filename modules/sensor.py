class sensor():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.insideTemp = 0
        self.outsideTemp = 0

    def printTempStats(self):
        print datetime.datetime.now().strftime('%Y-%M-%D %H:%M:%S')
        print "Outside Temperature: " + str(self.outsideTemp)
        print "Inside Temperature: " + str(self.insideTemp)