# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 15:39:36 2020

@author: wanghaoran
Edited: Benedict 


This script runs on the openSIM UC2 module and ensures two things:
    1. Triggering of the camera 
    2. Display SIM-pattern on the DMD 
"""

import pygame
import numpy as np

import RPi.GPIO as GPIO
import time

def trigger(gpiopin):
    GPIO.output(gpiopin, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(gpiopin, GPIO.LOW)
    time.sleep(0.2)
    


'''
Initialize; Define Variables
'''
#import matplotlib.pyplot as plt
pygame.init()
myreso = [640, 360]

''' 
Please connect the camera to the Raspberry Pi as follows: 
GND  => GND 
Trigger 0 => Raspi GPIO 18
'''
camerapin = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(camerapin, GPIO.OUT)

'''
Compute SIM Pattern:
TOOO: Has to be replaced with more sophisticated stuff..
    '''
myconst = 3
myunits = []

myunit = np.ones((myconst*2,myconst*2))
myunit[:,0:myconst] = 0
myunit = np.array(myunit)
myunits.append(myunit)
myunit = np.ones((myconst*2,myconst*2))
myunit[0:myconst,:] = 0
myunits.append(myunit)

xx = myreso[0]//myunit.shape[0]+1
yy = myreso[1]//myunit.shape[1]+1

myimg = np.tile(myunit,(xx*2,yy*2))
myimg = myimg[:myreso[0],:myreso[1]]

# Initialize PyGame output
display = pygame.display.set_mode(myreso,pygame.FULLSCREEN)
surf = pygame.surfarray.make_surface(myimg*255)
pygame.mouse.set_visible(False) # turn of the mouse cursor
running = True
iiter=0

try:
    while running:            
        print(iiter)
        iiter += 1
        display.blit(surf, (0, 0))
        pygame.display.update()
        trigger(camerapin)
        myimg = np.roll(myimg,2,axis=0)
        surf = pygame.surfarray.make_surface(myimg*255)
        time.sleep(1)
except:
    GPIO.cleanup()