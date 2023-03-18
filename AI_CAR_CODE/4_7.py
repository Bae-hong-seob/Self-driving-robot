import threading
import serial
import time
import RPi.GPIO as GPIO

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)

gData = ""

SW1 = 5
SW2 = 6
SW3 = 13
SW4 = 19

PWMA = 18
AIN1 = 22
AIN2 = 27

PWMB = 23
BIN1 = 25
BIN2 = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(PWMA,GPIO.OUT)
GPIO.setup(AIN1,GPIO.OUT)
GPIO.setup(AIN2,GPIO.OUT)

GPIO.setup(PWMB,GPIO.OUT)
GPIO.setup(BIN1,GPIO.OUT)
GPIO.setup(BIN2,GPIO.OUT)

L_Motor = GPIO.PWM(PWMA,500)
L_Motor.start(0)

R_Motor = GPIO.PWM(PWMB,500)
R_Motor.start(0)

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

BUZZER = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER,GPIO.OUT)

p = GPIO.PWM(BUZZER,391)
p.stop()

def motor_go(speed):
    GPIO.output(AIN1,0)
    GPIO.output(AIN2,1)
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN1,0)
    GPIO.output(BIN2,1)
    R_Motor.ChangeDutyCycle(speed)

def motor_back(speed):
    GPIO.output(AIN1,1)
    GPIO.output(AIN2,0)
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN1,1)
    GPIO.output(BIN2,0)
    R_Motor.ChangeDutyCycle(speed)
    
def motor_left(speed):
    GPIO.output(AIN1,1)
    GPIO.output(AIN2,0)
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN1,0)
    GPIO.output(BIN2,1)
    R_Motor.ChangeDutyCycle(speed)
    
def motor_right(speed):
    GPIO.output(AIN1,0)
    GPIO.output(AIN2,1)
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN1,1)
    GPIO.output(BIN2,0)
    R_Motor.ChangeDutyCycle(speed)

def motor_stop():
    GPIO.output(AIN1,0)
    GPIO.output(AIN2,1)
    L_Motor.ChangeDutyCycle(0)
    GPIO.output(BIN1,0)
    GPIO.output(BIN2,1)
    R_Motor.ChangeDutyCycle(0)

def serial_thread():
    global gData
    while True:
        data = bleSerial.readline()
        data = data.decode()
        gData = data

def main():
    global gData
    try:
        while True:
            if gData.find("go") >= 0:
                gData = ""
                print("ok go")
                motor_go(50)
                GPIO.output(LED1,GPIO.HIGH)
                GPIO.output(LED2,GPIO.HIGH)
                GPIO.output(LED3,GPIO.LOW)
                GPIO.output(LED4,GPIO.LOW)
            elif gData.find("back") >= 0:
                gData = ""
                print("ok back")
                motor_back(50)
                GPIO.output(LED1,GPIO.LOW)
                GPIO.output(LED2,GPIO.LOW)
                GPIO.output(LED3,GPIO.HIGH)
                GPIO.output(LED4,GPIO.HIGH)
            elif gData.find("left") >= 0:
                gData = ""
                print("ok left")
                motor_left(50)
                GPIO.output(LED1,GPIO.HIGH)
                GPIO.output(LED2,GPIO.LOW)
                GPIO.output(LED3,GPIO.HIGH)
                GPIO.output(LED4,GPIO.LOW)
            elif gData.find("right") >= 0:
                gData = ""
                print("ok right")
                motor_right(50)
                GPIO.output(LED1,GPIO.LOW)
                GPIO.output(LED2,GPIO.HIGH)
                GPIO.output(LED3,GPIO.LOW)
                GPIO.output(LED4,GPIO.HIGH)
            elif gData.find("stop") >= 0:
                gData = ""
                print("ok stop")
                motor_stop()
                GPIO.output(LED1,GPIO.LOW)
                GPIO.output(LED2,GPIO.LOW)
                GPIO.output(LED3,GPIO.LOW)
                GPIO.output(LED4,GPIO.LOW)
            elif gData.find("bz_on") >= 0:
                gData = ""
                print("ok buzzer on")
                p.start(50)
                p.ChangeFrequency(391)
            elif gData.find("bz_off") >= 0:
                gData = ""
                print("ok buzzer off")
                p.stop()
            
                
            if GPIO.input(SW1) == 1 or GPIO.input(SW2) == 1 or GPIO.input(SW3) == 1 or GPIO.input(SW4) == 1 :
                motor_stop()
                GPIO.output(LED1,GPIO.LOW)
                GPIO.output(LED2,GPIO.LOW)
                GPIO.output(LED3,GPIO.LOW)
                GPIO.output(LED4,GPIO.LOW)
                p.stop()

    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    task1 = threading.Thread(target = serial_thread)
    task1.start()
    main()
    bleSerial.close()
    GPIO.cleanup()
