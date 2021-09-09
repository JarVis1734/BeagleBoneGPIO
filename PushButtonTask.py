# Push Button to toggle the LED 
import Adafruit_BBIO.GPIO as GPIO
import time

pinIn = "P9_14"
pinOut = "P9_11"

GPIO.setup(pinIn,GPIO.IN)
GPIO.setup(pinOut,GPIO.OUT)
ledState = False

while 1: 
 if GPIO.input(pinIn): #reducing debouncing using software method
  time.sleep(0.1)
  if GPIO.input(pinIn):
   time.sleep(0.001)
   print "Button Pressed...!!!"
   ledState = not ledState
   GPIO.output(pinOut,ledState)
   print "Current State of Led is:"
   print(ledState)
