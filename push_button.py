#SUTD-MIT hackathon
#Jacob Miske

import RPi.GPIO as GPIO

def button_call(channel):
    print("Button pushed ")


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(12, GPIO.RISING, callback=button_call)

message = input("Press Enter to quit \n\n")
GPIO.cleanup()

