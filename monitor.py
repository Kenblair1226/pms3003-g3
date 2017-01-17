#!/usr/bin/python

import time
import datetime
import os
import httplib, urllib
import g5
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 50)  # channel=12 frequency=50Hz
p.start(0)

air=g5.g5sensor()
try:
    while True:
        try:
            pmdata=air.read("/dev/ttyAMA0")
        except:
            pmdata=[0,0,0,0,0,0]
    	continue

        if pmdata[5] > 100:
            p.ChangeDutyCycle(100)
        else:
            p.ChangeDutyCycle(pmdata[5])

        # # thingspeak
        # params = urllib.urlencode({'field1': pmdata[3], 'field2': pmdata[4], 'field3': pmdata[5], 'key':'YOUR WRITE KEY'})
        # headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        # try:
        #     tconn = httplib.HTTPConnection("api.thingspeak.com:80")
        #     tconn.request("POST", "/update", params, headers)
        #     response = tconn.getresponse()
        #     data = response.read()
        #     tconn.close()
        # except:
        #     continue
        time.sleep(1)

except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
