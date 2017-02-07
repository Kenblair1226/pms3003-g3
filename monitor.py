#!/usr/bin/python

import time
import datetime
import os
import httplib, urllib
import g5
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
p = GPIO.PWM(16, 50)  # channel=16 frequency=50Hz
p.start(0)

air=g5.g5sensor()
try:
    while True:
        try:
            pmdata=air.read("/dev/ttyAMA0")
        except:
            pmdata=[0,0,0,0,0,0,0,0,0,0,0,0]
    	    continue
	print pmdata

	a = pmdata[5] * 2
        if a > 100:
            p.ChangeDutyCycle(100)
        else:
            p.ChangeDutyCycle(a)

        # thingspeak
        params = urllib.urlencode({'field1': pmdata[3], 'field2': pmdata[4], 'field3': pmdata[5], 'key':'YOUR_KEY'})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        try:
            tconn = httplib.HTTPConnection("api.thingspeak.com:80")
            tconn.request("POST", "/update", params, headers)
            response = tconn.getresponse()
            data = response.read()
            tconn.close()
        except:
            continue
        time.sleep(300)

except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
