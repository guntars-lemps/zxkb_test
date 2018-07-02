#!/usr/bin/python

import time
import os
import sys
import json
import signal
import RPi.GPIO as GPIO

# Color for ON key 
CON = '\033[93m'

# Color for OFF key
COFF = '\033[0m'

# Base GPIO pin for address A8
GPIO_ADDR_BASE = 4

# Base GPIO pin for data D0
GPIO_DATA_BASE = 12


keys = {
    'rows':
        [
            {'keys': 
                [
                    {'sym':'1', 'addr':3, 'data':0},
                    {'sym':'2', 'addr':3, 'data':1}, 
                    {'sym':'3', 'addr':3, 'data':2},
                    {'sym':'4', 'addr':3, 'data':3},
                    {'sym':'5', 'addr':3, 'data':4},
                    {'sym':'6', 'addr':4, 'data':4},
                    {'sym':'7', 'addr':4, 'data':3}, 
                    {'sym':'8', 'addr':4, 'data':2},
                    {'sym':'9', 'addr':4, 'data':1},
                    {'sym':'0', 'addr':4, 'data':0},
                ]
            },
            {'keys': 
                [
                    {'sym':'Q', 'addr':2, 'data':0},
                    {'sym':'W', 'addr':2, 'data':1}, 
                    {'sym':'E', 'addr':2, 'data':2},
                    {'sym':'R', 'addr':2, 'data':3},
                    {'sym':'T', 'addr':2, 'data':4},
                    {'sym':'Y', 'addr':5, 'data':4},
                    {'sym':'U', 'addr':5, 'data':3}, 
                    {'sym':'I', 'addr':5, 'data':2},
                    {'sym':'O', 'addr':5, 'data':1},
                    {'sym':'P', 'addr':5, 'data':0},
                ]
            },
            {'keys': 
                [
                    {'sym':'A', 'addr':1, 'data':0},
                    {'sym':'S', 'addr':1, 'data':1}, 
                    {'sym':'D', 'addr':1, 'data':2},
                    {'sym':'F', 'addr':1, 'data':3},
                    {'sym':'G', 'addr':1, 'data':4},
                    {'sym':'H', 'addr':6, 'data':4},
                    {'sym':'J', 'addr':6, 'data':3}, 
                    {'sym':'K', 'addr':6, 'data':2},
                    {'sym':'L', 'addr':6, 'data':1},
                    {'sym':'EN', 'addr':6, 'data':0},
                ]
            },
            {'keys': 
                [
                    {'sym':'CS', 'addr':0, 'data':0},
                    {'sym':'Z', 'addr':0, 'data':1}, 
                    {'sym':'X', 'addr':0, 'data':2},
                    {'sym':'C', 'addr':0, 'data':3},
                    {'sym':'V', 'addr':0, 'data':4},
                    {'sym':'B', 'addr':7, 'data':4},
                    {'sym':'N', 'addr':7, 'data':3}, 
                    {'sym':'M', 'addr':7, 'data':2},
                    {'sym':'SS', 'addr':7, 'data':1},
                    {'sym':'SP', 'addr':7, 'data':0},
                ]
            }
       ]
}


def signal_handler(signal, frame):
    print ""
    print 'You pressed Ctrl+C'
    sys.exit(0)


def setupGPIO():
    GPIO.setmode(GPIO.BCM)

    # set address pins as output
    for n in range(8):
        GPIO.setup(GPIO_ADDR_BASE + n, GPIO.OUT)

    # set data pins as input
    for n in range(5):
        GPIO.setup(GPIO_DATA_BASE + n, GPIO.IN)


def readKey(address, data):
    for n in range(8):
        GPIO.output(GPIO_ADDR_BASE + n, GPIO.LOW if (address == n) else GPIO.HIGH)
    return (GPIO.input(GPIO_DATA_BASE + data) == GPIO.LOW)


def printKeyboardState():
    for row in keys['rows']:
        for key in row['keys']:
            pressed = readKey(key['addr'], key['data'])
            print (CON if pressed else "") + key['sym'].rjust(3) + COFF,
        print


signal.signal(signal.SIGINT, signal_handler)

setupGPIO()

# main loop
while True:

    os.system("clear")

    print "Press keys on ZX Keyboard for test, press Ctrl+C to exit"
    print ""

    printKeyboardState()

    time.sleep(0.1)

