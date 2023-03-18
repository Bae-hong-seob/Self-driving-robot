import RPi.GPIO as GPIO
import time

PWMA = 18
AIN1 = 22
AIN2 = 27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA,GPIO.OUT)
GPIO.setup(AIN1,GPIO.OUT)
GPIO.setup(AIN2,GPIO.OUT)

L_Motor = GPIO.PWM(PWMA,500)
L_Motor.start(0)

try:
    while True:
        GPIO.output(AIN1,0)
        GPIO.output(AIN2,1)
        L_Motor.ChangeDutyCycle(100)
        time.sleep(1.0)
        
        GPIO.output(AIN1,0)
        GPIO.output(AIN2,1)
        L_Motor.ChangeDutyCycle(0)
        time.sleep(1.0)
        
except KeyboardInterrupt:
    pass

GPIO.cleanup()