import RPi.GPIO as GPIO
import time

LED1 = 26
LED2 = 16
LED3 = 20
LED4 = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED3,GPIO.OUT)
GPIO.setup(LED4,GPIO.OUT)

try:
    while True:
        GPIO.output(LED1,GPIO.HIGH)
        GPIO.output(LED2,GPIO.HIGH)
        GPIO.output(LED3,GPIO.HIGH)
        GPIO.output(LED4,GPIO.HIGH)
        time.sleep(1.0)
        GPIO.output(LED1,GPIO.LOW)
        GPIO.output(LED2,GPIO.LOW)
        GPIO.output(LED3,GPIO.LOW)
        GPIO.output(LED4,GPIO.LOW)
        time.sleep(1.0)

except KeyboardInterrupt:
    pass

GPIO.cleanup()

