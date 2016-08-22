from __future__ import division

import socket
import threading
from Queue import Queue

import json
import requests
import datetime

import getopt
import sys

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
                print self.name + ": Command sent successfully."
                client.close()

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
        self.insideTemp = 0
        self.outsideTemp = 0

    def printTempStats(self):
        print datetime.datetime.now().strftime('%Y-%M-%D %H:%M:%S')
        print "Outside Temperature: " + str(self.outsideTemp)
        print "Inside Temperature: " + str(self.insideTemp)


def getWeather():
    try:
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=NewYork&APPID=7bc2fb26c56440d720e853b22d3e6781')
        data = json.loads(r.text)

        kelvin = data['main']['temp']

        fahrenheit = (kelvin * (9 / 5)) - 459.67
        return fahrenheit
    except:
        print "ERROR: Unable to get outside temperature."
        return 75

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

def isNowInTimePeriod(startTime, endTime, nowTime):
    startTime = startTime.time()
    endTime = endTime.time()

    if startTime < endTime:
        return nowTime >= startTime and nowTime <= endTime
    else: #Over midnight
        return nowTime >= startTime or nowTime <= endTime

def usage():
    print "Options:"
    print "-m, --mode <on|off>      Specify whether AC is already powered on."

def main():

    officeController = controller("Office", "192.168.1.248", "Off", 4998)
    officeSensor = sensor("Office", "192.168.1.249")
    officeAC = ac("Office", "Off", 80)

    try:
        opts, args = getopt.getopt(sys.argv[1:], "m:", ["mode"])
    except getopt.GetoptError as err:
        print str(err)
        sys.exit()

    for o,a in opts:
        if o in ("-m","--mode"):
            if a == "on":
                officeAC.state = "On"
                print "[*] AC is already turned on."


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
            officeSensor.insideTemp = q.get(1)
            officeSensor.outsideTemp = getWeather()

            #Print inside and outside temperatures
            officeSensor.printTempStats()

            now = datetime.datetime.now()
            now_time = now.time()

            if officeAC.state == "On" and change_counter <= 0:
                #If between 10PM and 7AM set temperature to 82 and outside temp is greater than 73
                if isNowInTimePeriod(datetime.datetime.strptime("22:00",'%H:%M'),datetime.datetime.strptime("7:00",'%H:%M'),now_time):
                    print("Night time mode.")
                    if officeSensor.outsideTemp < float(86) and officeSensor.insideTemp < float(88):
                        officeAC.setTemperature(officeController, 82)
                        print("Action: Set temperature to 82.")
                        change_counter = 20
                    # If Outside temp is below 74 degrees turn off AC if AC is on
                    elif officeSensor.outsideTemp <= float(73) and officeSensor.insideTemp < float(84):
                        officeAC.setPower(officeController,"Off")
                        print("Action: Turn off.")
                        change_counter = 20
                    # If inside temperature is high and outside temperature is high turn down temp setting
                    elif officeSensor.outsideTemp >= float(90) and officeSensor.insideTemp >= float(88):
                            officeAC.setTemperature(officeController, (officeAC.temperature - 2))
                            print("Action: reduce temperature.")
                            change_counter = 20

                #If day time, AC is on, but temperature is high, reduce thermostat
                elif officeSensor.insideTemp >= float(88):
                    officeAC.setTemperature(officeController,(officeAC.temperature - 2))
                    change_counter = 20
                    print("Action: Increase temperature setting to %" % (officeAC.temperature))
                #If daytime, AC is on, but temperature is very low, increase thermostat
                elif officeSensor.insideTemp <= 80 and officeAC.temperature >= float(82):
                    officeAC.setTemperature(officeController,(officeAC.temperature + 2))
                    change_counter = 20
                    print("Action: Reduce temperature setting to %." % (officeAC.temperature))
                elif officeSensor.outsideTemp <= float(73) and officeSensor.insideTemp < float(84):
                        print "Action: Turn off AC."
                        officeAC.setPower(officeController,"Off")
                        change_counter = 20
                else:
                    print "Action: Nothing to do."

            if officeAC.state == "Off" and change_counter <= 0:
                if officeSensor.outsideTemp > float(73) and officeSensor.insideTemp > float(86):
                    print "Action: Turn on AC."
                    officeAC.setPower(officeController,"On")
                    change_counter = 20
                elif officeSensor.insideTemp > float(88.5):
                    print "Action: Turn on AC."
                    officeAC.setPower(officeController,"On")
                    change_counter = 20

            #If change_counter was previously set, decrement counter by 1 every minute
            if change_counter > 0:
                change_counter -= 1
                print change_counter

            print "\n"

main()
