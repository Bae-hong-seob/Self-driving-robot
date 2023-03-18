import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)

while True:
    GPIO.output(26,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(26,GPIO.LOW)
    time.sleep(1.0)
