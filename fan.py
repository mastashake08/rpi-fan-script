import os
from time import sleep
import RPi.GPIO as GPIO
import re
import sys
pin = int(sys.argv[1])
base_temp = float(sys.argv[2])
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

def measure_temp():
    raw = os.popen('vcgencmd measure_temp').readline()
    m = re.match("temp=(\d+\.?\d*)'C", raw)
    if not m:
        raise ValueError("Unexpected temperature string: " + raw)
    return float(m.group(1))

while True:
    temp = measure_temp()
#    print 'Temperature from vcgencmd: {}'.format(temp)

    if temp > base_temp:
        #print 'Turning on GPIO 4'
        GPIO.output(pin, True)
    else:
        #print 'Turning off GPIO 4'
        GPIO.output(pin, False)
    sleep(3)
