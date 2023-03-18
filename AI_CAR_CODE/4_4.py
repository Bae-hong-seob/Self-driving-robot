import threading
import serial
import time

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)

gData = ""

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
            elif gData.find("back") >= 0:
                gData = ""
                print("ok back")
            elif gData.find("left") >= 0:
                gData = ""
                print("ok left")
            elif gData.find("right") >= 0:
                gData = ""
                print("ok right")
            elif gData.find("stop") >= 0:
                gData = ""
                print("ok stop")

    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    task1 = threading.Thread(target = serial_thread)
    task1.start()
    main()
    bleSerial.close()
    

