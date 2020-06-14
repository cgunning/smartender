from classes import Pump
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pump1 = Pump.Pump(23, 60)
pump2 = Pump.Pump(24, 60)

pump1.pour(8)
