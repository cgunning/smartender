import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
print("RED LED on")
GPIO.output(17,GPIO.HIGH)
time.sleep(1)
print("RED LED off")
GPIO.output(17,GPIO.LOW)
print("GREEN LED on")
GPIO.output(22,GPIO.HIGH)
time.sleep(1)
print("GREEN LED off")
GPIO.output(22,GPIO.LOW)
print("BLUE LED on")
GPIO.output(27,GPIO.HIGH)
time.sleep(1)
print("BLUE LED off")
GPIO.output(27,GPIO.LOW)

