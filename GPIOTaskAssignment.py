import Adafruit_BBIO.GPIO as GPIO
pinIn = "P8_14"
GPIO.setup(pinIn,GPIO.IN)
GPIO.setup("USR0",GPIO.OUT)

while 1:
  val = GPIO.input(pinIn)
  print("Hello")
  if val:
     GPIO.output("USR0",GPIO.LOW)
  else:
     GPIO.output("USR0",GPIO.HIGH)
