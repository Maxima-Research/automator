#! python3
# main.py -- automator
# 02/10/2017

import logging
logging.basicConfig(filename='log.txt', level=logging.Debug, format='%(ascitime)s - %(level name)s - %(message)s')

import threading
import time

#Import Custom modules
import controller from controller

def main():
    threads = []

    configuration = config('av_room.txt')

    


main()




