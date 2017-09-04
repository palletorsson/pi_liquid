
#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM) 

# Setup schema -----------------------------------------------------------------
# 2   | 4  | 6    | 8   | 10   | 12   | 14  | 16  | 18   | 20  | 22  | 24  | 26  | 
# 5V! | 5V | GnD! | G14 | G15  | G18! | GnD | G23 | G24! | GND | G25 | G8  | G7  | relay 
# 3V! | G2 | G3   | G4  | GnD! | G17! | GnD | G22 | 3V   | G10 | G9  | G11 | GnD | moist
# 1   | 3  | 5    | 7   | 9    | 11   | 13  | 15  | 17   | 19  | 21  | 23  | 27  | 

# moist -----------------
# pin1  : sensor VCC 
# pin9  : sensor GnD
# pin9  : sensor D0 - G17
# pin9  : sensor A0 - G23

# relay ------------------
# pin2  : relay VCC
# pin6  : relay GnD
# pin18 : relay IN1 - G24


moist_pin  = 17
moist_pin_a = 23
relay_pin = 24

GPIO.setup(moist_pin,GPIO.IN)
GPIO.setup(moist_pin_a,GPIO.IN)
GPIO.setup(relay_pin,GPIO.OUT)
GPIO.output(relay_pin, GPIO.LOW) 

while True:
    moist_value = GPIO.input(moist_pin)
    moist_value_a = GPIO.input(moist_pin_a)
    print "the", moist_value_a

    if moist_value == 1:
        print "turn on relay and timeout"
        GPIO.output(relay_pin, GPIO.HIGH) 
        time.sleep(5)    
        GPIO.output(relay_pin, GPIO.LOW)   
    else:
        print "plants not dry"

    time.sleep(2)

GPIO.cleanup()

