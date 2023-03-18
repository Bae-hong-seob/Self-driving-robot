import RPi.GPIO as GPIO
import time

LED1 = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1,GPIO.OUT)

try:
    while True:
        GPIO.output(LED1,GPIO.HIGH)
        time.sleep(1.0)
        GPIO.output(LED1,GPIO.LOW)
        time.sleep(1.0)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
