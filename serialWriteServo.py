#SUTD MIT Hackathon
#Jacob Miske

import time
import serial
import sys



ser = serial.Serial(
    port='/dev/ttyACM1',
    baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout=1
)
time.sleep(5)
ser.write('0,0,0\n')
time.sleep(10)
ser.write('50,50,50\n')
time.sleep(10)
ser.write('100,0,100\n')

ser.write('0,0,0\n')

