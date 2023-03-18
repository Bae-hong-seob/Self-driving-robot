import RPi.GPIO as GPIO
import time

SW1 = 5
SW2 = 6
SW3 = 13
SW4 = 19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

oldSw = [0,0,0,0]
newSw = [0,0,0,0]
cnt = [0,0,0,0]

try:
    while True:
        newSw[0] = GPIO.input(SW1)
        if newSw[0] != oldSw[0]:
            oldSw[0] = newSw[0]
            
            if newSw[0] == 1:
                cnt[0] = cnt[0] + 1
                print("SW1 click",cnt[0])
            
            time.sleep(0.2)
        
        newSw[1] = GPIO.input(SW2)
        if newSw[1] != oldSw[1]:
            oldSw[1] = newSw[1]
            
            if newSw[1] == 1:
                cnt[1] = cnt[1] + 1
                print("SW2 click",cnt[1])
            
            time.sleep(0.2)
            
        newSw[2] = GPIO.input(SW3)
        if newSw[2] != oldSw[2]:
            oldSw[2] = newSw[2]
            
            if newSw[2] == 1:
                cnt[2] = cnt[2] + 1
                print("SW3 click",cnt[2])
            
            time.sleep(0.2)
            
        newSw[3] = GPIO.input(SW4)
        if newSw[3] != oldSw[3]:
            oldSw[3] = newSw[3]
            
            if newSw[3] == 1:
                cnt[3] = cnt[3] + 1
                print("SW4 click",cnt[3])
            
            time.sleep(0.2)

except KeyboardInterrupt:
    pass

GPIO.cleanup()


