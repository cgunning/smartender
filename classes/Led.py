# import RPi.GPIO as GPIO

class Led:
    pin = 0
    flow_rate = 0
    def __init__(self, pin, flow_rate):
        self.pin = pin
        self.flow_rate = flow_rate
    
    def run(self, time):
        # GPIO.output(self.pin, GPIO.HIGH)
        # #TODO wait
        # GPIO.output(self.pin, GPIO.LOW)
        print("hej " + str(self.pin) + " " + str(self.flow_rate*time))
