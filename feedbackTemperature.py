#SUTD MIT Hackathon
#PID Control of Servos

import sys
import time
import datetime
import serial
import sys
import Adafruit_DHT
import signal
import RPi.GPIO as GPIO
import pprint

# Welcome message
print("Welcome! \n")
print("Raspberry Pi Interface for PID Controlled AC Fans \n")


#Relay test
print('relay test')
GPIO.setmode(GPIO.BCM) #default board channels
GPIO.setwarnings(False) #Remove anticipated "channel is already in use" warning
GPIO.setup(17, GPIO.OUT) #GPIO 17 is an output
GPIO.output(17, 0)
time.sleep(3)
GPIO.output(17, 1) 
print('relay text over \n')

#setup serial information and port addressing
print('Setting Up Serial Connection ... \n')
ser = serial.Serial(
    port='/dev/ttyACM2',
    baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout=1
)
print('Serial Configured')
# Open a file to write towards
text_file = open("sensorData.txt", "w")
ts = time.time() #get time since epoch
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('Usage: sudo ./Adafruit_DHT.py [11|22|2302] <GPIO pin number>')
    print('Example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO pin #4')
    sys.exit(1)


# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

#other sensors
humidity1, temperature1 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 27)
humidity2, temperature2 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 22)

print("h and T 0")
print(str(humidity) + ' ' + str(temperature) + 'C')
print("h and T 1")
print(str(humidity1) + ' ' + str(temperature1) + 'C')
print("h and T 2")
print(str(humidity2) + ' ' + str(temperature2) + 'C')

humidityValues = []
temperatureValues = []

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)


#Test Sensor
print('Testing DHT 2302 \n')
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    text_file.write('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    text_file.write('\n')
    time.sleep(3)
    print(st)
    text_file.write(st)
    text_file.write('\n')
else:
    print('Failed to get reading. Try again!')              
print('Test Complete \n')


'''
time.sleep(5)
ser.write('0,0,0\n')
time.sleep(10)
ser.write('50,50,50\n')
time.sleep(10)
ser.write('100,0,100\n')
ser.write('0,0,0\n')

'''
#General variables
optimalTemperature = 22 #degrees C
personnelPrefer = 0 #start at zero, negative numbers
                    #lower the optimal temp, higher number raise the optimal temp



def PIDdriveServo(optimalT, actualT):
    #takes in an optimal T and actual T, outputs a string for
    #serial communication to the arduino
    error = int(round(actualT - optimalTemperature))
    K_P = 1
    K_I = 1
    K_D = 1
    servoPos = ''
    openPosition = 50
    closePosition = 0
    servoPos = servoPos + str(K_P*error)

    if int(servoPos) > 50:
        servoPos = '50'
    elif int(servoPos) < 0:
        servoPos = '0'
    return  servoPos 

# Timeout Class asking for personnel input
class InputTimedOut(Exception):
    pass
def inputTimeOutHandler(signum, frame):
    "called when read times out"
    print 'interrupted!'
    raise InputTimedOut
signal.signal(signal.SIGALRM, inputTimeOutHandler)
def input_with_timeout(timeout=5):
    foo = ""
    try:
            print 'You have {0} seconds to enter -2: too cold, -1 cool, 0: okay, 1: warm, or 2 for too hot...'.format(timeout)
            signal.alarm(timeout)
            foo = raw_input()
            signal.alarm(0)    #disable alarm
    except InputTimedOut:
            pass
    return foo

s = input_with_timeout(timeout=5)
print 'You entered', s



while True: #run indefinitely
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    humidity1, temperature1 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 27)
    humidity2, temperature2 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 22)


    if humidity is not None and temperature is not None:
        print('Room 0 \n')
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        text_file.write('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        text_file.write('\n')
        time.sleep(3) #run for 3 sec
        text_file.write(st)
        text_file.write('\n')

        print('Room 1 \n')
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature1, humidity1))
        text_file.write('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature1, humidity1))
        text_file.write('\n')
        time.sleep(3) #run for 3 sec
        text_file.write(st)
        text_file.write('\n')

        print('Room 2 \n')
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature2, humidity2))
        
        text_file.write('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature2, humidity2))
        text_file.write('\n')
        time.sleep(3) #run for 4 hour, 60s times 240
        text_file.write(st)
        text_file.write('\n')

        
        servoPosition0 = PIDdriveServo(optimalTemperature, temperature)
        servoPosition1 = PIDdriveServo(optimalTemperature, temperature1)
        servoPosition2 = PIDdriveServo(optimalTemperature, temperature2)
        fanPos = 50

        ser.write(servoPosition0 + ',' + servoPosition1 + ',' + servoPosition2 + ',' + fanPos + '\n')
        s = input_with_timeout(timeout=5)
        print 'You entered', s
        personnelPrefer = personnelPrefer + s;
        time.sleep(1)
    else:
        print('Failed to get reading. Try again!')



#Break out of program
sys.exit(1)


