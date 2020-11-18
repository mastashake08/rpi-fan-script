import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO
import re
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

def measure_temp():
    raw = os.popen('vcgencmd measure_temp').readline()
    m = re.match("temp=(\d+\.?\d*)'C", raw)
    if not m:
        raise ValueError("Unexpected temperature string: " + raw)
    return float(m.group(1))

while True:
    temp = measure_temp()
#    print 'Temperature from vcgencmd: {}'.format(temp)

    if temp > 65:
        #print 'Turning on GPIO 4'
        GPIO.output(4, True)
    else:
        #print 'Turning off GPIO 4'
        GPIO.output(4, False)
    sleep(3)
