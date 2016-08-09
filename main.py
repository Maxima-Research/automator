from __future__ import division

import socket
import threading
from Queue import Queue

import json
import requests
import datetime


class office:
    def __init__(self,name,address, state):
        self.name = name
        self.address = address
        self.state = state

class controller():
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
                client.close()
                print self.name + ": Command sent successfully."

        except:
            print "Error: Unable to connect to controller."

class ac:
    def __init__(self,name, state, temperature):
        self.name = name
        self.state = state
        self.temperature = temperature
        self.mode = "Day"

    def setPower(self, controller, desired_state):
        if (desired_state == 'Off'):
            controller.sendCommand("sendir,1:1,2,37993,1,1,144,72,18,18,18,54,18,18,18,54,18,18,18,54,18,18,18,54,18,18,18,54,18,18,18,54,18,54,18,18,18,54,18,18,18,54,18,54,18,54,18,54,18,18,18,18,18,54,18,54,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,54,18,54,18,54,18,54,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,54,18,54,18,54,18,54,18,54,18,18,18,18,18,18,18,18,18,18,18,54,18,54,18,3700\x0D\x0A")
            self.state = "Off"
            self.temperature = 80
        elif(desired_state == 'On'):
            controller.sendCommand("sendir,1:1,1,38109,1,1,144,72,18,18,18,54,18,18,18,54,18,18,18,54,18,18,18,54,18,18,18,54,18,18,18,54,18,54,18,18,18,54,18,18,18,54,18,54,18,54,18,54,18,18,18,18,18,54,18,54,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,54,18,54,18,54,18,54,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,54,18,54,18,54,18,54,18,54,18,18,18,18,18,18,18,54,18,54,18,54,18,54,18,3800\x0D\x0A")
            self.state = "On"

    def setTemperature(self, controller, temp):
        if temp == 79:
            controller.sendCommand("sendir,1:1,4,37993,1,1,144,72,18,18,18,54,18,18,18,54,18,18,18,54,18,18,18,54,18,18,18,54,18,18,18,54,18,54,18,18,18,54,18,18,18,54,18,54,18,54,18,54,18,18,18,18,18,54,18,54,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,54,18,54,18,54,18,54,18,18,18,18,18,18,18,54,18,54,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,54,18,54,18,54,18,54,18,54,18,18,18,18,18,18,18,18,18,54,18,18,18,54,18,3700")
        elif temp == 78:
            controller.sendCommand("sendir,1:1,5,37993,1,1,144,72,18,18,18,54,18,18,18,54,18,18,18,54,18,18,18,54,18,18,18,54,18,18,18,54,18,54,18,18,18,54,18,18,18,54,18,54,18,54,18,54,18,18,18,18,18,54,18,54,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,54,18,54,18,54,18,54,18,54,18,18,18,54,18,54,18,54,18,18,18,18,18,18,18,54,18,54,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,54,18,54,18,54,18,54,18,54,18,18,18,18,18,18,18,54,18,54,18,54,18,18,18,3700")
        elif temp == 82:
            controller.sendCommand("sendir,1:1,1,38109,1,1,144,72,18,18,18,54,18,18,18,54,18,18,18,54,18,18,18,54,18,18,18,54,18,18,18,54,18,54,18,18,18,54,18,18,18,54,18,54,18,54,18,54,18,18,18,18,18,54,18,54,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,54,18,54,18,54,18,54,18,18,18,18,18,18,18,54,18,54,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,54,18,54,18,54,18,54,18,54,18,18,18,18,18,18,18,54,18,54,18,54,18,54,18,3800")
        elif temp == 80:
            controller.sendCommand("sendir,1:1,7,38109,1,1,144,72,18,18,18,54,18,18,18,54,18,18,18,54,18,18,18,54,18,18,18,54,18,18,18,54,18,54,18,18,18,54,18,18,18,54,18,54,18,54,18,54,18,18,18,18,18,54,18,54,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,54,18,54,18,54,18,54,18,18,18,18,18,18,18,54,18,54,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,54,18,18,18,18,18,54,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,54,18,54,18,54,18,54,18,54,18,18,18,18,18,18,18,54,18,18,18,18,18,54,18,3800")

        self.temperature = temp

    def getPower(self):
        return self.state

    def getTemperature(self):
        return self.temperature

