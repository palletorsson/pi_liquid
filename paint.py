#!/usr/bin/python

use_schedule = False

import RPi.GPIO as GPIO

if use_schedule == True:
    import schedule

import time
import datetime

GPIO.setmode(GPIO.BCM) 

relay_pin = 24

GPIO.setup(relay_pin,GPIO.OUT)

def job():
    print("I'm working...")
    print "turn on relay and timeout"
    GPIO.output(relay_pin, GPIO.HIGH) 
    time.sleep(5)    
    GPIO.output(relay_pin, GPIO.LOW)  
    print datetime.datetime.now()

if use_schedule == True:
    #schedule.every(1).minutes.do(job)
    schedule.every().monday.at("15:30").do(job)
    schedule.every().friday.at("15:15").do(job)
while True:
    if use_schedule == True:
        schedule.run_pending()
        time.sleep(1)
    else:
        job()
        time.sleep(5)   
        
