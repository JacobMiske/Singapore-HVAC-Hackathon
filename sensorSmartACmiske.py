#Script for SUTD-MIT Hackathon, running variety of sensors on RPi for smart AC response
#Jacob Miske

import RPi.GPIO as GPIO

GPIO.setwarnings(False) #ignore warnings
GPIO.setmode(GPIO.BOARD) #Use physical numbering
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #the config is as a pull down

while True:
    if GPIO.input(12) == GPIO.HIGH:
        print("button pushed")
        
