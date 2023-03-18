import RPi.GPIO as GPIO
import time

BUZZER = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER,GPIO.OUT)

p = GPIO.PWM(BUZZER,391)
p.start(50)

try:
    while True:
        p.start(50)
        p.ChangeFrequency(391)
        time.sleep(0.2)
        
        p.stop()
        time.sleep(0.1)
        
        p.start(50)
        p.ChangeFrequency(391)
        time.sleep(0.2)
        
        p.stop()
        time.sleep(0.1)
        
        p.stop()
        time.sleep(2.0)

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()


