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
from modules.activity import Activity

def main():
    print('Launching Automator v1')
    print('Loading configuration ...\n')

    #Create array for GUI and Scheduler threads
    threads = []

    #Read config.ini for room configuration. If bad syntax end application cleanly.
    configuration = ConfigObj("config.ini")
    try:
        myRoom = Room(configuration['Room'])
        devices = configuration['Devices']
        controller = configuration['Controller']
        activities = configuration['Activities']
    except Exception as error:
        print('Unable to verify config.ini syntax. Please review and relaunch application.')
        exit()

    print('[Rooms]')
    #Create Room object
    print('Creating ' + myRoom.name + ' in ' + myRoom.location + ' Room Object.\n')

    print('[Devices]')
    #Create Devices dictionary object
    for device in devices:
        myRoom.devices[device] = Device(devices[device])

        print('Creating .... ' + str(myRoom.devices[device].name) + ' Object.')
    print('\n')

    print('[Controllers]')
    #Create Controller object
    myController = Controller(controller)
    print('Creating .... ' + str(myController.name) + ' Controller at ' + str(myController.ip) + '.')
    print('\n')


    print('[Activities]')
    #Create Activities object
    for activity in activities:
        myRoom.activities[activity] = Activity(activities[activity], myRoom.devices)

        print('Creating .... ' + str(myRoom.activities[activity].name) + ' Activity.')
    print('\n')

    #Check last state of room ... dirty/clean shutdown
    lastState = ConfigObj('last_state.ini')
    try:
        if lastState['state'] == 'on':
            print('Recovering from dirty shutdown')
        else:
            print('Starting clean start.')
    except Exception as error:
        print('Clean start ...')


    #Launch GUI thread

    #Launch Scheduler thread

    #End program
    print('Exiting Automator...')
    exit()


if __name__ == '__main__':
    main()
