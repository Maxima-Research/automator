#! python3
# main.py -- automator
# 02/10/2017

import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(ascitime)s - %(level name)s - %(message)s')

#Requires pip install ConfigObj
from configobj import ConfigObj

import threading
import time

#Import Custom modules
from modules.room import Room
from modules.device import Device
from modules.controller import Controller

def main():
    #Create array for GUI and Scheduler threads
    threads = []

    configuration = ConfigObj("config.ini")

    #Create Room object
    myRoom = Room(configuration['Room'])
    print('Creating ' + myRoom.name + ' Object.\n')
        
    #Create Device objects
    for device in configuration['Devices']:
        myRoom.devices.append(Device(configuration['Devices'][device]))
        print('Creating ... ' + str(myRoom.devices[device].keys) + ' Object.\n')

    #Create Controller object
#    for controller in configuration.config['Controller']:
#        myController = Controller(configuration.config('Controller')
        
    #Check last state of room ... dirty/clean shutdown
    
    #Launch GUI thread

    #Launch Scheduler thread

if __name__ == '__main__':
    main()
