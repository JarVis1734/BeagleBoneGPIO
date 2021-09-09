# 7 Segment display interfacing with BeagleBone
import Adafruit_BBIO.GPIO as GPIO
import time

num = {
    0:(1,1,1,1,1,1,0),
    1:(0,1,1,0,0,0,0),
    2:(1,1,0,1,1,0,1),
    3:(1,1,1,1,0,0,1),
    4:(0,1,1,0,0,1,1),
    5:(1,0,1,1,0,1,1),
    6:(1,0,1,1,1,1,1),
    7:(1,1,1,0,0,0,0),
    8:(1,1,1,1,1,1,1),
    9:(1,1,1,1,0,1,1)
}
segments = ["P8_9","P8_7","P8_8","P8_12","P8_14","P8_11","P8_13"]
# seg a,b,c,d,e,f,g

#initialization of pins
for segment in segments:
 GPIO.setup(segment,GPIO.OUT)
 GPIO.output(segment,0)

while True:
 #counting of number begin
 for count in range(0,10):
  #assigning of output at pins
  for loop in range(0,7):
   GPIO.output(segments[loop],num[count][loop])
  print(count,num[count])
  time.sleep(1)

GPIO.cleanup()