class sensor:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.currentTemp = 0
        self.outsideTemp = 0

    def printTempStats(self):
        print str(datetime.datetime.now())
        print "Outside Temperature: " + str(self.outsideTemp)
        print "Inside Temperature: " + str(self.currentTemp)


def getWeather():
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=NewYork&APPID=7bc2fb26c56440d720e853b22d3e6781')
    data = json.loads(r.text)

    kelvin = data['main']['temp']

    fahrenheit = (kelvin * (9 / 5)) - 459.67
    return fahrenheit

def receiveTemperature(sensor,queue):
    # Get temperature

    data = ""

    while True:
        buffer = sensor.recv(1024)

        if not buffer:
            sensor.send("ACK!")
            sensor.close()
            break

        data += buffer

    #Convert response into JSON string
    #Remove first 23 characters
    data = data[24:]

    #Remove any text that starts a new line
    data = data[:data.find('\n')-1]

    #Clean out bad characters
    data = data.replace('%20','',10)

    sensorData = json.loads(data)

    queue.put(sensorData['sensor'][0]['tempf'])


def main():
    officeController = controller("Office", "192.168.1.248", "OFF", 4998)
    officeSensor = sensor("Office", "192.168.1.249")
    officeAC = ac("Office", "Off", 80)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 8080))
    server.listen(5)

    command_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    command_server.bind(("0.0.0.0", 8081))
    command_server.listen(5)

    change_counter = 0

    while True:
        client, addr = server.accept()

        if (addr[0] == officeSensor.address):
            q = Queue(1)
            officeSensor.thread = threading.Thread(target=receiveTemperature, args=(client,q))
            officeSensor.thread.start()

            #Get inside and outside temperatures
            officeSensor.currentTemp = q.get(1)
            officeSensor.outsideTemp = getWeather()

            #Print inside and outside temperatures
            officeSensor.printTempStats()


            if if datetime.now() >= time(22,0) and datetime.now() <= time(8,0):
                if officeAC.mode == "Day":
                        officeAC.setTemperature(officeController, 82)
                        officeAC.mode = "Night"
                elif officeAC.mode == "Night":
                    if officeSensor.outsideTemp <= float(73) & officeSensor.currentTemp < float(88):
                        officeAC.setPower(officeController,"Off")
                        change_counter = 20
            else:




            if officeAC.state == "On":
                #If between 10PM and 7AM set temperature to 82 and outside temp is greater than 73
                if datetime.now() >= time(22,0) and datetime.now() <= time(8,0):

                elif
                # If Outside temp is below 74 degrees turn off AC if AC is on
                elif
                    print "Action: Turn off."
                    officeAC.setPower(officeController, "Off")
                #If AC is on, but temperature is extremely low, reduce thermostat
                elif officeSensor.currentTemp >= float(88):
                    if change_counter > 0:
                        officeAC.setTemperature(officeController, (officeAC.temperature - 2))
                        change_counter = 20
                        print "Action: Reduce temperature setting to %." % (officeAC.temperature)
                elif officeSensor.currentTemp <= 80:
                    if change_counter > 0:
                        officeAC.setTemperature(officeController,(officeAC.temperature + 2))
                        change_counter = 20
                        print "Action: Reduce temperature setting to %." % (officeAC.temperature)


                else:
                    print "Action: Nothing to do."

            elif(officeSensor.outsideTemp < officeSensor.currentTemp):

                if float(officeSensor.currentTemp) - float(officeSensor.outsideTemp) > float(5):
                    if officeAC.state == "Off":
                        officeAC.setPower(officeController, "On")
                        print "Action: Turning on AC."
                    elif officeAC.state == "On":
                        print "Action: Leave AC on."

                elif officeAC.state == "On":
                    officeAC.setPower(officeController, "Off")
                    print "Action: Turn off AC."
                else:
                        print "Action: Nothing to do."

            elif officeAC.state == "Off":

            #If change_counter was previously set, decrement counter by 1 every minute
            if change_counter > 0:
                change_counter -= 1
                print change_counter

            print "\n"
        else:



main()
