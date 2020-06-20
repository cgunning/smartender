import RPi.GPIO as GPIO
import time
import threading

class Pump:
    pin = 0
    flowRate = 0
    def __init__(self, pin, flowRate):
        self.pin = pin
        self.flowRate = flowRate
        GPIO.setup(pin, GPIO.OUT)

    def getEstimatedPourTime(self, amount):
        return amount/self.flowRate*60

    def pour(self, amount):
        t = threading.Thread(target=self.pourInternal, args=(amount,))
        t.start()
        return t # returning thread in case we want to wait for it to be done in calling function

    def start(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.pin, GPIO.LOW)

    def pourInternal(self, amount):
        GPIO.output(self.pin, GPIO.HIGH)
        print("print poured " + str(amount) + " with a flow rate of " + str(self.flowRate))
        time.sleep(amount/self.flowRate*60)
        GPIO.output(self.pin, GPIO.LOW)

    def toString(self):
        return "pin: " + str(self.pin) + ", flowRate: " + str(self.flowRate)
